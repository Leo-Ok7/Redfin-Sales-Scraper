**Redfin Sales Scraper**

This is a Python tool that fetches and saves real estate data from Redfin’s internal GIS API. It pulls recently sold property listings in a specific region (example: San Diego) and exports them to a clean CSV for analysis or research.

**Features**

* Direct API access - Fetches sold listings directly from Redfin’s backend (no need for browser automation).

* Relevant data extraction - Captures key details that includes the: 

    * Address, City

    * Price, Beds, Baths

    * Square Footage, Lot Size

    * Year Built, Sale Date

    * Listing URL

* Clean CSV output - Saves results as redfin_listings.csv for easy use with Excel, pandas, etc.

* Codebase is organized into modules for fetching, parsing, and running the script.

**Instructions on running the program**

1. Clone the repository
2. Install requirements
3. Run the CLI tool : python main.py --city "San Diego" --output csv. The scraper is currenrtly only configured to fetch listings for **San Diego**. You can also apply filters to the CLI argument -> Ex : python main.py --city "San Diego" --beds 3 --max-price 1000000 --output csv.

**Extra Notes**

* Uses a hardcoded Redfin GIS API URL. To scrape a different region, you need to inspect Redfin’s network traffic by looking for XHR requests to /gis? and input the appropriate URL.

* Redfin’s API responses are prefixed with {}&&, which needs to be stripped before parsing the JSON.

* I currently have the query filtered for sold listings only. It won’t work for rentals or active listings unless you update the URL parameters.

**Disclaimer**

Redfin.com's data is available publically so no private data is being collected. 
