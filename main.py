import bs4
import requests

URLS = [
    'http://hotline.ua/computer-noutbuki-netbuki/dell-inspiron-13-7348/'
]


def get_price_string(url):
    """
    Extract price range from hotline product url and return
    it as string
    :return: string
    """
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    price_all = soup.find_all('span', {'class': 'prc'})[0]
    price_range = price_all.find_all('a', {'class': 'g_statistic'})[0]
    return price_range.get_text()


if __name__ == '__main__':
    for url in URLS:
        print get_price_string(url)