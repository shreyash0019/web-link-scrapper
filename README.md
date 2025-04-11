# Web Link Scraper

This repository contains a simple Python script that extracts all hyperlinks from a given webpage and saves them into a text file named `myLinks.txt`. The script utilizes the `requests` and `beautifulsoup4` libraries to fetch and parse HTML content.

## Features
- Accepts any URL and automatically corrects it if the protocol (http/https) is missing.
- Parses all anchor tags (`<a>`) from the HTML.
- Extracts the `href` attribute values and stores them in a text file.
- Appends the links to the output file so multiple runs won't overwrite previous results.

## Prerequisites
Before running the script, make sure you have Python installed on your system. You also need to install the required dependencies listed in the `requirements.txt` file.

## Installation
To get started, clone the repository to your local machine and install the required Python packages. The dependencies include `beautifulsoup4` and `requests`.

## How to Use
1. Run the script in your terminal or command prompt.
2. When prompted, enter the URL of the website from which you want to extract links.
3. The script will fetch the webpage, extract all valid hyperlinks, and save them to `myLinks.txt` in the same directory.

## Output
The result is a plain text file (`myLinks.txt`) that contains one link per line. This file can be opened with any text editor or imported into other tools for further analysis.

## Use Cases
This script is ideal for:
- Developers learning web scraping techniques.
- Auditing or archiving website links.
- Research and data collection tasks.

---

### 👨‍💻 Author
Developed by [Shreyash Ingle](https://github.com/shreyash0019)

