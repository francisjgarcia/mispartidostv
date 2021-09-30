import scrapy
from scrapy.http import FormRequest
from functions.convertDate import convertDate
from functions.convertCompetition import convertCompetition
from functions.convertChannel import convertChannel
from functions.matchPriority import fullPriority
from functions.todo import addTask

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
                channel = convertChannel(item.css('td.canales > ul > li ::text').getall())
                if date is not None and hour is not None and competition is not None and channel is not None:
                    addTask(local, visitor, competition, date, hour, fullPriority(local, visitor, competition), channel)
