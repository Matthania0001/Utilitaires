import pandas as pd
import plotly.express as px

class HexbinPlot:
    def __init__(self, df: pd.DataFrame, x_column: str, y_column: str):
        """
        Initialise la classe HexbinPlot avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            x_column (str): Le nom de la colonne pour l'axe X.
            y_column (str): Le nom de la colonne pour l'axe Y.
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.fig = None

    def create_hexbin_plot(self, title: str = "Hexbin Plot", color_scale: str = "Viridis", nbins: int = 20, midpoint: float = None):
        """
        Crée un hexbin plot interactif avec une color bar personnalisée.

        Args:
            title (str): Le titre du graphique.
            color_scale (str, optional): La palette de couleurs à utiliser. Par défaut, 'Viridis'.
            nbins (int, optional): Nombre de binnings (hexagones). Par défaut, 20.
            midpoint (float, optional): Point médian pour la color bar. Par défaut, None.
        """
        self.fig = px.density_heatmap(
            self.df,
            x=self.x_column,
            y=self.y_column,
            nbinsx=nbins,
            nbinsy=nbins,
            color_continuous_scale=color_scale,
            color_continuous_midpoint=midpoint,
            title=title
        )

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_hexbin_plot' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_hexbin_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")