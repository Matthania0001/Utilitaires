from Utils import dashboard, datatransfer, histogram, pieplot
a = datatransfer.Import("data.csv", ".csv")
a._load_data()
b = pieplot.PiePlot(a.df, "niveau_etude")
b.create_pie_plot("Repartition par niveau d'étude")
b.show()

import plotly.express as px


# Exemple de graphiques
df = px.data.iris()

fig1 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Scatter Plot")
fig2 = px.histogram(df, x="sepal_width", title="Histogram")
fig3 = px.box(df, x="species", y="petal_length", title="Box Plot")
fig4 = px.violin(df, x="species", y="petal_width", title="Violin Plot")

# Création du tableau de bord
dashboard = dashboard.Dashboard(title="Exemple de Dashboard")

# Ajout de lignes avec des graphiques
dashboard.add_row([fig1], row_title="Scatter Plot")
dashboard.add_row([fig2])
dashboard.add_row([fig3])# Ligne 1 : Scatter Plot et Histogram
dashboard.add_row([fig4])  # Ligne 2 : Box Plot et Violin Plot

# Lancement du tableau de bord
dashboard.run()