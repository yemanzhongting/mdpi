# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/11 21:17'
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'mdpi'])  # 你需要将此处的spider_name替换为你自己的爬虫名称