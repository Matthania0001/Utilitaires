import pandas as pd
import plotly.express as px

class LatticePlot:
    def __init__(self, df: pd.DataFrame, x_column: str, y_column: str, facet_row: str = None, facet_col: str = None):
        """
        Initialise la classe LatticePlot avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            x_column (str): Le nom de la colonne pour l'axe X.
            y_column (str): Le nom de la colonne pour l'axe Y.
            facet_row (str, optional): Colonne pour créer des facettes en lignes. Par défaut, aucune.
            facet_col (str, optional): Colonne pour créer des facettes en colonnes. Par défaut, aucune.
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.facet_row = facet_row
        self.facet_col = facet_col
        self.fig = None

    def create_lattice_plot(self, title: str = "Lattice Plot", color_column: str = None):
        """
        Crée un lattice plot interactif.

        Args:
            title (str): Le titre du graphique.
            color_column (str, optional): Colonne pour colorer les points. Par défaut, aucune.
        """
        self.fig = px.scatter(
            self.df,
            x=self.x_column,
            y=self.y_column,
            color=color_column,
            facet_row=self.facet_row,
            facet_col=self.facet_col,
            title=title
        )

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_lattice_plot' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_lattice_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")