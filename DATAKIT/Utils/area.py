import pandas as pd
import plotly.express as px

class AreaPlot:
    def __init__(self, df: pd.DataFrame, x_column: str, y_column: str, group_column: str = None):
        """
        Initialise la classe AreaPlot avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            x_column (str): Le nom de la colonne pour l'axe X.
            y_column (str): Le nom de la colonne pour l'axe Y.
            group_column (str, optional): Colonne pour grouper les données (empilement). Par défaut, aucune.
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.group_column = group_column
        self.fig = None

    def create_area_plot(self, title: str = "Area Plot", color_scale: str = "Viridis"):
        """
        Crée un area plot interactif.

        Args:
            title (str): Le titre du graphique.
            color_scale (str, optional): La palette de couleurs à utiliser. Par défaut, 'Viridis'.
        """
        self.fig = px.area(
            self.df,
            x=self.x_column,
            y=self.y_column,
            color=self.group_column,
            title=title,
            color_discrete_sequence=px.colors.qualitative.Vivid if self.group_column else None
        )

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_area_plot' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_area_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")
        
        