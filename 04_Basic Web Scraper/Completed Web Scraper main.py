#Basic Web Scraper

import requests
from bs4 import BeautifulSoup

print("=== Basic Web Scraper ===")

url = input("Enter Website URL: ")
try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text,"html.parser")

    headlines = soup.find_all("h1")

    if headlines:
        print("\nHeadlines Found:")

        file = open("headlines.txt", "w")

        for headline in headlines:
            text = headline.get_text(strip=True)
            print("_", text)
            file.write(text + "\n")

        file.close()

        print("\nHeadlines saved to headlines.txt")
    else:
        print("No headlines found.")

except requests.exceptions.RequestException as e:
    print("Error:", e)
