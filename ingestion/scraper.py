from playwright.sync_api import sync_playwright
import pandas as pd
import time
import json
import os
from datetime import datetime

# Create directories if not exist
os.makedirs("../data/raw", exist_ok=True)
os.makedirs("../logs", exist_ok=True)

products = []
seen_ids = set()


def log_message(message):
    with open("../logs/scraper.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def handle_response(response):
    try:
        url = response.url

        # Filter possible product-related API endpoints
        if any(keyword in url for keyword in [
            "/api/",
            "product",
            "search"
        ]):

            content_type = response.headers.get("content-type", "")

            if "application/json" in content_type:
                data = response.json()

                def extract_products(obj):
                    if isinstance(obj, dict):

                        if (
                            ("id" in obj and "name" in obj) or
                            "price" in obj or
                            "selling_price" in obj
                        ):

                            product_id = str(obj.get("id") or obj.get("product_id") or obj.get("name"))

                            if product_id and product_id not in seen_ids:
                                seen_ids.add(product_id)

                                products.append({
                                    "product_id": product_id,
                                    "name": obj.get("name") or obj.get("title", ""),
                                    "brand": obj.get("brand", ""),
                                    "mrp": obj.get("mrp") or obj.get("max_retail_price"),
                                    "selling_price": obj.get("selling_price") or obj.get("price"),
                                    "inventory": obj.get("inventory") or obj.get("stock"),
                                    "unit": obj.get("unit") or obj.get("size"),
                                    "category": obj.get("category") or obj.get("sub_category"),
                                    "ingestion_time": datetime.now()
                                })

                        for value in obj.values():
                            extract_products(value)

                    elif isinstance(obj, list):
                        for item in obj:
                            extract_products(item)

                extract_products(data)

    except Exception as e:
        log_message(f"Error processing response: {e}")


def run_scraper():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.on("response", handle_response)

        print("Opening e-commerce site...")
        page.goto("https://blinkit.com/")
        page.wait_for_timeout(5000)

        input("Set location manually if required, then press ENTER...")

        search_query = "fresh fruits"
        print(f"Searching for: {search_query}")

        page.goto(f"https://blinkit.com/s/?q={search_query.replace(' ', '%20')}")
        page.wait_for_timeout(4000)

        # Scroll to load products
        for _ in range(20):
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(1500)

        print(f"Total products captured: {len(products)}")

        if products:
            df = pd.DataFrame(products)
            df = df.drop_duplicates(subset=["product_id"])

            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"../data/raw/products_{timestamp}.csv"

            df.to_csv(filename, index=False)

            print(f"Data saved to {filename}")
            log_message(f"Successfully saved {len(df)} products.")

        else:
            print("No products captured.")
            log_message("No products captured.")

        browser.close()


if __name__ == "__main__":
    run_scraper()
