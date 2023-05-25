# Teste 2: Transformação de Dados

A partir do arquivo `Anexo I - Lista completa de procedimentos`, do exercício anterior, lê-se todos os dados das tabelas nele presente, e gera um arquivo `.csv` _zippado_ com eles;

* Com a biblioteca `tabula-py` e vários parâmetros para melhor leitura, os dados são extraídos para um DataFrame da biblioteca `pandas`
* É realizada a substiuição dos valores de legenda especificados no exercício
* A partir de uma função nativa de DataFrames, ele é convertido em um arquivo `csv`
* Com a biblioteca `zipfile` ele é comprimido, e o arquivo csv original é deletado

# Dependências Utilizadas e suas Versões
* Python `3.8.10`
* pandas `2.0.1`
* tabula-py `2.7.0`
