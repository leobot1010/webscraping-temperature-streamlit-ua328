import time
import requests
import selectorlib
from time import gmtime, strftime
import sqlite3

connection = sqlite3.connect('data.db')

URL = 'https://programmer100.pythonanywhere.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# EXTRACT THE DATA FROM THE WEBSITE
def scrape(url):
    """ Scrape the page source from the url """
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


# WRITE THE DATA TO THE SQL DATABASE
def write_data(temperature):
    time = strftime('%y-%m-%d,%H:%M:%S', gmtime())
    date, time = time.split(',')

    print(f'Date: {date}')
    print(f'Time: {time}')
    print(f'Temperature: {temperature}')
    print(f'---------------')
    print()

    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?,?,?)", (date, temperature, time))
    connection.commit()


# EXECUTIVE FUNCTION, RUNS EVERY 5 SECONDS
if __name__ == '__main__':
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        write_data(extracted)
        time.sleep(5)






