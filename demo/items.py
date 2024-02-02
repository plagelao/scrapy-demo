# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    excerpt = scrapy.Field()
    body = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    objectID = scrapy.Field(regex=r"^https?://[^\?#]+$")
