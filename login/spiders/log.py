# -*- coding: utf-8 -*-
from scrapy.http import Request, FormRequest
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector


class LogSpider(CrawlSpider):
    name = "log"
    allowed_domains = ["needlogin.cn"]
    start_urls = [
        'https://zabbix.needlogin.cn/index.php'
    ]
    def start_requests(self):
	for url in self.start_urls:
		yield FormRequest(url,meta={'cookiejar':1},formdata={'name':'admin','password':'admin','enter':'Sign+in','request':' ','autologin':'1'},callback = self.login)

    def _log_page(self,response,filename):
	with open(filename,'w') as f:
		try:
			f.write("%s\n%s\n%s\n" % (response.url, response.headers, response.body))
		except:
			f.write("%s\n%s\n" % (response.url, response.headers))
    def login(self, response):
	self._log_page(response,'index_login.html')
	#return [FormRequest.from_response(response,formdata={'name':'admin','password':'admin','enter':'Sign in','request':' ','autologin':'1'}, meta = {'cookiejar':response.meta['cookiejar']},callback = self.parse_item)]	
