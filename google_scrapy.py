import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = [
        'https://www.google.com/search?q=קורבן קורונה',
        'https://www.google.com/search?q=קורבנות קורונה'
    ]

    def parse(self, response):
        #for title in response.css('h3'):
        for link in response.css('h3').xpath('..'):
            #title = link.css('h3 ::text').get()
            #url = link.attrib['href']
            #yield {'koteret': title, 'url': url}
            yield response.follow(link, self.parse_article)

        #for next_page in response.css('a.next-posts-link'):
        #    yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        is_from_israel = 'ישראל' in ''.join(response.css('::text').getall())
        is_a_corona_article = 'קורונה' in ''.join(response.css('::text').getall())
        yield {
            'is_relvant': is_from_israel and is_a_corona_article,
            'url': response.url
        }
