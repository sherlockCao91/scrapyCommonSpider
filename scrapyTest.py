import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']
    rst = 'test.txt'

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            with open(self.rst,"w") as f:
                target = {'title': title.css('a ::text').extract_first()}
                print target
                f.write("%s"%(target))
        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

# if __name__ == 'main':
    # test = BlogSpider()
    # test.parse()