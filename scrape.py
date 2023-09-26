from sys import argv
import bs4 as bs
import requests
import re


def scrape_meta_div(url):
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, 'html.parser')

    div = soup.find('div', class_='meta')

    text = div.text.split()
    hours = int(text[0])
    minutes = int(text[2])

    days = (hours + minutes / 60) * 0.5

    return hours, minutes, days


def log(text, mode='a'):
    with open('output.log', mode) as f:
        f.write(text)


def get_urls_from_file(file):
    urls = []
    with open(file) as f:
        for line in f:
            urls.append(line.strip())
    return urls


def log_scrape_meta_div(url):
    d = .0
    try:
        url = re.search(r'(https://[\w./-]+/)', url)[1]
        h, m, d = scrape_meta_div(url)
        log(f"{url} {h}:{m} == {d:.1f} days\n")
    except:
        print('Error: Invalid URL or file path')
    return d


def run(args):
    log('', 'w')

    total_days = .0
    for arg in args:
        print(f"Scraping {arg}...")
        if arg.startswith('http'):
            total_days += log_scrape_meta_div(arg)
        elif arg.endswith('.txt'):
            for url in get_urls_from_file(arg):
                print(f"Scraping {url}...")
                total_days += log_scrape_meta_div(url)

    log(f"Total days: {total_days:.1f}\n")


if __name__ == '__main__':
    if len(argv) > 1:
        run(argv[1:])
    else:
        print('Usage: python scrape.py <http://url|file.txt>')
