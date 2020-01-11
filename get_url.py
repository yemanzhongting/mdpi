# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/11 13:51'

import re
#1. 确定好要爬取的入口链接
url = "http://blog.csdn.net"
# 2.根据需求构建好链接提取的正则表达式
pattern1 = '(https://mp.weixin.qq.com/cgi-bin)(.*?)"'

pat="""
<div><div style="text-align:center; padding-top:3em;"><img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQH17zwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyeVd2cm9JX3VkOUUxOGFMcWh1MUkAAgSKXRleAwSAUQEA" style="height:13em;"</div><div style="text-align:center; padding-top:0.3em; font-size:1em; letter-spacing:2px;">请微信扫码登录后使用</div>		<div style="text-align:center; padding-top:0.63em; font-size:0.75em; letter-spacing:2px; color:#888686; ">如不显示二维码查看上方故障解决</div></div>
"""


content_href = re.findall(pattern1, pat)[0]

print(content_href[0]+content_href[1])