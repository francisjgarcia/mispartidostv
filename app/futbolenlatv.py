import scrapy
from scrapy.http import FormRequest
from functions.todo import addItem
from functions.convertDate import convertDate
from functions.convertCompetition import convertCompetition 

class ScrapySite(scrapy.Spider):
    name = "FutbolEnLaTV"
    start_urls = [ "https://www.futbolenlatv.es" ]

    def parse(self, response):
        yield FormRequest.from_response(response,
                                        formdata={
                                            'opSearch': '1'
                                            },
                                        callback=self.after_form)

    def after_form(self, response):
        match_list = response.css('table.tabla-partidos')
        for match in match_list:
            date = convertDate(match.css('tr > td.dia-partido::text').get())
            list = match.css('tr.event-row')
            for item in list:
                hour = item.css('td.hora::text').get()
                local = item.css('td.local > ul > li > span::text').get()
                visitor = item.css('td.visitante > ul > li > span::text').get()
                competition = convertCompetition(item.css('td.detalles > ul > li.detalles-liga > span::text').get())
                channel = item.css('td.canales > ul > li ::text').getall()
                yield {
                    'date': date,
                    'hour': hour,
                    'competition': competition,
                    'local': local,
                    'visitor': visitor,
                    'channel': channel[0]
                }
                addItem(local, visitor, competition, date, hour, 4, channel[0])
                break