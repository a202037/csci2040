import scrapy
import json

class OpenriceSpider(scrapy.Spider):
	name = 'openrice'
	allowed_domains = ['www.openrice.com']


	def start_requests(self):
		headers = {
			'accept-encoding': 'gzip, deflate, sdch, br',
			'accept-language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'cache-control': 'max-age=0',
		}
		file = open('openrice_urls.txt', 'r')
		# for line in file:
		firstLine = file.readline()
		yield scrapy.Request(url=str(firstLine), headers=headers, callback=self.parse)

	def parse(self, response):
		output_filename = 'openrice_data.json'
		data = {}
		restaurant_info = response.css("script.application/ld+json").extract()  # 1. select the restaurants list
		# restaurant_review = "h2.title-name a::attr(href)"  # 2. select the link of a restaurant
		# restaurant_link = # 3. extract the information
		# actuall_link = "https://www.openrice.com" + str(restaurant_link)[3:-2]
		# with open(output_filename, 'a') as output_file: # you should delete the intermediate file before you run the code
		# 	json.dump(data, output_file)
		print restaurant_info
	# your code here

		