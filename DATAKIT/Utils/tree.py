import pandas as pd
import plotly.express as px

class TreeMap:
    def __init__(self, df: pd.DataFrame, path_columns: list, value_column: str, color_column: str = None):
        """
        Initialise la classe TreeMap avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            path_columns (list): Liste des colonnes définissant la hiérarchie (ordre des niveaux).
            value_column (str): Le nom de la colonne pour les valeurs numériques.
            color_column (str, optional): Colonne pour colorer les blocs. Par défaut, aucune.
        """
        self.df = df
        self.path_columns = path_columns
        self.value_column = value_column
        self.color_column = color_column
        self.fig = None

    def create_tree_map(self, title: str = "Tree Map", color_scale: str = "Viridis"):
        """
        Crée une tree map interactive.

        Args:
            title (str): Le titre du graphique.
            color_scale (str, optional): La palette de couleurs à utiliser. Par défaut, 'Viridis'.
        """
        self.fig = px.treemap(
            self.df,
            path=self.path_columns,
            values=self.value_column,
            color=self.color_column,
            color_continuous_scale=color_scale,
            title=title
        )

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_tree_map' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_tree_map' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")
        
