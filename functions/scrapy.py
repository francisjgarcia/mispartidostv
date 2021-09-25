import scrapy
from scrapy.http import FormRequest
from functions.convertDate import convertDate

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
        lista_partidos = response.css('table.tabla-partidos')
        for partido in lista_partidos:
            dia = convertDate(partido.css('tr > td.dia-partido::text').get())
            list = partido.css('tr.event-row')
            for item in list:
                hora = item.css('td.hora::text').get()
                local = item.css('td.local > ul > li > span::text').get()
                visitante = item.css('td.visitante > ul > li > span::text').get()
                competicion = item.css('td.detalles > ul > li.detalles-liga > span::text').get()
                canales = item.css('td.canales > ul > li ::text').getall()
                yield {
                    'dia': dia,
                    'hora': hora,
                    'competicion': competicion,
                    'local': local,
                    'visitante': visitante,
                    'canales': canales
                }
