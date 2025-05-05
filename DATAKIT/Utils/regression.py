import numpy as np
class LinearRegression:
    #Methodes des moindres carrés
    def __init__(self, x: list, y: list):
        self.x = x
        self.y = y
        self.slope = None
        self.intercept = None
        self.r_squared = None
    def fit(self):
        n = len(self.x)
        x_mean = sum(self.x) / n
        y_mean = sum(self.y) / n
        numerator = sum((self.x[i] - x_mean) * (self.y[i] - y_mean) for i in range(n))
        denominator = sum((self.x[i] - x_mean) ** 2 for i in range(n))
        
        self.slope = numerator / denominator
        self.intercept = y_mean - self.slope * x_mean

    def predict(self, x):
        return [self.slope * xi + self.intercept for xi in x]

    def calculate_r_squared(self):
        ss_total = sum((yi - sum(self.y) / len(self.y)) ** 2 for yi in self.y)
        ss_residual = sum((yi - self.predict([xi])[0]) ** 2 for xi, yi in zip(self.x, self.y))
        
        self.r_squared = 1 - (ss_residual / ss_total)
import numpy as np

class PolynomialRegression:
    def __init__(self, x, y, degree):
        self.x = x
        self.y = y
        self.degree = degree
        self.coefficients = None
        self.r_squared = None

    def fit(self):
        # Construction de la matrice de Vandermonde
        X = np.vander(self.x, self.degree + 1, increasing=True)
        # Résolution des coefficients avec la méthode des moindres carrés
        self.coefficients = np.linalg.lstsq(X, self.y, rcond=None)[0]

    def predict(self, x):
        # Construction de la matrice de Vandermonde pour les nouvelles données
        X = np.vander(x, self.degree + 1, increasing=True)
        # Calcul des prédictions
        return X @ self.coefficients

    def calculate_r_squared(self):
        # Calcul de la somme totale des carrés
        y_mean = np.mean(self.y)
        ss_total = sum((yi - y_mean) ** 2 for yi in self.y)
        # Calcul de la somme des résidus au carré
        y_pred = self.predict(self.x)
        ss_residual = sum((yi - y_pred[i]) ** 2 for i, yi in enumerate(self.y))
        # Calcul du coefficient de détermination R²
        self.r_squared = 1 - (ss_residual / ss_total)