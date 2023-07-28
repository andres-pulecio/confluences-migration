"""
Confluence Page Data Fetcher

This script retrieves page information from the Confluence API for a list of specified spaces. It then saves the data to CSV files for each space.

The script uses the "requests" library to make API calls to Confluence and the "csv" library to write the data to CSV files.

Note: Please replace the "<TOKEN>" placeholder in the "headers" dictionary with a valid access token for Confluence API authentication.

Author: Andres Pulecio (apulecio)

"""

import requests
import csv

# Confluences Credentials
token = "<TOKEN>"

# List of Confluence spaces to fetch data from
espacios = ['~athayyil', '~avkumar', '~ayaseer', ...]

# List to store the fetched results
results = []

def main():
    for espacio in espacios:
        url = f"https://confluence.bbpd.io/rest/api/content?spaceKey={espacio}"
        fetch_data(url)
        with open(f"{espacio}.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["pageid", "title", "tinyui", "searchurl"])
            writer.writerows(results)
            print(espacio)

def fetch_data(url):
    headers = {'Authorization': 'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        handle_page_of_results(data)
        if "next" in data["_links"]:
            next_url = "https://confluence.bbpd.io" + data["_links"]["next"]
            fetch_data(next_url)

def handle_page_of_results(data):
    for result in data["results"]:
        pageid = result["id"]
        title = result["title"]
        tinyui = "https://confluence.bbpd.io" + result["_links"]["tinyui"]
        searchurl = "https://www.microsoft365.com/search?auth=2&home=1&q=" + title.replace(" ", "+")
        results.append([pageid, title, tinyui, searchurl])

if __name__ == "__main__":
    main()
    print("CSV files created successfully.")
