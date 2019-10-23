import scrapy
class TestSpider(scrapy.Spider):
    name = "test"

    start_urls = [
        "https://web.archive.org/web/20150906082429/http://brinkoffreedom.net/outdoor-activities/trapping-for-winter-survival-or-all-around-for-food-fur-and-fun-part-2/",
    ]

    def parse(self, response):
        filename = 'trapping1-3.html'
        with open(filename, 'wb') as f:
            f.write(response.body)