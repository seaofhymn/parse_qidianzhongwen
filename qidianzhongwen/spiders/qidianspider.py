# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QidianspiderSpider(CrawlSpider):
    name = 'qidianspider'
    allowed_domains = ['qidian.com']
    start_urls = ['http://www.qidian.com/free/all/']

    rules = (
        Rule(LinkExtractor(allow=r'//book.qidian.com/info/\d+'), callback='parse_item'),
        Rule(LinkExtractor(
            allow=r'//www\.qidian\.com/free/all\?orderId=&vip=hidden&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=1&page=\d+?'),
            follow=True),
        # 翻页
    )

    def parse_item(self, response):
        li_list = response.xpath("//div[@class='volume']//li")

        for li in li_list:
            href = "http:" + li.xpath("./a/@href").extract_first()

            yield scrapy.Request(href, callback=self.parse_zhangjie, )

    def parse_zhangjie(self, response):
        a = []
        item = {}
        item["book_name"] = response.xpath("/html/head/title/text()").extract_first()
        content = response.xpath("//div[@class='read-content j_readContent']/p/text()").extract()
        for i in content:
            a.append(i.strip())
        ii = "".join(a)
        item["book_content"] = ii
        # print(item)
        yield item
