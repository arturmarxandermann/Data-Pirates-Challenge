import scrapy
from ..items import GetCorrItem
from scrapy.loader import ItemLoader
from uuid import uuid4


class CorrsSpider(scrapy.Spider):
    name = 'corrs'
    url = 'https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
    init = '1'
    end = '50'
    counter = 0
    uf_array = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
                'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

    # if the next button doesn't exist we modify counter ...
    search_form =  {
                'UF': uf_array[counter],
                'pagini': init,
                'pagfim': end
        }

    def start_requests(self):
        yield scrapy.FormRequest(url=self.url, method="POST",
                           formdata=self.search_form, callback=self.parse)

    def parse(self, response):
        cities = response.xpath('//table[last()]//td[1]/text()').getall()
        ceps = response.xpath('//table[last()]//td[2]/text()').getall()
        next = response.xpath('//*[@name="Proxima"]/../a/@href').get()

        for count, city in enumerate(cities):
            il = ItemLoader(item=GetCorrItem())
            il.add_value('UF', self.uf_array[self.counter])
            il.add_value('Cidade', city)
            il.add_value('Faixa_de_CEP', ceps[count])
            il.add_value('ID', str(uuid4()))
            yield il.load_item()

        #IF NEXT BUTTON EXISTS
        if bool(next):
            self.search_form['pagini'] = str(float(self.search_form['pagini']) + 50)
            self.search_form['pagfim'] = str(float(self.search_form['pagfim']) + 50)
        #IF NEXT BUTTON DOESN'T EXISTS
        else:
            self.search_form['pagini'] = self.init
            self.search_form['pagfim'] = self.end
            self.counter += 1
            try:
                self.search_form['UF'] = self.uf_array[self.counter]
            except:
                print("DATA COLLECTION COMPLETED SUCCESSFULLY.")

        yield scrapy.FormRequest(url=self.url, method="POST",
                                 formdata=self.search_form, callback=self.parse)


