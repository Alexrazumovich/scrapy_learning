import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https:divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # divans=response.css('div._UdOk')
        divans = response.css('div.LlPhw')
        for divan in divans:
            yield{
                'name':divan.css('div.lsooF span::text').get(),
                'price':divan.css('div.pY3d2 span::text').get(),
                'url':divan.css('a').attrib['href']

            }


