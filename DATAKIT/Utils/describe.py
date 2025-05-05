import pandas as pd

class Variables_Descriptor:
    def __init__(self, df: pd.DataFrame):
        """
        Initialise la classe avec un DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame à analyser.
        """
        self.df = df

    def get_column_types(self):
        """
        Retourne un dictionnaire contenant le type de chaque colonne du DataFrame.

        Returns:
            dict: Un dictionnaire où les clés sont les noms des colonnes et les valeurs sont leurs types.
        """
        column_types = {}
        for column in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[column]):
                column_types[column] = "Numérique"
            elif pd.api.types.is_categorical_dtype(self.df[column]):
                column_types[column] = "Catégorielle"
            elif pd.api.types.is_bool_dtype(self.df[column]):
                column_types[column] = "Booléenne"
            elif pd.api.types.is_datetime64_any_dtype(self.df[column]):
                column_types[column] = "Date/Heure"
            else:
                column_types[column] = "Texte/Objet"
        return column_types

    def describe_column_types(self):
        """
        Affiche les types des colonnes du DataFrame.

        Returns:
            None
        """
        column_types = self.get_column_types()
        for column, col_type in column_types.items():
            print(f"{column}: {col_type}")
            