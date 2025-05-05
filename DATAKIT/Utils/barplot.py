import pandas as pd
import plotly.express as px

class BarPlot:
    def __init__(self, df: pd.DataFrame, x_column: str, y_column: str):
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.fig = None

    def create_bar_plot(self, title: str = "Bar Plot", color_column: str = None, orientation: str = "v"):
        self.fig = px.bar(
            self.df,
            x=self.x_column,
            y=self.y_column,
            color=color_column,
            title=title,
            orientation=orientation
        )

    def show(self):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_bar_plot' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_bar_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")