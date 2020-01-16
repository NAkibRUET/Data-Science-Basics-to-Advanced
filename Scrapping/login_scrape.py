# -*- coding: utf-8 -*-
import scrapy


class LoginScrapeSpider(scrapy.Spider):
    name = 'login_scrape'
    allowed_domains = ['toscrape.com']
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        data ={
            'csrf_token':token,
            'username':'abc',
            'password':'abc'
        }
        yield scrapy.FormRequest(url=self.login_url,formdata=data,callback=self.parse_quotes)
    
    def parse_quotes(self, response):
        cells_list = response.css('div.quote')
        for cell in cells_list:
            yield{
                'author_name': cell.css('small.author::text').extract_first(),
                'author_url': cell.css('small.author ~ a[href *= "goodreads.com"]::attr(href)').extract_first()
            }
            next_url = response.css('li.next > a::attr(href)').extract_first()
            if next_url:
                next_page = response.urljoin(next_url)
                yield scrapy.Request(url=next_page, callback=self.parse_quotes)
