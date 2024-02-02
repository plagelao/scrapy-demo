# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from typing import Optional
from algoliasearch.search_client import SearchClient  # type: ignore[import]
from demo.items import Article

CONFIG_PREFIX = "ALGOLIA_"
CONFIG_INDEX = f"{CONFIG_PREFIX}INDEX"
CONFIG_WRITE_API_KEY = f"{CONFIG_PREFIX}WRITE_API_KEY"
CONFIG_APPLICATION_ID = f"{CONFIG_PREFIX}APPLICATION_ID"

LOGGER = logging.getLogger(__name__)

class DemoPipeline:
    def __init__(
        self,
        application_id: Optional[str],
        write_api_key: Optional[str],
        index: Optional[str],
    ):
        if None in {application_id, write_api_key, index}:
            LOGGER.info("DemoPipeline is disabled")
            self._enabled = False
        else:
            self._enabled = True
            LOGGER.info("DemoPipeline is enabled")
            self._client = SearchClient.create(application_id, write_api_key)
            self._index = self._client.init_index(index)

    @classmethod
    def from_crawler(cls, crawler) -> "DemoPipeline":
        """
        Initialised by crawler and used to initialise this class with the appropriate config

        :param crawler:
        :return:
        """
        return cls(
            application_id=crawler.settings.get(CONFIG_APPLICATION_ID),
            write_api_key=crawler.settings.get(CONFIG_WRITE_API_KEY),
            index=crawler.settings.get(CONFIG_INDEX),
        )

    def process_item(self, item, spider):
        if self._enabled:
            self._index.save_object(dict(item))
            spider.logger.info("Received response from Algolia")
        return item
