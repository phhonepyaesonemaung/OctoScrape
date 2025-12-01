import scrapy
class bookSpider(scrapy.Spider):
    name = 'spidy'
    start_urls =['http://books.toscrape.com/catalogue/category/books/mystery_3/index.html']

    def parse(self, response):
        for products in response.css('article.product_pod'):
            try:
                yield{
                    'name': products.css('h3 a::text').get(),
                    'price': products.css('div.product_price p.price_color::text').get().replace('£',''),
                    'link':response.urljoin(products.css('h3 a::attr(href)').get())
                        
                    }
            except:

                 yield{
                    'name': products.css('h3 a::text').get(),
                    'price': 'sold out',
                    'link':response.urljoin(products.css('h3 a::attr(href)').get())
                        
                    }
            next_page = response.urljoin(response.css('li.next a::attr(href)').get())
            if next_page is not None:
                yield response.follow(next_page, callback= self.parse)  # if there is next page it will go back and parse it
