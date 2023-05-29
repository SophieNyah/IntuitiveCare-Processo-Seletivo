from typing import Optional
from pandas import read_csv, DataFrame
import difflib


# Classe singleton, para que seja possível acessar o DataFrame
#   de qualquer requisição, uma vez que ele tenha sido criado
class Operadoras:
    _operadoras_table: Optional[DataFrame] = None

    # Como o singleton têm um parâmetro, e também por ter um ponto
    #   fixo de inicialização (ao iniciar o servidor), julgou-se melhor criar uma
    #   função separada para sua instanciação
    @classmethod
    def set_singleton(cls, csv_path: str):
        if cls._operadoras_table is None:
            cls._operadoras_table = \
                read_csv(csv_path, sep=';', skiprows=2, encoding='ISO-8859-1', keep_default_na=False)
        else:
            raise AssertionError("`set_singleton` called on already instantiated singleton")

    # Retorna uma instância do singleton, gerando uma exception caso não tenha sido inicializado
    @classmethod
    def instance(cls) -> DataFrame:
        if cls._operadoras_table is None:
            raise AssertionError("`instance` called on non instantiated singleton")
        return cls._operadoras_table

    # Método para encontrar as operadoras cujo nome mais se assemelha ao nome passado
    @staticmethod
    def find_closest(name: str, field: str):
        name = name.upper()
        operadoras: DataFrame = Operadoras.instance()
        names_to_search: [str] = operadoras[field]

        found_names = difflib.get_close_matches(name, names_to_search, n=5, cutoff=0.6)
        if len(found_names) == 0:
            raise LookupError(f"Name `{name}` not found on attribute `{field}`")

        rows = []
        for name in found_names:
            row = operadoras.loc[operadoras[field] == name].to_dict()
            rows.append(row)

        return rows
