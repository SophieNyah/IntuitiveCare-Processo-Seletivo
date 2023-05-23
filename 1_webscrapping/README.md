# Teste 1: WebScraping

Realiza WebScraping na página https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude para pegar vários arquivos e compactá-los em um único arquivo.

* Com a biblioteca `requests`, é lido o html da página
* Com a biblioteca `BeautifulSoup4` busca-se nesse html a url e nome dos arquivos desejados
* Para cada url, é criado um arquivo, e nele é inserido o conteúdo obtido dessa url
* Utilizando a biblioteca `zipfile`, todos esses arquivos são compactados
* Excluí os arquivos baixados, sobrando apenas o .zip

# Dependências Utilizadas e suas Versões
* Python `3.8.10`
* beautifulsoup4 `4.12.2`
* requests `2.31.0`