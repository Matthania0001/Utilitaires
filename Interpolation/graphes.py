import numpy as np
from operations import evaluate
from donnees import Donnees
from interpolant import poly_interpolant
import plotly.graph_objects as go
from operations import somme_Donnees
import colorsys
def courbe_interpolante(t: Donnees, precision: int = 100):
    if t.est_interpolable():
        n = len(t.list_donnees)
        s = [t.list_donnees[i][0] for i in range(n)]
        b = max(s)
        z = min(s)
        x = np.linspace(z, b, 100*b)
        y = [evaluate(poly_interpolant(t, precision),i) for i in x]
        fig = go.Figure(data=go.Scatter(
            x=x,
            y=y,
            mode='lines',
            line=dict(color='blue', width=2),
            name=""
            #marker=dict(size=4, color='royalblue')
        ))
        fig.update_layout(
            title="",
            title_font_size=100/int(2*n)+2,
            xaxis_title="Axe x",
            yaxis_title="Axe y = P(x)",
            template="plotly_white"
        )
        fig.add_trace(go.Scatter(
            x = [t.list_donnees[i][0] for i in range(n)],
            y = [t.list_donnees[i][1] for i in range(n)],
            mode='markers',
            marker=dict(size=15, color='crimson', symbol='star'),
            #text=  [t.list_donnees[i][1] for i in range(n)],
            #textposition="top center",
            name=''
        ))
        fig.show()
        print(poly_interpolant(t))
    else:
        return "Erreur: Jeu de données non-interpolable"

# Ce graphe fais un comparaison entre la courbe pour t et cell entre t + w
def gr_comp_ajout_points(t: Donnees,w: Donnees, precision = 100):
    p: Donnees = Donnees([])
    p = somme_Donnees(t, w)
    if p.est_interpolable():
        n = len(t.list_donnees)
        s = [t.list_donnees[i][0] for i in range(n)]
        b = max(s)
        z = min(s)
        x = np.linspace(z, b, 100 * b)
        y = [evaluate(poly_interpolant(t, precision), i) for i in x]
        fig = go.Figure(data=go.Scatter(
            x=x,
            y=y,
            mode='lines',
            line=dict(color='blue', width=2),
            name=""
            # marker=dict(size=4, color='royalblue')
        ))
        n2 = len(p.list_donnees)
        s2 = [p.list_donnees[i][0] for i in range(n2)]
        b2 = max(s2)
        z2 = min(s2)
        x2 = np.linspace(z2, b2, 100 * b2)
        y2 = [evaluate(poly_interpolant(p, precision), i) for i in x2]
        fig.add_trace(go.Scatter(
            x=x2,
            y=y2,
            mode='lines',
            line=dict(color='green', width=2),
            name=""
            # marker=dict(size=4, color='royalblue')
        ))

        fig.update_layout(
            title="",
            title_font_size=100 / int(2 * max(n,n2)) + 2,
            xaxis_title="Axe X",
            yaxis_title="Axe Y",
            template="plotly_white"
        )
        fig.add_trace(go.Scatter(
            x=[t.list_donnees[i][0] for i in range(n)],
            y=[t.list_donnees[i][1] for i in range(n)],
            mode='markers',
            marker=dict(size=15, color='crimson', symbol='star'),
            # text=  [t.list_donnees[i][1] for i in range(n)],
            # textposition="top center",
            name=''
        ))
        fig.add_trace(go.Scatter(
            x=[w.list_donnees[i][0] for i in range(len(w.list_donnees))],
            y=[w.list_donnees[i][1] for i in range(len(w.list_donnees))],
            mode='markers',
            marker=dict(size=15, color='black', symbol='star'),
            # text=  [t.list_donnees[i][1] for i in range(n)],
            # textposition="top center",
            name=''
        ))
        fig.show()
    else:
        return "Erreur"


def gr_comp_ajout_point_par_point(t: Donnees,w: Donnees, precision = 100):
    p: Donnees = Donnees([])
    p = somme_Donnees(t, w)
    if t.est_interpolable():
        n = len(t.list_donnees)
        s = [t.list_donnees[i][0] for i in range(n)]
        b = max(s)
        z = min(s)
        x = np.linspace(z, b, 100 * b)
        y = [evaluate(poly_interpolant(t, precision), i) for i in x]
        fig = go.Figure(data=go.Scatter(
            x=x,
            y=y,
            mode='lines',
            line=dict(color='black', width=2),
            name=""
            # marker=dict(size=4, color='royalblue')
        ))
        fig.add_trace(go.Scatter(
            x=[t.list_donnees[i][0] for i in range(n)],
            y=[t.list_donnees[i][1] for i in range(n)],
            mode='markers',
            marker=dict(size=10, color='black', symbol='star'),
            # text=  [t.list_donnees[i][1] for i in range(n)],
            # textposition="top center",
            name=''
        ))
        fig.update_layout(
            title="",
            title_font_size=100 / int(2 * max(n, n)) + 2,
            xaxis_title="Axe X",
            yaxis_title="Axe Y",
            template="plotly_white"
        )
    #colors = [generate_distinct_rgb(j, len(w.list_donnees)) for j in range(len(w.list_donnees))]
    for i in range(len(w.list_donnees)):
        p: Donnees = Donnees([])
        p = somme_Donnees(t, Donnees([w.list_donnees[i]]))
        if p.est_interpolable():
            n2 = len(p.list_donnees)
            s2 = [p.list_donnees[i][0] for i in range(n2)]
            b2 = max(s2)
            z2 = min(s2)
            x2 = np.linspace(z2, b2, 100 * b2)
            y2 = [evaluate(poly_interpolant(p, precision), i) for i in x2]
            r, g, b = [colorsys.hsv_to_rgb(j / len(w.list_donnees), 0.9, 0.9) for j in range(len(w.list_donnees))][i]
            fig.add_trace(go.Scatter(
                x=x2,
                y=y2,
                mode='lines',
                #line=dict(color=f'rgb({34-i},{139+i},{34-i})', width=2),
                line=dict(color=f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})', width=2),
                name=""
                # marker=dict(size=4, color='royalblue')
            ))
            fig.add_trace(go.Scatter(
                x=[w.list_donnees[i][0]],
                y=[w.list_donnees[i][1]],
                mode='markers',
                marker=dict(size=15, color=f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})', symbol='star'),
                # text=  [t.list_donnees[i][1] for i in range(n)],
                # textposition="top center",
                name=''
            ))
        else:
            return "Erreur"
    fig.show()

'''a = Donnees([(i, np.cos(i) + np.sin(i)) for i in range(1,8)])

b = Donnees([(5.5,10),(5.5,20),(5.5,30), (5.5,40)])
print(somme_Donnees(a,b))
for i in range(len(b.list_donnees)):
    p: Donnees = Donnees([])
    p = somme_Donnees(a, Donnees([b.list_donnees[i]]))
    print(p.est_interpolable())
#gr_comp_ajout_point_par_point(a,b)
courbe_interpolante(a)'''