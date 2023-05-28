from typing import Optional
from pandas import read_csv, DataFrame
import difflib


class Operadoras:
    _operadoras_table: Optional[DataFrame] = None

    @classmethod
    def set_singleton(cls, csv_path: str):
        if cls._operadoras_table is None:
            cls._operadoras_table = \
                read_csv(csv_path, sep=';', skiprows=2, encoding='ISO-8859-1', keep_default_na=False)
        else:
            raise AssertionError("`set_singleton` called on already instantiated singleton")

    @classmethod
    def instance(cls) -> DataFrame:
        if cls._operadoras_table is None:
            raise AssertionError("`instance` called on non instantiated singleton")
        return cls._operadoras_table

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
