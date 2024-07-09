import requests
import selectorlib
from time import gmtime, strftime

URL = 'https://programmer100.pythonanywhere.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """ Scrape the page source from the url """
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def write_data(temperature):
    """ Append temperature and datetime to text file """
    time = strftime('%y-%m-%d-%H-%M-%S', gmtime())

    with open('data.txt', 'a') as f:
        data = f.write(time + ',' + temperature + '\n')


if __name__ == '__main__':
    scraped = scrape(URL)
    extracted = extract(scraped)
    write_data(extracted)






