# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/13 17:27'
import requests, json, sys
def login(Phone, PassWord):
    url = "https://wechatx.34580.com/sz/Sign/SignInV2"
    payload = {
    'SourceType': 9,
    'Phone': Phone,
    'PassWord': PassWord
    }
    # 测试下来发现，连 header 都不需要
    response = requests.post(url, data=json.dumps(payload))
    data = json.loads(response.text)
    is_error = data['Error']
    # 登录失败直接退出
    if is_error:
        print('登录失败：{}'.format(data['Message']))
        sys.exit(1)
    else:
        print('登陆成功')
    return (data['Data']['CustomerGuid'], data['Data']['AccessToken'])
def signin(customerguid, accesstoken):
     url = "https://wechatx.34580.com/sz/SignUp/CustomerSignUp"
     querystring = {"accesstoken": accesstoken,
     "customerguid": customerguid, "sourcetype": "9"}
     # 这次不需要 body 中的传入数据
     response = requests.post(url, params=querystring)
     data = json.loads(response.text)
     is_error = data['Error']
     if is_error:
        print(data['Message'])
     else:
        print("签到成功，获取到 {} 个积分".format(data['Data']['GetPoints']))
if __name__ == "__main__":
 # Phone = input('请输入账号：')
 # PassWord = input('请输入密码：')
 # customerguid, accesstoken = login(Phone.strip(), PassWord.strip())
 # signin(customerguid, accesstoken)
 url='https://booking.bestwehotel.com/proxy/trip-goods/hotel/v2/roomRateList'
 cookie='wehotel_sso_token=arvPKljiUbU7NW+/PizkjOXo23izGFjBe7mh2r48yyBtMEvRuC3Po6rZeo3/Dheg; Hm_lvt_cd714ecf74a90a1b343a7df3a11d9b06=1578906357; BTH_MEMBER_WAP=lnJQ1q8oRJQKW/zjwHjeHPe286JvpQTDy6LIjIQEwlslOOn0op3r17BBlC07I9HB; mid=223836881; WX_OPENID=oDMTPjiCBXaQ9zPtb29SX86kG32g; WX_UNIONID=oVod1tykOIig03qmKQn571ZUxB2A; Hm_lpvt_cd714ecf74a90a1b343a7df3a11d9b06=1578906427'
 referer='https://booking.bestwehotel.com/wehotelapp/hotel/index.html?showWETitle=false'
 token='lnJQ1q8oRJQKW/zjwHjeHPe286JvpQTDy6LIjIQEwlslOOn0op3r17BBlC07I9HB'
 payload={"innId":"1000203","brandId":"137","beginDate":"2020-01-13","endDate":"2020-01-14","days":1,"country":"0","timeZone":"GMT+8","cityCode":"AR02960","dayUse":0,"primeFree":False,"assetReload":False,"channelCode":"CA00007","languageCode":0,"clientInfo":None}

 heads = {}
 heads['User-Agent'] = 'Mozilla/5.0 ' \
                       '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                       '(KHTML, like Gecko) Version/5.1 Safari/534.50'
 #heads['url']=url
 heads['Cookie']=cookie
 heads['Referer']=referer
 heads['token']=token
 from requests.packages.urllib3.exceptions import InsecureRequestWarning

 requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

 response = requests.request(method='post',url=url, data=json.dumps(payload),headers= heads,verify=False)

print(response.text)
