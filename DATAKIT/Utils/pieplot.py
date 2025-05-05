import pandas as pd
import plotly.express as px
class PiePlot:
    def __init__(self, df: pd.DataFrame, column_name: str):
        self.df = df
        self.column_name = column_name
        self.fig = None    
    def create_pie_plot(self, title: str = ""):
        # Compter les occurrences de chaque valeur dans la colonne
        value_counts = self.df[self.column_name].value_counts()
        # Créer le graphique en secteurs
        if title == None:
            fig = px.pie(value_counts, values=value_counts.values, names=value_counts.index, title=f'Répartition de {self.column_name}')
        else:
           fig = px.pie(value_counts, values=value_counts.values, names=value_counts.index, title=title) 
        self.fig = fig
    def show(self):
        if self.fig is None:
            raise ValueError("Le graphique n'a pas encore été créé. Appelez 'create_pie_plot' d'abord.")
        else:
            self.fig.show()
    def save(self, filename: str, file_format: str = "png"):
        if file_format == "html":
            self.fig.write_html(filename)
        elif file_format == "png":
            self.fig.write_image(filename)
        else:
            raise ValueError("Format non pris en charge. Utilisez 'html' ou 'png'.")