import pandas as pd
import plotly.express as px

class ScatterPlot:
    def __init__(self, df: pd.DataFrame, x_column: str, y_column: str, z_column: str = None):
        """
        Initialise la classe ScatterPlot avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            x_column (str): Le nom de la colonne pour l'axe X.
            y_column (str): Le nom de la colonne pour l'axe Y.
            z_column (str, optional): Le nom de la colonne pour l'axe Z (pour un scatter plot 3D). Par défaut, None.
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.z_column = z_column
        self.fig = None

    def create_scatter_plot(self, title: str = "Scatter Plot", color_column: str = None, size_column: str = None):
        """
        Crée un scatter plot interactif en 2D ou 3D.

        Args:
            title (str): Le titre du graphique.
            color_column (str, optional): Colonne pour colorer les points. Par défaut, None.
            size_column (str, optional): Colonne pour définir la taille des points. Par défaut, None.
        """
        if self.z_column is None:
            # Scatter plot 2D
            self.fig = px.scatter(
                self.df,
                x=self.x_column,
                y=self.y_column,
                color=color_column,
                size=size_column,
                title=title
            )
        else:
            # Scatter plot 3D
            self.fig = px.scatter_3d(
                self.df,
                x=self.x_column,
                y=self.y_column,
                z=self.z_column,
                color=color_column,
                size=size_column,
                title=title
            )

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_scatter_plot' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_scatter_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")