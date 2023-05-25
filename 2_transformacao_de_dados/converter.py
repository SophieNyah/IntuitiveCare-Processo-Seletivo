import tabula
from pandas import DataFrame
from csv import QUOTE_ALL


###
#  Para ler o pdf especificado da melhor maneira possível, várias configurações foram necessárias,
#    portanto julgou-se melhor criar uma função própria para essa operação.
#  É realiazada a leitura do pdf apenas nas páginas onde a tabela está presente,
#    e também apenas na área específica da tabela.
#  Retorna-se o DataFrame obtido nessa leitura.
###
def read_pdf(pdf_path: str) -> DataFrame:
    PDF_UNIT_FACTOR = 72
    # Área não inclui o header da tabela
    read_area = [
        1.30  * PDF_UNIT_FACTOR,
        0.60  * PDF_UNIT_FACTOR,
        7.70  * PDF_UNIT_FACTOR,
        13.38 * PDF_UNIT_FACTOR,
    ]
    tables_list: [DataFrame] = tabula.read_pdf(
        pdf_path,
        pages='3-180',
        multiple_tables=False,
        lattice=True,
        area=[read_area],
        output_format='dataframe',
        pandas_options={
            'names': [
                'PROCEDIMENTO',
                'RN (alteração)',
                'VIGÊNCIA',
                'Seg. Odontológica',
                'Seg. Ambulatorial',
                'HCO',
                'HSO',
                'REF',
                'PAC',
                'DUT',
                'SUBGRUPO',
                'GRUPO',
                'CAPÍTULO'
            ]
        }
    )

    return tables_list[0]


###
#  Converte o DataFrame passado para csv,
#    substituindo as legendas especificadas.
#  Reetorna o nome do csv salvo.
###
def convert_to_csv(table: DataFrame) -> str:
    replace_subtitles = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }

    table.replace(to_replace=replace_subtitles, inplace=True)

    # Seria possível utilizar o parâmetro 'compress', para que a função .to_csv comprimisse automaticamente,
    #   mas na versão atual da biblioteca, há um bug onde a extensão correta não é gerada,
    #   portanto achei melhor criar o arquivo e comprimí-lo de maneira separada.
    csv_name = 'Lista Completa de Procedimentos.csv'
    table.to_csv(csv_name, index=False, header=True, mode='w', encoding='UTF8', quoting=QUOTE_ALL)

    return csv_name
