import re
import time

import requests
from bs4 import BeautifulSoup
from lxml import etree

import urllib3

urllib3.disable_warnings()


class GetContent(object):
    def __init__(self, url_book):
        self.url_home = 'https://m.ibiquku.la'
        self.url_book = url_book
        self.xpath_page = '/html/body/div[2]/div[9]/span[2]/select/option'  # 获取有多少章节
        self.xpath_title = '/html/body/div[2]/ul[2]/li/*'  # 获取当前展示章节中的内容链接
        self.xpath_content = '//*[@id="nr"]/text()'  # 获取内容
        self.header = {
            "Host": "m.ibiquku.la",
            "Cookie": "Hm_lvt_f8f5b99aeec11e12bfbb2f9ab781c861=1688448132; wsci=15418; wsii=74c2fa2f4f86df3968b1bf3c8170bca4; wsii.sig=ys75d8RmWRnAFRsXS2w-PpVs4mMpdQ0Ejkq8F591ExA; Hm_lvt_b903b69445834ce30e84fd93a25d5408=1688480241,1688517702; Hm_lpvt_b903b69445834ce30e84fd93a25d5408=1688517702",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

    def get_url(self, url):
        return requests.get(url, verify=False, headers=self.header).content.decode()

    def get_title_page(self):
        url = self.url_home + self.url_book
        page = etree.HTML(self.get_url(url))
        p_xp = page.xpath(self.xpath_page)
        for c in p_xp:
            if c.get('value'):
                self.get_title(self.url_home + c.get('value'))
                # print(self.url_home + c.get('value'))

    def get_title(self, url):
        title = etree.HTML(self.get_url(url))
        p_xp = title.xpath(self.xpath_title)
        for c in p_xp:
            # print(self.url_home + c.get('href'), c.text)
            self.get_content_pag(self.url_home + c.get('href'))

    def get_content_pag(self, url):
        content = etree.HTML(self.get_url(url))
        p_xp = content.xpath(self.xpath_content)
        all_url = self.url_home + self.url_book + '{}_{}.html'
        book_page_id = re.compile(r".*/(\d.*?).html").findall(url)[0]
        page = re.compile(r"\(.*?/(\d)页\)").findall(p_xp[0])[0]
        for n in range(1, int(page) + 1):
            self.get_content_text(all_url.format(book_page_id, n))

    def get_content_text(self, url):
        p_xp = etree.HTML(self.get_url(url)).xpath(self.xpath_content)
        text_ = ''.join(p_xp[1:]) \
            .replace('\n', '') \
            .replace('\xa0', '') \
            .replace('7017k', '') \
            .replace('（本章未完，请点击下一页继续阅读）', '')
        print(text_, end='')

    def run(self):
        self.get_title_page()


if __name__ == '__main__':
    r = GetContent('/95/95111/')
    r.run()
