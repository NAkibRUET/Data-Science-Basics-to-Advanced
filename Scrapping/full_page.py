# -*- coding: utf-8 -*-
import scrapy


class FullPageSpider(scrapy.Spider):
    name = 'full_page'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        cells_list = response.css('div.quote')
        for cell in cells_list:
            yield{
                'author_name': cell.css('small.author::text').extract_first(),
                'text':cell.css('span.text::text').extract_first(),
                'tags':cell.css('a.tag::text').extract()
            }
