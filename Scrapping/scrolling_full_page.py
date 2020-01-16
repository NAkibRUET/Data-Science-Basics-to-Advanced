# -*- coding: utf-8 -*-
import json
import scrapy


class ScrollingFullPageSpider(scrapy.Spider):
    name = 'scrolling_full_page'
    api_url = "http://quotes.toscrape.com/api/quotes?page={}"
    allowed_domains = ['toscrape.com']
    start_urls = [api_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield{
                'author_name': quote['author']['name'],
                'text':quote['text'],
                'tags':quote['tags']
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)



