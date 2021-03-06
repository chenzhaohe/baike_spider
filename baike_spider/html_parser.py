# coding=utf-8

# 网页解析器
import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):

    # 获取页面其它词条的url
    def _get_new_urls(self,page_url, soup):
        new_urls = set()
        # /item/%E7%88%B1%E5%A5%BD%E8%80%85
        links = soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url) # 将new_url按照page_url的格式拼接成一个全新的url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class ="lemmaWgt-lemmaTitle-title" >< h1 > Python < / h1 >
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class ="lemma-summary" label-module="lemmaSummary" >
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

