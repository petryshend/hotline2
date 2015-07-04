import bs4
import requests
import datetime

class HotlineCrawler:

    def __init__(self, hotline_urls):
        self.hotline_urls = hotline_urls
        self.min_price = 0
        self.max_price = 0
        self.crawled_date = ''
        self.page_html = ''

    def get_price_string(self, url):
        """
        Extract price range from hotline product url and return
        it as string
        :return: string
        """
        self.page_html = requests.get(url)
        soup = bs4.BeautifulSoup(self.page_html.text, 'html.parser')
        price_all = soup.find_all('span', {'class': 'prc'})[0]
        price_range = price_all.find_all('a', {'class': 'g_statistic'})[0]

        return price_range.get_text()


    def get_price_range_as_int(self, price):
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


    def crawl(self):
        for url in self.hotline_urls:
            self.min_price, self.max_price = self.get_price_range_as_int(self.get_price_string(url))
            self.crawled_date = datetime.datetime.now()