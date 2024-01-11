# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class IabScraperPipeline():    
    def open_spider(self, spider):
        self.file = open("./data/generic_desc_urls.txt", "w", encoding="utf-8")
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # print(item["graph"])
        try:
            for schema_type in item["graph"]["@graph"]:
                    
                if schema_type["@type"] != "WebSite":
                    continue

            # print("#######", self.file)
                self.file.write(schema_type["description"] + "\n")
                self.file.flush()
            # self.file.flush()

            return item
        except:
            return item