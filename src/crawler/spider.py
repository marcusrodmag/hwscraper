import scrapy
from dataclass.Lojas import Kabum
class KabumSpider(scrapy.Spider):
    name = 'Hardware Scraper'
    start_urls = []

    custom_settings = {
        'LOG_ENABLED': 'True',
        'LOG_LEVEL': 'WARNING',
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    }

    def parse(self, response):
        precos = []
        loja = Kabum()

        for path in loja.paths:
            precos.append(response.selector.xpath(path).get())
        
        menor_preco = None;
        for preco in precos:
            if preco is not None:
                if menor_preco is None:
                    menor_preco = preco
                if preco < menor_preco:
                    menor_preco = preco
        print("Preço: " + menor_preco)