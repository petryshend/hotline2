from HotlineCrawler import HotlineCrawler

HOTLINE_URLS = [
    'http://hotline.ua/computer-noutbuki-netbuki/dell-inspiron-13-7348/',
]


if __name__ == '__main__':
    hotline_crawler = HotlineCrawler(HOTLINE_URLS)
    hotline_crawler.crawl()