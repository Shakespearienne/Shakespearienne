# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.babelio.com/auteur/William-Shakespeare/3174/citations']

    def parse(self, response):
        for title in response.css('div.post_con td div.text.row div'):
            yield {'quotes': title.css('div ::text').extract_first()}

        next_pages = response.css('div.pagination.row > a').extract()
        for index, page in enumerate(next_pages):
            if 'class="active"' in page:
                n_page = next_pages[index + 1]
                next_page = Selector(text=n_page).xpath('//a/@href').extract()
                next_page_url = next_page[0]
                if index == (len(next_pages) - 1):
                    next_page = False

        if next_page:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)