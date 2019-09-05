#!/usr/bin/env python

######################    requests 库  ######################
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

#res = requests.get("https://www.zhhanker.com",headers = headers)
img = requests.get("https://i5.meizitu.net/thumbs/2019/05/178809_05b03_200.jpg",headers=headers)
print(img.


respons = requests.get("https://i5.meizitu.net/thumbs/2019/05/178809_05b03_200.jpg",headers=headers)
with open('1.jpg','rb') as f:
    f.write(respons.content)
	f.close()
	

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.taobao.com")


import urllib

urllib.request  请求模块
urllib.error    异常处理模块
urllib.parse    url解析模块
urllib.robotparser   robots.txt解析模块


import urllib.request                                                  

response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))           

# requests 库
import requests
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')

# Get 请求
import requests

response = requests.get('http://httpbin.org/get')
print(response.text)

# get请求带参数
import requests
data = {
"age": 18,
"name": "lawrence",
"salary": 20000

}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)

# 解析 json
import requests

response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(type(response.json()))

# 获取二进制数据
import requests

response = requests.get('http://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(response.content)
    f.close()
print(type(response.text),type(response.content))
print(response.text)
print(response.content)

# 添加headers
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
response = requests.get('http://github.com/perfect-lawrence',headers=headers)
print(response.text)


# 基于POST请求
import requests
data = {'name': 'lawrence','age': 21}
response = requests.post('http://httpbin.org/post',data=data)
print(response.text)

# 添加headers
import requests
data = {'name': 'lawrence','age': 21}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
response = requests.post('http://httpbin.org/post',data=data,headers=headers)
print(response.json())

# response属性
import requests
response = requests.get('http://www.jianshu.com')
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),(response.cookies))
print(type(response.url),(response.url))
print(type(response.history),(response.history))

# 状态码判断
import requests
response = requests.get('http://www.jianshu.com')
if not response.status_code == requests.codes.ok: 
    print('Request Successfully')
else:
    print("error")

'''
Requests还附带了一个内置的状态码查询对象
主要有如下内容：

100: ('continue',),
101: ('switching_protocols',),
102: ('processing',),
103: ('checkpoint',),
122: ('uri_too_long', 'request_uri_too_long'),
200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\o/', '✓'),
201: ('created',),
202: ('accepted',),
203: ('non_authoritative_info', 'non_authoritative_information'),
204: ('no_content',),
205: ('reset_content', 'reset'),
206: ('partial_content', 'partial'),
207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
208: ('already_reported',),
226: ('im_used',),

Redirection.

300: ('multiple_choices',),
301: ('moved_permanently', 'moved', '\o-'),
302: ('found',),
303: ('see_other', 'other'),
304: ('not_modified',),
305: ('use_proxy',),
306: ('switch_proxy',),
307: ('temporary_redirect', 'temporary_moved', 'temporary'),
308: ('permanent_redirect',
'resume_incomplete', 'resume',), # These 2 to be removed in 3.0

Client Error.

400: ('bad_request', 'bad'),
401: ('unauthorized',),
402: ('payment_required', 'payment'),
403: ('forbidden',),
404: ('not_found', '-o-'),
405: ('method_not_allowed', 'not_allowed'),
406: ('not_acceptable',),
407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
408: ('request_timeout', 'timeout'),
409: ('conflict',),
410: ('gone',),
411: ('length_required',),
412: ('precondition_failed', 'precondition'),
413: ('request_entity_too_large',),
414: ('request_uri_too_large',),
415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
417: ('expectation_failed',),
418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
421: ('misdirected_request',),
422: ('unprocessable_entity', 'unprocessable'),
423: ('locked',),
424: ('failed_dependency', 'dependency'),
425: ('unordered_collection', 'unordered'),
426: ('upgrade_required', 'upgrade'),
428: ('precondition_required', 'precondition'),
429: ('too_many_requests', 'too_many'),
431: ('header_fields_too_large', 'fields_too_large'),
444: ('no_response', 'none'),
449: ('retry_with', 'retry'),
450: ('blocked_by_windows_parental_controls', 'parental_controls'),
451: ('unavailable_for_legal_reasons', 'legal_reasons'),
499: ('client_closed_request',),

Server Error.
500: ('internal_server_error', 'server_error', '/o\', '✗'),
501: ('not_implemented',),
502: ('bad_gateway',),
503: ('service_unavailable', 'unavailable'),
504: ('gateway_timeout',),
505: ('http_version_not_supported', 'http_version'),
506: ('variant_also_negotiates',),
507: ('insufficient_storage',),
509: ('bandwidth_limit_exceeded', 'bandwidth'),
510: ('not_extended',),
511: ('network_authentication_required', 'network_auth', 'network_authentication'),
'''

