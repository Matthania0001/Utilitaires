import pandas as pd
import plotly.express as px

class Histogram:
    def __init__(self, df: pd.DataFrame, column_name: str):
        self.df = df
        self.column_name = column_name
        self.fig = None

    def create_histogram(self, nbins=None, color='black', border_width=1,
                           title="Histogram", title_x=None, title_y="Fréquence"):
        if self.df is None:
            raise ValueError("Le DataFrame est vide ou non initialisé.")
        
        x = self.df[self.column_name]
        fig = px.histogram(x=x, nbins=nbins)
        fig.update_traces(marker_line_color=color, marker_line_width=border_width)
        fig.update_layout(
            title=title,
            xaxis_title=title_x if title_x else self.column_name,
            yaxis_title=title_y
        )
        self.fig = fig  
    def show(self):
        if self.fig is None:
            raise ValueError("Aucun graphique à afficher. Utilisez 'create_histogram()' d'abord.")
        self.fig.show()
    def save(self, filename: str, file_format: str = "png"):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_box_plot' d'abord.")
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")