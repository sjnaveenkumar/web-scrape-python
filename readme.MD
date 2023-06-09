# Web Scrapping using selectorlib in Python

An Flask web application for scraping data from websites using Selenium and Selectorlib.

## Prerequisites

- Python 3
- Flask
- Selenium
- Webdriver Manager
- Selectorlib

## Setup

1. Clone this repository: `git clone https://github.com/sjnaveenkumar/repo.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`

## Files

### app.py

This is the main file of the Flask application. It imports and initializes the necessary modules, defines the routes, and starts the server.

### scrape_service.py

This file contains functions for initializing a ChromeDriver, loading a webpage, and extracting data from the webpage using Selectorlib.

### search.py

This file contains a function for searching Amazon India using the search bar and returning the results.

### deals.py

This file contains a function for retrieving the top deals from Amazon India and returning the results.

### search_template.yml

This is the Selectorlib template file for extracting data from the search results page.

### top_deals_template.yml

This is the Selectorlib template file for extracting data from the top deals page.

## Usage

- To search for a product, navigate to `http://localhost:5050/search?query=<query>&page=<page_number>`, replacing `<query>` with the product you want to search for and `<page_number>` with the page number of the search results you want to view.
- To view the top deals, navigate to `http://localhost:5050/top-deals`.

## Credits

This project was created by Naveen. The Selectorlib library was created by [Scrapinghub](https://github.com/scrapinghub/selectorlib).

## Note

This project is designed to follow the robots.txt policy of Amazon website.