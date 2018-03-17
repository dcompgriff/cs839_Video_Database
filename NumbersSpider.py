import numpy as np
import pandas as pd
import scrapy
from scrapy.shell import inspect_response



'''
Website: https://www.the-numbers.com/movies/letter/A
'''


class TheNumbersSpider(scrapy.Spider):
    name = "movies"
    # Scrape Movies from page 1 through 43.
    # start_urls = ['http://www.imdb.com/list/ls032600534/?st_dt=&mode=detail&sort=list_order,asc' + '&page=' +
                  #str(i) for i in range(1, 44)]
    #start_urls = ['http://www.imdb.com/list/ls032600534/?st_dt=&mode=detail&sort=list_order,asc&page=1']
    #base_url = 'http://www.imdb.com'
    start_urls = ['https://www.the-numbers.com/movies/letter/A']
    headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, headers=self.headers)

    def moviepage_callback(self, response):
        print("yay in callback")
        rows=response.xpath('//div[@id="summary"]/table/tr')
        #print(rows)
        #the problem here is there is no fix format, need to do regex matching to find the mpaa rating etc
        rating_data=rows.xpath('.//td[contains(.,"MPAA")]/ancestor::tr')
        runningtime = rows.xpath('.//td[contains(.,"Running Time")]/parent::tr')
        #print("rating data xpath ", rating_data)
        print("rating data is",rating_data.xpath('td[2]/a/text()').extract())
        #print("runtime xoath", runningtime)
        print("running time", runningtime.xpath('td[2]/text()').extract())
        cast_data = response.xpath('//div[@id="cast-and-crew"]//td[contains(.,"Director")]/parent::tr')
        #print("cast data is" , cast_data)
        print("director ",cast_data.xpath('.//td[1]//span/text()').extract())
        finance_data = response.xpath('//table[@id="movie_finances"]//td[contains(.,"Worldwide")]/parent::tr')
        #print("finance data xpath ", finance_data)
        print("finance data is", finance_data.xpath('.//td[2]/text()').extract())
        try:
            yield {
                    'mpaa': rating_data.xpath('td[2]/a/text()').extract()[0],
                    'runtime': runningtime.xpath('td[2]/text()').extract()[0],
                    'gross':finance_data.xpath('.//td[2]/text()').extract()[0],
                    'director':cast_data.xpath('.//td[1]//span/text()').extract()[0]
                    }
        except:
            pass

    def parse(self, response):
        # Get the movie information from each movie item in the list.
        #print(response.xpath('//table/tr'))
        #row_elements = table.xpath(".//tr")
        #for row in row_elements:
            #first_tr = table.xpath(".//tr")[0]
        #for h3 in response.xpath('//h1').extract():
         #   yield {"title":h3}
          #  print(h3)
        rows=response.xpath('//div[@id="wrap"]/div[@id="main"]/div[@id="page_filling_chart"]/center/table/tr')
        rows = rows[2:]
        for row in rows:
            url=row.xpath('.//td[2]/b/a/@href').extract()
            if not url or len(url)<1:
                continue
            url = 'https://www.the-numbers.com'+url[0]
            print("url is ",url)
            pageresp= yield scrapy.Request(url, self.moviepage_callback, headers=self.headers)
            print("pageresp is", pageresp)
            try:
                yield {
                        'title': row.xpath('td[2]/b/a/text()').extract()[0],
                        'release_date': row.xpath('td[1]/text()').extract()[0],
                        'genres':row.xpath('td[3]/a/text()').extract(),
                        'domestic gross': row.xpath('td[5]/text()').extract()[0],
                        'gross': row.xpath('td[5]/text()').extract()[0],
                        'director':"",
                        'stars':""
                        }
            except:
                continue

        return

        for url in response.xpath('//a/@href').extract():
                                                yield scrapy.Request(url, callback=self.parse)




















