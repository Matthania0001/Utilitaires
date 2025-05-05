from typing import Optional, List
import pandas as pd
class Clean:
    def __init__(self, df: pd.DataFrame):
        self.df: pd.DataFrame = df
    def remove_empty(self, column_names: Optional[List[str]] = None) -> None:
        if column_names is None or len(column_names) == 0:
            self.df = self.df.dropna()
        else:
            self.df = self.df.dropna(subset=column_names)

    def remove_duplicates(self) -> None:
        self.df = self.df.drop_duplicates()

    def remove_columns_by_variable(self, column_names: List[str]) -> None:
        if column_names:
            self.df = self.df.drop(columns=column_names)

    def remove_columns_by_sequence(self, start: Optional[int] = None, end: Optional[int] = None) -> None:
        if start is None and end is None:
            return
        elif start is not None and end is None:
            if 0 <= start < len(self.df.columns):
                self.df = self.df.drop(columns=self.df.columns[start:])
            else:
                raise IndexError("Start index out of range")
        elif start is None and end is not None:
            if 0 <= end < len(self.df.columns):
                self.df = self.df.drop(columns=self.df.columns[:end + 1])
            else:
                raise IndexError("End index out of range")
        else:
            if 0 <= start <= end < len(self.df.columns):
                self.df = self.df.drop(columns=self.df.columns[start:end + 1])
            else:
                raise IndexError("Start or end index out of range")

    def remove_outliers(self, var: str) -> None:
        if var not in self.df.columns:
            raise ValueError(f"La colonne '{var}' n'existe pas dans le DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.df[var]):
            raise TypeError(f"La colonne '{var}' doit être de type numérique pour calculer les quantiles.")
        
        Q1: float = self.df[var].quantile(0.25)
        Q3: float = self.df[var].quantile(0.75)
        IQR: float = Q3 - Q1
        lower_bound: float = Q1 - 1.5 * IQR
        upper_bound: float = Q3 + 1.5 * IQR
        self.df = self.df[(self.df[var] >= lower_bound) & (self.df[var] <= upper_bound)]
        