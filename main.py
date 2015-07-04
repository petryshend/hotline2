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


def get_price_range_as_int(price):
    """
    Convert price range string to ints
    :param price:
    :return: mix and max price in array
    """
    splitted = price.split(u'\u2013')
    result = []
    for i, el in enumerate(splitted):
        num_string = []
        for ch in el:
            if ch.isdigit():
                num_string.append(ch)
        result.append(int(''.join(num_string)))

    return result

if __name__ == '__main__':
    for url in URLS:
        price_string = get_price_string(url)
        print get_price_range_as_int(price_string)