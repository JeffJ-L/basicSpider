import scrapy


class BillboardSpider(scrapy.Spider):
    name = "ChartList"
    start_urls = ["https://www.billboard.com/charts/hot-100/"]

    def parse(self, response):
        for elementDiv in response.css("div.chart-results-list"):
            titles = elementDiv.css("h3#title-of-a-story.c-title.a-no-trucate::text").getall() #returns a list

            for title in titles:
                if title:
                    yield {
                        "title": title.strip() #getting rid of unnecessary elements/texts
                    }