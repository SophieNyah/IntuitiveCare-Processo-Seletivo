# Back-End
Foi utilizada a biblioteca Flask para criação dessa API devido à sua simplicidade.

As requisições são feitas para as rotas `/razao/` ou `/nome/`, dependendo se a pesquisa é por Razão Social ou Nome Fantasia.

O nome passado na requisição é procurado na respectiva coluna do dataframe, buscando nomes similares com a biblioteca `difflib`.

Caso seja encontrado, é retornada na resposta uma lista com até 5 operadoras com nomes similares. Caso contrário, é retornado um erro 404.

## Notas de Implementação
Ao iniciar o servidor, o arquivo csv é lido e inserido em um DataFrame, armazenado em memória por toda a duração do servidor.

Esse DataFrame fica armazenado em um singleton, instanciado ao iniciar-se o servidor, e fica disponível para ser lido por cada requisição.

Já que o servidor só faz leitura dos dados da tabela, e não os altera de maneira alguma, julgou-se que um objeto global seria o suficiente,
uma vez que, pela natureza de apenas leitura, não é necessário preocupação com concorrência de threads.

Outro aspecto pelo qual foi escolhida essa abordagem, ao invés de uma mais complexa, como um banco de dados, foi justamente
a simplicidade de implementação, e o pequeno escopo do problema. Como dito acima, não há preocupações com concorrência,
e também o arquivo csv é pequeno o suficiente para que pudesse ser mantido em memória sem problemas.


# Dependências Utilizadas e suas Versões
Nota: não é necessário rodar o servidor, as dependências estão aqui por razões de documentação apenas.
* Python `3.8`
* Flask `2.2.2`
* Flask-Cors `3.0.10`
* numpy `1.23.3`
* pandas `1.5.1`
