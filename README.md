# 5BestInCity data scraper

This repository contains an educational Python script for collecting public business-listing snapshots from [5BestInCity](https://5bestincity.com/). It records the city, category, listing name, displayed rating text, and source URL in CSV format.

---

## Features

- **Web scraping with BeautifulSoup**: Fetches business details from various categories and cities listed on the website.
- **Bounded runs**: Processes one city by default so a test does not accidentally create excessive traffic.
- **Clear failures**: Uses timeouts and status checks, and does not overwrite an existing CSV when no records are found.
- **Data output**: Saves the scraped data into a CSV file for further analysis.

---

## Files in the Repository

1. **`5bestcity.py`**
   - The main script that handles web scraping.
   - Uses Python libraries like `requests`, `BeautifulSoup`, and `pandas`.
   - Outputs the scraped data into a CSV file named `5BestinCity.csv`.

2. **`5BestinCity_Data.csv`**
   - A sample CSV file containing data scraped from the website.

---

## Requirements

The script requires the following Python libraries:
- `requests`
- `BeautifulSoup` from `bs4`
- `pandas`

Install them using:
```bash
pip install -r requirements.txt
```

---

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JanakDobariya/5bestincity-Scraping.git
   cd 5bestincity-Scraping
   ```

2. **Run the script**:
   Execute the Python script to scrape data and save it to a CSV file:
   ```bash
   python 5bestcity.py --max-cities 1 --output 5BestinCity.csv
   ```

3. **Output**:
   The data will be saved in a CSV file (`5BestinCity.csv`) in the same directory.

---

## Data Description

The script outputs a CSV file with the following columns:
- **City**: Name of the city.
- **Business Category**: Category of the business (e.g., restaurants, gyms).
- **Business**: Name of the business.
- **Name**: Name shown on the listing card; the script does not assume this identifies an owner.
- **Rating Details**: Rating text displayed by the source page.
- **Source URL**: Page from which the record was collected.

---

## Output Example

![image](https://github.com/user-attachments/assets/d91c9f3f-ca1c-4587-87ff-c57061d761ff)

---

## Limitations

- The script depends on the current structure of the [5BestinCity](https://5bestincity.com/) website. Changes in the HTML structure may break the scraper.
- Network issues or site restrictions may affect the scraping process.
- The committed `5BestinCity_Data.csv` is a historical sample, not a live directory.
- Keep request volume low and follow the website's terms and robots guidance.

---


## Author

Developed by [Janak Dobariya](https://github.com/JanakDobariya). Feel free to reach out for questions or contributions!

---
