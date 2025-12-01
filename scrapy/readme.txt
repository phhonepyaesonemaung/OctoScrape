1.to start the project
scrapy startproject projectname


2.open the shell
scrapy shell


3.fetch the content
fetch('url')


fetch response are store in response

xpath or css selector to get information form the page

css selector 
response.css('article.product_pod').get()  -> find the product container

store it in variable 
products=response.css('article.product_pod')

and we can see how many product are in the page
len(products)

products.css('h3 a::text').get() -> it will get the product name 
products.css('h3 a::text').getall() -> it will get all the product in page


products.css('div.product_price p.price_color::text').get() -> this will get the product price

products.css('div.product_price p.price_color::text').get().replace('£','') -> replace the pwn sighn with nothing

products.css('h3 a::text').attrib['href'] -> can also write like this for storing the link




three step 
1.extract  -> request 
2.transform -> pass
3.load  -> output



this is run the crawler
scrapy crawl spidy

scrapy crawl spidy -O book.json  -> it will save in the json


response.urljoin(response.css('li.next a::attr(href)').get()) -> ths will get the link of next page