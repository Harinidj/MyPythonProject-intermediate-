import requests
from bs4 import BeautifulSoup
import csv

def scrape_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headings = [h2.text.strip() for h2 in soup.find_all(['h2', 'h3'])]
    paragraphs = [p.text.strip() for p in soup.find_all('p')]

    data = []
    for heading, paragraph in zip(headings, paragraphs):
        data.append({
            "Heading": heading,
            "Paragraph": paragraph
        })

    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Heading", "Paragraph"])
        writer.writeheader()
        writer.writerows(data)

def main():
    url = input("Enter the Wikipedia URL: ")
    filename = input("Enter the CSV filename: ") + ".csv"

    try:
        data = scrape_wikipedia(url)
        save_to_csv(data, filename)
        print("Data scraped and saved to CSV successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()

