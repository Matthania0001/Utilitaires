import pandas as pd
import plotly.graph_objects as go

class ParetoPlot:
    def __init__(self, df: pd.DataFrame, category_column: str, value_column: str):
        """
        Initialise la classe ParetoPlot avec un DataFrame et les colonnes nécessaires.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
            category_column (str): Le nom de la colonne pour les catégories.
            value_column (str): Le nom de la colonne pour les valeurs associées aux catégories.
        """
        self.df = df
        self.category_column = category_column
        self.value_column = value_column
        self.fig = None

    def create_pareto_plot(self, title: str = "Pareto Chart"):
        """
        Crée un graphique de Pareto interactif.

        Args:
            title (str): Le titre du graphique.
        """
        # Trier les données par ordre décroissant des valeurs
        sorted_df = self.df.sort_values(by=self.value_column, ascending=False)
        sorted_df['Cumulative Percentage'] = sorted_df[self.value_column].cumsum() / sorted_df[self.value_column].sum() * 100

        # Créer le graphique combiné (barres + ligne cumulative)
        fig = go.Figure()

        # Ajouter les barres
        fig.add_trace(go.Bar(
            x=sorted_df[self.category_column],
            y=sorted_df[self.value_column],
            name="Valeurs",
            marker=dict(color="blue")
        ))

        # Ajouter la ligne cumulative
        fig.add_trace(go.Scatter(
            x=sorted_df[self.category_column],
            y=sorted_df['Cumulative Percentage'],
            name="Pourcentage cumulatif",
            mode="lines+markers",
            line=dict(color="red")
        ))

        # Mettre à jour les titres et axes
        fig.update_layout(
            title=title,
            xaxis_title=self.category_column,
            yaxis_title=self.value_column,
            yaxis2=dict(
                title="Pourcentage cumulatif",
                overlaying="y",
                side="right"
            ),
            legend=dict(x=0.8, y=1.2)
        )

        self.fig = fig

    def show(self):
        """
        Affiche le graphique dans le navigateur.
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_pareto_plot' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        """
        Sauvegarde le graphique dans un fichier.

        Args:
            filename (str): Le nom du fichier de sortie.
            file_format (str): Le format du fichier ('html' ou 'png').
        """
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_pareto_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")