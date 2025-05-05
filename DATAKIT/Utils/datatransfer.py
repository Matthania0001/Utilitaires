from typing import Optional, List
import pandas as pd
import pyreadstat
import numpy as np

class Import:
    def __init__(self, file_name: str, file_type: str) -> None:
        self.file_name: str = file_name
        self.file_type: str = file_type
        self.df: pd.DataFrame = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        if self.file_type == ".sas":
            self.df = pd.read_sas(self.file_name)
        elif self.file_type == ".sav":
            self.df = pd.read_spss(self.file_name)
        elif self.file_type == ".csv":
            self.df = pd.read_csv(self.file_name)
        elif self.file_type == ".xlsx":
            self.df = pd.read_excel(self.file_name)
        elif self.file_type == ".json":
            self.df = pd.read_json(self.file_name)
        elif self.file_type == ".txt":
            self.df = pd.read_csv(self.file_name, sep="\t")
        elif self.file_type == ".html":
            self.df = pd.read_html(self.file_name)[0]
        elif self.file_type == ".xml":
            self.df = pd.read_xml(self.file_name)
        elif self.file_type == ".parquet":
            self.df = pd.read_parquet(self.file_name)
        else:
            raise ValueError("Unsupported file type")

class Export:
    def __init__(self, df: pd.DataFrame, file_name: str, file_type: str) -> None:
        self.df: pd.DataFrame = df
        self.file_name: str = file_name
        self.file_type: str = file_type
    def _save_data(self) -> None:
        if self.file_name.endswith(".sas"):
            pyreadstat.write_sas(self.df, self.file_name)
        elif self.file_name.endswith(".sav"):
            pyreadstat.write_sav(self.df, self.file_name)
        elif self.file_name.endswith(".csv"):
            self.df.to_csv(self.file_name, index=False)
        elif self.file_name.endswith(".xlsx"):
            self.df.to_excel(self.file_name, index=False)
        elif self.file_name.endswith(".json"):
            self.df.to_json(self.file_name, orient="records")
        elif self.file_name.endswith(".txt"):
            self.df.to_csv(self.file_name, sep="\t", index=False)
        elif self.file_name.endswith(".html"):
            self.df.to_html(self.file_name, index=False)
        elif self.file_name.endswith(".xml"):
            self.df.to_xml(self.file_name, index=False)
        elif self.file_name.endswith(".parquet"):
            self.df.to_parquet(self.file_name, index=False)
        else:
            raise ValueError("Unsupported file type")
        
if __name__ == "__main__":
    print("")