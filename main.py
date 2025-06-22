from scraper.fetcher import fetch_redfin_gis_data
from scraper.parser import parse_redfin_json
import pandas as pd

def main():
    print("Starting Redfin data fetch...")

    raw_data = fetch_redfin_gis_data()
    if not raw_data:
        print("No data received from Redfin.")
        return

    print("Parsing the response...")
    listings_df = parse_redfin_json(raw_data)

    if listings_df.empty:
        print("No listings parsed from the response.")
        return

    print(f"Parsed {len(listings_df)} listings.")
    print(listings_df.head())

    output_path = "redfin_listings.csv"
    listings_df.to_csv(output_path, index=False)
    print(f"Saved results to {output_path}")

if __name__ == "__main__":
    main()
