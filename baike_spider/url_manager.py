# coding=utf-8

# url管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set() # 放置待爬取的url
        self.old_urls = set() # 放置已爬取的url

    # 添加新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 添加从网页中获取的新的待爬取url集合
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 返回是否还有待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个新的待爬取url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

