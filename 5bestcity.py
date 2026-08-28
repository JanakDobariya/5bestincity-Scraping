"""Collect business-listing snapshots from 5BestInCity."""

from __future__ import annotations

import argparse
import time
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://5bestincity.com/"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
    ),
}


def fetch_soup(session: requests.Session, url: str) -> BeautifulSoup:
    response = session.get(url, timeout=20)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def city_pages(home: BeautifulSoup) -> list[tuple[str, str]]:
    pages = []
    seen = set()
    for block in home.select("div.col-lg-2.col-md-6"):
        anchor = block.find("a", href=True)
        if not anchor:
            continue
        url = urljoin(BASE_URL, anchor["href"])
        if "businesses-in" not in url or url in seen:
            continue
        seen.add(url)
        pages.append((block.get_text(" ", strip=True), url))
    return pages


def category_pages(city_soup: BeautifulSoup) -> list[tuple[str, str, str]]:
    pages = []
    for block in city_soup.select("div.col-md-3"):
        headings = block.find_all("h3")
        lists = block.find_all("ul")
        for heading, item_list in zip(headings, lists):
            category = heading.get_text(" ", strip=True)
            for item in item_list.find_all("h4"):
                anchor = item.find("a", href=True)
                if anchor:
                    pages.append((category, item.get_text(" ", strip=True), urljoin(BASE_URL, anchor["href"])))
    return pages


def listing_rows(soup: BeautifulSoup, city: str, category: str, business: str, source_url: str) -> list[dict[str, str]]:
    names = soup.select("h3.notranslate")
    ratings = soup.select("span.rating-star")
    rows = []
    for index, name in enumerate(names):
        rating_text = ratings[index].get_text(" ", strip=True) if index < len(ratings) else ""
        rows.append(
            {
                "City": city,
                "Business Category": category,
                "Business": business,
                "Name": name.get_text(" ", strip=True),
                "Rating Details": rating_text,
                "Source URL": source_url,
            }
        )
    return rows


def scrape(max_cities: int | None, delay: float) -> pd.DataFrame:
    session = requests.Session()
    session.headers.update(HEADERS)
    home = fetch_soup(session, BASE_URL)
    cities = city_pages(home)
    if max_cities is not None:
        cities = cities[:max_cities]
    if not cities:
        raise RuntimeError("No city links were found; the site may be blocking requests or its markup changed.")

    rows = []
    for city_index, (city, city_url) in enumerate(cities, start=1):
        city_soup = fetch_soup(session, city_url)
        for category, business, listing_url in category_pages(city_soup):
            rows.extend(listing_rows(fetch_soup(session, listing_url), city, category, business, listing_url))
            if delay:
                time.sleep(delay)
        print(f"City {city_index}/{len(cities)}: {city}")
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-cities", type=int, default=1, help="limit the run while testing; omit with 0 for all cities")
    parser.add_argument("--delay", type=float, default=1.0, help="seconds between listing requests")
    parser.add_argument("--output", type=Path, default=Path("5BestinCity.csv"))
    args = parser.parse_args()
    if args.max_cities < 0 or args.delay < 0:
        raise SystemExit("--max-cities and --delay cannot be negative")

    try:
        data = scrape(args.max_cities or None, args.delay)
    except requests.RequestException as exc:
        raise SystemExit(f"Website request failed: {exc}") from exc
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc
    if data.empty:
        raise SystemExit("No listings were found; the existing CSV was not overwritten.")
    data.to_csv(args.output, index=False)
    print(f"Saved {len(data)} rows to {args.output}")


if __name__ == "__main__":
    main()
