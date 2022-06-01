from itemloaders.processors import  TakeFirst, MapCompose
import scrapy

def strip_spaces(x):
    return x.strip()

class GetCorrItem(scrapy.Item):
    UF = scrapy.Field(output_processor=TakeFirst())
    Cidade = scrapy.Field(output_processor=TakeFirst())
    Faixa_de_CEP = scrapy.Field(input_processor=MapCompose(strip_spaces) ,
                       output_processor=TakeFirst())
    ID = scrapy.Field(output_processor=TakeFirst())



