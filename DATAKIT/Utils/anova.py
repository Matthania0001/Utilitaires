import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

class AnovaAnalyzer:
    def __init__(self, dataframe: pd.DataFrame, target_column: str, group_column: str):
        """
        Initialise l'analyseur ANOVA.
        
        Args:
            dataframe (pd.DataFrame): DataFrame contenant les données
            target_column (str): Nom de la colonne numérique à analyser
            group_column (str): Nom de la colonne catégorielle définissant les groupes
        """
        self.df = dataframe.dropna(subset=[target_column, group_column]).copy()
        self.target = target_column
        self.group = group_column
        self.anova_result = None
        self.tukey_result = None
        
    def run_anova(self):
        """Exécute le test ANOVA unidirectionnel."""
        # Préparation des données
        groups = self.df[self.group].unique()
        group_data = [self.df[self.df[self.group] == g][self.target] for g in groups]
        
        # Test ANOVA
        self.anova_result = stats.f_oneway(*group_data)
        
        # Test post-hoc de Tukey
        self.tukey_result = pairwise_tukeyhsd(
            endog=self.df[self.target],
            groups=self.df[self.group],
            alpha=0.05
        )
        
        return self.anova_result
    
    def get_results(self):
        """Retourne les résultats sous forme de dictionnaire."""
        if self.anova_result is None:
            self.run_anova()
            
        return {
            'anova': {
                'statistic': self.anova_result.statistic,
                'pvalue': self.anova_result.pvalue
            },
            'tukey': {
                'summary': self.tukey_result.summary(),
                'reject': self.tukey_result.reject
            }
        }
    
    def plot_results(self):
        """Visualise les résultats avec une boîte à moustaches."""
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df, x=self.group, y=self.target)
        plt.title(f"Distribution de {self.target} par {self.group}")
        plt.xticks(rotation=45)
        plt.show()
        
        # Affichage des résultats ANOVA
        print("\nRésultats ANOVA:")
        print(f"F-statistic: {self.anova_result.statistic:.4f}")
        print(f"p-value: {self.anova_result.pvalue:.4f}")
        
        # Interprétation
        alpha = 0.05
        if self.anova_result.pvalue < alpha:
            print("\nConclusion: Il existe des différences significatives entre les groupes (p < 0.05)")
            print("\nComparaisons multiples (Tukey HSD):")
            print(self.tukey_result.summary())
        else:
            print("\nConclusion: Aucune différence significative entre les groupes (p > 0.05)")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création de données exemple
    data = {
        'valeur': [25, 30, 28, 36, 29, 22, 35, 40, 32, 27, 31, 38],
        'groupe': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'A', 'B', 'C']
    }
    df = pd.DataFrame(data)
    
    # Analyse ANOVA
    analyzer = AnovaAnalyzer(df, 'valeur', 'groupe')
    results = analyzer.run_anova()
    analyzer.plot_results()