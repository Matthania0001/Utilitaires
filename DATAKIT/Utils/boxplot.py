import plotly.express as px
import pandas as pd

class BoxPlot:
    def __init__(self, dataframe: pd.DataFrame, column_name: str):
        self.df = dataframe
        self.column_name = column_name
        self.fig = None

    def create_box_plot(self, title="Titre", yaxis_title="Valeurs", boxpoints='all'):
        self.fig = px.box(
            self.df,
            y=self.column_name,
            points=boxpoints,
            title=title
        )
        self.fig.update_layout(
            yaxis_title=yaxis_title,
            boxmode="group"
        )

    def save(self, filename, file_format="png"):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_box_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")

    def show(self):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_box_plot' d'abord.")
        self.fig.show()