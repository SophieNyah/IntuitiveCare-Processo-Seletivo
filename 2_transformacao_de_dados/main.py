import os
import zipfile

import converter
from pandas import DataFrame


def main():
    # Lê o pdf como um único DataFrame
    table: DataFrame = converter.read_pdf('Anexo I - Lista completa de procedimentos.pdf')

    # Converte esse DataFrame para um arquivo csv
    csv_file_name: str = converter.convert_to_csv(table)

    # Comprimi esse arquivo e o deleta
    zip_file = zipfile.ZipFile('Teste_Sophie_Nascimento.zip', mode='w')
    zip_file.write(csv_file_name, compress_type=zipfile.ZIP_DEFLATED)
    os.remove(csv_file_name)


if __name__ == '__main__':
    main()
