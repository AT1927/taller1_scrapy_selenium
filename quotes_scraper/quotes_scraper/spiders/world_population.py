import scrapy

class WorldPopulationSpider(scrapy.Spider):
    name = "world_population"
    start_urls = ["https://www.worldometers.info/world-population/"]

    def parse(self, response):
        # Selecciona la tabla de países y población
        rows = response.css('table#example2 tbody tr')
        for row in rows:
            yield {
                'country': row.css('td:nth-child(2)::text').get(),
                'population_2023': row.css('td:nth-child(3)::text').get(),
                'yearly_change': row.css('td:nth-child(4)::text').get(),
                'net_change': row.css('td:nth-child(5)::text').get(),
                'density': row.css('td:nth-child(6)::text').get(),
                'land_area': row.css('td:nth-child(7)::text').get(),
                'migrants': row.css('td:nth-child(8)::text').get(),
                'fertility_rate': row.css('td:nth-child(9)::text').get(),
                'median_age': row.css('td:nth-child(10)::text').get(),
                'urban_pop': row.css('td:nth-child(11)::text').get(),
                'world_share': row.css('td:nth-child(12)::text').get(),
            }
