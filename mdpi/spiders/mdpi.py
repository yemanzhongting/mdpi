# -*- coding: UTF-8 -*-
from items import MdpiItem

__author__ = 'zy'
__time__ = '2020/1/11 21:18'
import time
import scrapy
import re
from datetime import datetime
from requests_html import HTMLSession


class ExampleSpider(scrapy.Spider):
    name = 'mdpi'
    allowed_domains = ['mdpi.com']
    start_urls = [
        "http://www.mdpi.com/search?year_from=2016&year_to=2018&page_no=1&page_count=200&sort=relevance&journal=sustainability&view=default"
        ,
        "http://www.mdpi.com/search?year_from=2016&year_to=2018&page_no=2&page_count=200&sort=relevance&journal=sustainability&view=default"
        ,
        "http://www.mdpi.com/search?year_from=2016&year_to=2018&page_no=3&page_count=200&sort=relevance&journal=sustainability&view=default"
    ]

    # for url in start_urls:
    #     scrapy.Request(url=url, callback=self.parse)
    #     yield 1

    def __init__(self):
        self.url = 'http://www.mdpi.com/search?year_from=2016&year_to=2018&page_count=200&sort=relevance&journal=sustainability&article_types=&countries='
        self.urls = [self.url]
        for i in range(2, 4):#44
            a = f'http://www.mdpi.com/search?year_from=2016&year_to=2018&page_no={i}&page_count=200&sort=relevance&journal=sustainability&view=default'
            self.urls.append(a)

    def crawl_parse(url):
        session = HTMLSession()
        r = session.get(url)
        eles = r.html.find('.article-item')
        items = []
        for e in eles:
            title_e = e.find('a.title-link', first=True)
            if not title_e:
                continue

            abstract_e = e.find('div.abstract-full', first=True)
            if not abstract_e:
                continue

            href_e = e.find('a:contains(HTML)', first=True)

            if not href_e:
                href = None
            else:
                re_href = href_e.attrs['href']
                href = f'http://www.mdpi.com{re_href}'

            info = dict(title=title_e.text, abstract=abstract_e.text, href=href)

            try:
                date_e = e.find('div.pubdates', first=True)
                m = re.search(r'Received: (.*?) / Revised: (.*?) / Accepted: (.*?) / Published: (.*)', date_e.text)
                received = datetime.strptime(m.group(1), '%d %B %Y')
                revisied = datetime.strptime(m.group(2), '%d %B %Y')
                accepted = datetime.strptime(m.group(3), '%d %B %Y')
                published = datetime.strptime(m.group(4), '%d %B %Y')

                received = datetime.strftime(received, '%Y-%m-%d')
                revisied = datetime.strftime(revisied, '%Y-%m-%d')
                accepted = datetime.strftime(accepted, '%Y-%m-%d')
                published = datetime.strftime(published, '%Y-%m-%d')
                info.update(date=date_e.text, received=received, revisied=revisied, accepted=accepted,
                            published=published)
            except Exception as e:
                pass

            items.append(info)

        return items

    def parse(self, response):
        for i in self.urls:
            items=ExampleSpider.crawl_parse(i)
            #print(items)
            for j in items:
                item = MdpiItem()
                item['title']=j['title']
                item['abstract'] = j['abstract']
                item['href']=j['href']
                print(item['href'])
                print('##########')
                yield item
            #time.sleep(0.1)

#import pandas as pd
# df = pd.DataFrame(articles)
# df.sample(5) # 此处想想为什么不用head...

#https://www.jianshu.com/p/e8428f8ecea6
#如何控制翻页

#循环换页爬取

# i = 2
# while i<=10:
#     next_url = "http://www.gznw.gov.cn/priceInfo/getPriceInfoByAreaId.jx?areaid=22572&page="+str(i)
#     i = i + 1
#     yield Request(next_url)