import pandas as pd
import plotly.express as px

class Heatmap:
    def __init__(self, df: pd.DataFrame, x_column: str, y_column: str, value_column: str, aggfunc: str = "sum"):
        """
        Initialise la classe Heatmap avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            x_column (str): Le nom de la colonne pour l'axe X.
            y_column (str): Le nom de la colonne pour l'axe Y.
            value_column (str): Le nom de la colonne pour les valeurs numériques.
            aggfunc (str, optional): La fonction d'agrégation à appliquer ('sum', 'mean', etc.). Par défaut, 'sum'.
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.value_column = value_column
        self.aggfunc = aggfunc
        self.fig = None

    def create_heatmap(self, title: str = "Heatmap", color_scale: str = "Viridis"):
        """
        Crée une heatmap avec une fonction d'agrégation.

        Args:
            title (str): Le titre du graphique.
            color_scale (str, optional): La palette de couleurs à utiliser. Par défaut, 'Viridis'.
        """
        # Agréger les données
        aggregated_df = self.df.pivot_table(
            index=self.y_column,
            columns=self.x_column,
            values=self.value_column,
            aggfunc=self.aggfunc
        )

        # Créer la heatmap
        self.fig = px.imshow(
            aggregated_df,
            color_continuous_scale=color_scale,
            title=title,
            labels=dict(color=self.aggfunc.capitalize())
        )

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_heatmap' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_heatmap' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")