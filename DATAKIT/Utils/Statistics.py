import pandas as pd
from typing import Optional, List
class Statistics:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df: pd.DataFrame = df
    def mean(self, column: str) -> float:
        return self.df[column].mean()
    def median(self, column: str) -> float:
        return self.df[column].median()
    def mode(self, column: str) -> pd.Series:
        return self.df[column].mode()
    def std(self, column: str) -> float:
        return self.df[column].std()
    def var(self, column: str) -> float:
        return self.df[column].var()
    def min(self, column: str) -> float:
        return self.df[column].min()
    def max(self, column: str) -> float:
        return self.df[column].max()
    def count(self, column: str) -> int:
        return self.df[column].count()
    def count_unique(self, column: str) -> int:
        return self.df[column].nunique()
    def unique_values(self, column: str) -> pd.Series:
        return self.df[column].unique()
    def frequency(self, column: str) -> pd.Series:
        return self.df[column].value_counts()
    def get_summary(self, column: str) -> pd.DataFrame:
        return self.df[column].describe()
    
    