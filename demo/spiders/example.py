import scrapy
from scrapy.loader import ItemLoader
from demo.items import Article


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["plagelao.github.io"]
    start_urls = [
            "https://plagelao.github.io/articles/software%20development/search/explanations/2023/11/19/about-search.html",
            "https://plagelao.github.io/articles/software%20development/jekyll/tutorials/2023/11/12/adding-categories-and-tags-to-the-site.html",
            ]

    def parse(self, response):
        item = Article()
        item['title'] = ' '.join(''.join(response.css('h2 *::text').extract()).split())
        item['body'] = ' '.join(''.join(response.css('article *::text').extract()).split())
        item['excerpt'] = ' '.join(''.join(response.css('article p:first-child::text').extract()).split())
        item['tags'] =  response.css('.tag::text').extract()
        item['url'] = response.url
        item['objectID'] = response.url
        return item
