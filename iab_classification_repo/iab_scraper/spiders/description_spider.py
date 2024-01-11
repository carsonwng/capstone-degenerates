import scrapy, json
from iab_scraper.items import IabScraperItem

class DescriptionSpider(scrapy.Spider):
    name = "description"

    def start_requests(self):
        path = "./data/generic_urls_to_scrape.txt"

        with open(path, "r") as file:
            for line in file:
                try:
                    url = str(line.rstrip()).split(',')[1]

                    if not url.startswith("http"):
                        url = "http://" + url
                    
                # self.log("!!!!!! NEW URL", str(line.rstrip()))
                    yield scrapy.Request(url=url, callback=self.parse)
                except Exception as e:
                    print(f"Error with {line}: {e}")

    def parse(self, response):
        try:
            item = IabScraperItem()

            item["graph"] = json.loads(response.xpath("//script[@type='application/ld+json']//text()").extract_first())
            return item
        
        except:
            pass