import scrapy
from scrapy import Request


class EcoalfSpider(scrapy.Spider):
    name = 'ecolaf'

    allowed_domains = ['ecoalf.com', ]

    def __init__(self, country, start_urls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.country = country
        self.start_urls = start_urls

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response):
        categories = response.xpath(
            "//*[has-class('menu-drawer__menu-item')]/@href"
        ).extract()
        for category in set(categories):
            url = response.urljoin(category)
            if url != self.start_urls[0]:
                yield Request(response.urljoin(category),
                              callback=self.parse_category)

    def parse_category(self, response):
        products = response.xpath(
            "//*[has-class('card-product__color')]/@href").extract()
        if products:
            for product in set(products):
                yield Request(response.urljoin(product),
                              callback=self.parse_item
                              )

    def parse_item(self, response):

        loader = {}

        current_url = response.url
        loader["url"] = current_url

        main_title = response.xpath(
            "//*[has-class('product__title')]/text()").extract_first()
        loader["main_title"] = main_title

        current_price = response.xpath(
            "//*[has-class('price-item--sale')]/text()").extract_first()
        prev_price = response.xpath(
            "//*[has-class('price-item--regular')]/text()").extract_first()
        if not current_price:
            current_price = prev_price
        price_tuple = (current_price, prev_price)
        loader["price"] = price_tuple

        description = response.xpath(
            "//*[has-class('product__description')]//text()"
        ).extract()
        description = " ".join(description).strip
        loader["description"] = description

        yield loader


class EcoalfDESpider(EcoalfSpider):
    name = 'ecolaf_de'
    country = 'de'
    start_urls = ['https://ecoalf.com/de', ]

    def __init__(self, *args, **kwargs):
        super(EcoalfDESpider, self).__init__(
            country=self.country,
            start_urls=self.start_urls,
            *args, **kwargs
        )
