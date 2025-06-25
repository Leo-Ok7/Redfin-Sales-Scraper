import argparse
import logging
from scraper.fetcher import fetch_redfin_data
from scraper.parser import parse_redfin_json

def parse_args():
    parser = argparse.ArgumentParser(description="Redfin Real Estate Scraper CLI")
    parser.add_argument("--city", required=True, help="City to search")
    parser.add_argument("--status", default="sold", choices=["sold", "active"], help="Listing status")
    parser.add_argument("--beds", type=int, default=0, help="Minimum number of beds")
    parser.add_argument("--max-price", type=int, help="Maximum listing price")
    parser.add_argument("--output", default="csv", choices=["csv", "json", "df"], help="Output format")
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_args()

    logging.info("Gathering Redfin data")
    raw_data = fetch_redfin_data(args.city, args.status, args.beds, args.max_price)
    listings_df = parse_redfin_json(raw_data)

    if listings_df.empty:
        logging.warning("No listings were found.")
        return

    logging.info(f"Parsed {len(listings_df)} listings.")

    if args.output == "csv":
        listings_df.to_csv("redfin_listings.csv", index=False)
        logging.info("Saved to redfin_listings.csv")
    elif args.output == "json":
        listings_df.to_json("redfin_listings.json", orient="records")
        logging.info("Saved to redfin_listings.json")
    else:
        print(listings_df.head())

if __name__ == "__main__":
    main()