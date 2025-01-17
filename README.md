# 5 Best in City Data Scraper

This repository contains a Python script for scraping business information from the website [5BestinCity](https://5bestincity.com/). It extracts data such as city names, business categories, business names, owners, ratings, and reviews, and saves the information into a CSV file.

---

## Features

- **Web scraping with BeautifulSoup**: Fetches business details from various categories and cities listed on the website.
- **Dynamic data extraction**: Handles nested data, including business categories, names, ratings, and reviews.
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
   git clone https://github.com/your-username/5-best-in-city.git
   cd 5-best-in-city
   ```

2. **Run the script**:
   Execute the Python script to scrape data and save it to a CSV file:
   ```bash
   python 5bestcity.py
   ```

3. **Output**:
   The data will be saved in a CSV file (`5BestinCity.csv`) in the same directory.

---

## Data Description

The script outputs a CSV file with the following columns:
- **City**: Name of the city.
- **Business Category**: Category of the business (e.g., restaurants, gyms).
- **Business**: Name of the business.
- **Name**: Owner or manager's name.
- **Rate**: Rating of the business.
- **Review**: Number of reviews.

---

## Output Example

![image](https://github.com/user-attachments/assets/d91c9f3f-ca1c-4587-87ff-c57061d761ff)

---

## Limitations

- The script depends on the current structure of the [5BestinCity](https://5bestincity.com/) website. Changes in the HTML structure may break the scraper.
- Network issues or site restrictions may affect the scraping process.

---


## Author

Developed by [Janak Dobariya](https://github.com/JanakDobariya). Feel free to reach out for questions or contributions!

---
