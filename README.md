# CONFLUENCES PAGE DATA FETCHER
Script to extract tinyurls

This repository contains two Python scripts that will help you interact with the Confluence platform and save web pages using Selenium.

## Requirements
Before using these scripts, make sure you meet the following requirements:

Python 3 installed on your system.
Required libraries: requests, csv (installable via pip).
Selenium WebDriver for Google Chrome (ensure you have the version compatible with your browser).
A valid access token for the Confluence API (required for "confluence_page_data_fetcher.py").

## Description of the Scripts
- confluence_page_data_fetcher.py
This script allows you to retrieve page data from the Confluence platform using its REST API. The script will fetch information about the pages in the spaces provided in the "espacios" list. The retrieved data includes the page ID, title, short URL (tinyui), and a search URL in Microsoft 365.

- selenium_webpage_saver.py
This script utilizes the Selenium library to interact with the web browser (Google Chrome) and save web pages from Confluence. The script starts a browser instance, logs in to Confluence using the provided credentials, opens each URL from the "urls_to_save" list, and simulates a right-click to save the page as an HTML file. The saved files will be stored in the "files-to-upload" directory on the desktop.

- confluence_xml_saver.py
This script logs in to a Confluence website using provided credentials, navigates to a list of spaces and useres, and export all the information in .zip file.

## Usage Instructions
Make sure you meet the mentioned prerequisites.

To use "confluence_page_data_fetcher.py," open the file and provide the Confluence API access token in the "TOKEN" variable. Then, execute the script, and page data will be saved in CSV files with the name of each space.

To use "selenium_webpage_saver.py," ensure that Selenium WebDriver for Google Chrome is correctly configured, and the browser is installed on your system. Then, run the script, and web pages will be saved as HTML files in the "files-to-upload" directory on your desktop.
