import pandas as pd
import plotly.express as px

class RadarChart:
    def __init__(self, df: pd.DataFrame, category_column: str, value_columns: list):
        """
        Initialise la classe RadarChart avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            category_column (str): Le nom de la colonne pour les catégories (axes du radar).
            value_columns (list): Liste des colonnes contenant les valeurs pour chaque axe.
        """
        self.df = df
        self.category_column = category_column
        self.value_columns = value_columns
        self.fig = None

    def create_radar_chart(self, title: str = "Radar Chart"):
        """
        Crée un radar chart interactif.

        Args:
            title (str): Le titre du graphique.
        """
        # Transformer les données pour qu'elles soient compatibles avec le radar chart
        melted_df = self.df.melt(id_vars=[self.category_column], value_vars=self.value_columns,
                                 var_name="Variable", value_name="Valeur")

        # Créer le radar chart
        self.fig = px.line_polar(
            melted_df,
            r="Valeur",
            theta="Variable",
            color=self.category_column,
            line_close=True,
            title=title
        )

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_radar_chart' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_radar_chart' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")