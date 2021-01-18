import requests
import csv
from bs4 import BeautifulSoup

def get_page(url):
    return requests.get(url).text

def get_data(html_page):

    soup = BeautifulSoup(html_page, 'html.parser')

    outputHead = []
    for th in soup.find_all('th'):
        outputHead.append(th.text)

    outputRows = []
    for tr in soup.find_all('tr'):
        tableColumns = tr.find_all('td')
        outputRow = []
        for tc in tableColumns:
            outputRow.append(tc.text)
        outputRows.append(outputRow)

    outputRows.insert(0, outputHead)

    return outputRows

def write_csv(filename, rows):

    with open(f'{filename}.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

if __name__ == "__main__":

    URL = 'http://127.0.0.1:8000/scraper'

    html_text = get_page(URL)
    rows = get_data(html_text)
    write_csv('scrape-tutorial', rows)