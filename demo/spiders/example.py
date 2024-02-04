import scrapy
from scrapy.loader import ItemLoader
from demo.items import Article


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["plagelao.github.io"]
    start_urls = [
            "https://plagelao.github.io/articles/",
            ]

    def parse(self, response):
        for article_url in response.xpath('//h3/a/@href'):
            url = response.urljoin(article_url.extract())
            yield scrapy.Request(url, callback = self.parse_article)

    def parse_article(self, response):
        item = Article()
        item['title'] = ' '.join(''.join(response.css('h2 *::text').extract()).split())
        item['body'] = ' '.join(''.join(response.css('article *::text').extract()).split())
        item['excerpt'] = ' '.join(''.join(response.css('article p:first-child::text').extract()).split())
        item['tags'] =  response.css('.tag::text').extract()
        item['url'] = response.url
        item['objectID'] = response.url
        yield item

