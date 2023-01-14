import json
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
        matches = []
        match_list = response.css('table.tablaPrincipal > tbody')
        for match in match_list:
            date = convertDate(match.css('tr.cabeceraTabla > td::text').get())
            list = match.css('tr')
            for item in list:
                hour = item.css('td.hora::text').get()
                local = item.css('td.local > span::text').get()
                visitor = item.css('td.visitante > span::text').get()
                competition = convertCompetition(item.css('td.detalles > ul > li > div.contenedorImgCompeticion > span.ajusteDoslineas > label::text').get())
                channel = convertChannel(item.css('td.canales > ul.listaCanales > li ::text').getall())
                if date is not None and hour is not None and competition is not None and channel is not None:
                    addTask(local, visitor, competition, date, str(hour).strip(), fullPriority(local, visitor, competition), channel, matches)
        if len(matches) > 0:
            print("Se añadieron los siguientes partidos:\n", json.dumps(matches, indent=2, ensure_ascii=False))
        else:
            print("No hay ningún partido que añadir.")