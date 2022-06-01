import pytest 
from get_corr.spiders import corrs


class TestCorrs:

  @pytest.mark.parametrize('expected', 
                          ['<POST https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm>']
  )

  def test_con(self, expected): 
    responses = []
    url = 'https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
    spider = corrs.CorrsSpider()
    spider_response = spider.start_requests()
    for item in spider_response:
      responses.append(item) 
      
    assert str(responses[0]) == expected   
                        
