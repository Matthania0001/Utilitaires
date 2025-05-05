import pandas as pd
import plotly.express as px

class ViolinPlot:
    def __init__(self, df: pd.DataFrame, x_column: str = None, y_column: str = None):
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.fig = None

    def create_violin_plot(self, title: str = "Violin Plot", color_column: str = None, box: bool = True, points: str = "all"):
        self.fig = px.violin(
            self.df,
            x=self.x_column,
            y=self.y_column,
            color=color_column,
            box=box,
            points=points,
            title=title
        )

    def show(self):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_violin_plot' d'abord.")
        self.fig.show()

    def save(self, filename: str, file_format: str = "png"):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_violin_plot' d'abord.")
        
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")