# requests 高级操作
import requests
files = {'file': open('/home/lawrence/Desktop/favicon.ico','rb')}
response = requests.post("http://httpbin.org/post',files=files)
print(response.text)

# 获取cookie
import requests
response = requests.get('http://www.baidu.com')
print(response.cookies)
for k,v in response.cookies.items():
    print(k + "=" + v)
	
	
# 会话维持
import requests

requests.get('http://httpbin.org/cookies/set/number/12345678')
response = requests.get('http://httpbin.org/cookies')
print(response.text)

import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/12345678')
response = s.get('http://httpbin.org/cookies')
print(response.text)

# 证书验证

import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)

import requests
from 
response = requests.get('http://www.12306.cn',verify=False)
print(response.status_code)

# 消除警告信息
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('http://www.12306.cn',verify=False)
print(response.status_code)

import requests
response = requests.get('https://www.12306.cn',cert=('/etc/ssl/server.crt','etc/ssl/server.key'))
print(response.status_code)

# 代理设置
import requests
proxies = {
"http": "http://127.0.0.1:9743",
"https": "http://127.0.0.1:9734",
}

response = requests.get("https://www.taobao.com",proxies=proxies)
print(response.status_code)

import requests
proxies = {
"http": "http://user:password@127.0.0.19743/",
}
response = requests.get("https://www.taobao.com",proxies=proxies)
print(response.status_code)

pip3 install 'requests[socks]'

import requests
proxies = {
"http": "socks5://127.0.0.1:9724",
"http": "socks5://127.0.0.1:9742",
}

response = requests.get("https://www.taobao.com",proxies=proxies)
print(response.status_code)

# 超时设置
import requests
from requests.exceptions import ReadTimeout
try:
    response = requests.get("https://www.taobao.com",timeout = 1)
    print(response.status_code)
except ReadTimeout:
    print("Timeout")

# 认证设置
import requests
from requests.auth import HTTPBasicAuth

r = requests.get("http://120.27.34.24:9001",auth=HTTPBasicAuth('user','123'))
print(r.status_code)

import requests

r = requests.get("http://120.27.34.24:9001",auth=('user','123'))
print(r.status_code)


# 异常处理
import requests

from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response = requests.get('http://httpbin.org/get',timeout=0.5)
	print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')
######################################   selenium 库      ###########################
	
# selenium 库 主要用自动化测试工具，支持多种浏览器
# 爬虫中主要用JavaScript渲染的html页面
# 基本使用
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('http://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until((EC.presence_of_element_located((By.ID,'content_left'))))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
	
### 声明浏览器对象
from selenium import webdriver

browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()

# 访问页面
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

## 查找元素
# 单元素
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)
browser.close()
"""
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

"""

# 单元素
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID,'q')
print(input_first)
browser.close()

# 多个元素
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
list = browser.find_elements _by_css_selector('.service-bd li')
print(list)
browser.close()

# 多个元素
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
list = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(list)
browser.close()
"""
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

"""

#元素交互操作
## 对获取的元素调用交互方法

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(2)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
# 更多操作：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.webelement
# 交互动作
## 将动作附加岛动作链链中串执行
from selenium import webdriver
from selenium.webdriver imoprt ActionChains
browser = webdriver.Chrome()
url = 'http://www.ruoobb.com/try/try.php?
browser.get('https://www.taobao.com')



