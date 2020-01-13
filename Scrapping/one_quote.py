# -*- coding: utf-8 -*-
import scrapy


class OneQuoteSpider(scrapy.Spider):
    name = 'one_quote'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        return{
            'author_name': response.css('small.author::text').extract_first(),
            'text':response.css('span.text::text').extract_first(),
            'tags':response.css('a.tag::text').extract()
        }
