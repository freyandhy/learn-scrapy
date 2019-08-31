# -*- coding: utf-8 -*-
import scrapy


class HeylocalApparelSpider(scrapy.Spider):
    name = 'heylocal_apparel'
    allowed_domains = ['heylocal.id']
    start_urls = ['https://heylocal.id/page/kategori/13']

    def parse(self, response):
        data = []

        # Extract data
        product_name = response.xpath('//h3[@class="product-name"]/a/text()').extract()
        product_price = response.xpath('//span[@class="new-price"]/text()').extract()

        row_data = zip(product_name, product_price)

        for item in row_data:
            data.append({
                'product_name': item[0],
                'product_price': item[1].strip()
            })

        return data
