import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

class Dashboard:
    def __init__(self, title="Dashboard"):
        """
        Initialise la classe Dashboard.

        Args:
            title (str): Le titre général du tableau de bord.
        """
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.title = title
        self.layout = []
        self.general_title = title

    def set_general_title(self, title):
        """
        Définit ou met à jour le titre général du tableau de bord.

        Args:
            title (str): Le nouveau titre général.
        """
        self.general_title = title

    def add_row(self, figures, row_title=None):
        """
        Ajoute une ligne au tableau de bord avec un titre optionnel.

        Args:
            figures (list): Liste des objets `fig` (graphiques Plotly) à afficher dans la ligne.
            row_title (str, optional): Titre de la ligne. Par défaut, None.
        """
        # Créer les colonnes avec les graphiques
        cols = [dbc.Col(dcc.Graph(figure=fig), width=12 // len(figures)) for fig in figures]
        
        # Si un titre de ligne est spécifié, l'ajouter au-dessus des graphiques
        if row_title:
            row_content = [
                html.H4(row_title, className="mt-4 mb-3"),
                dbc.Row(cols, className="mb-4")
            ]
        else:
            row_content = [dbc.Row(cols, className="mb-4")]
            
        self.layout.extend(row_content)

    def run(self, host="127.0.0.1", port=8050, debug=False):
        """
        Lance le tableau de bord.

        Args:
            host (str): Adresse hôte. Par défaut, "127.0.0.1".
            port (int): Port pour exécuter l'application. Par défaut, 8050.
            debug (bool): Mode debug. Par défaut, False.
        """
        # Ajouter le titre général en haut du tableau de bord
        full_layout = [
            html.H1(self.general_title, className="text-center my-4"),
            *self.layout
        ]
        
        self.app.layout = html.Div(full_layout, className="container")
        self.app.run(host=host, port=port, debug=False)