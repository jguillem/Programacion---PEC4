"""
ex1.py – Exercici 1: Càrrega del dataset i anàlisi exploratòria (EDA).

Funcions:
    load_and_eda(file) -> pd.DataFrame
    plot_home_away_goals(data) -> None
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import config



def load_and_eda(file: str) -> pd.DataFrame:
    """Carrega el dataset i elimina les columnes HTHG, HTAG i HTR.

    Mostra els primers i últims valors del dataset i la informació rellevant.

    Args:
        file: Ruta relativa o absoluta al fitxer CSV.

    Returns:
        DataFrame net sense les columnes de mig temps.
    """
    data = pd.read_csv(file)
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])
    print("=== Primers valors ===")
    print(data.head())
    print("\n=== Últims valors ===")
    print(data.tail())
    print("\n=== Informació general ===")
    print(data.info())
    print("\n=== Estadístiques descriptives ===")
    print(data.describe())
    return data


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """Mostra la distribució de gols marcats per local i visitant amb boxplots.

    Args:
        data: DataFrame del dataset de La Liga.
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))
    fig.suptitle("Distribució de gols – La Liga 1995‑2025", fontsize=14)

    axes[0].boxplot(data["FTHG"].dropna(), patch_artist=True,
                    boxprops={"facecolor": "steelblue", "color": "navy"})
    axes[0].set_title("Gols locals (FTHG)")
    axes[0].set_ylabel("Gols")

    axes[1].boxplot(data["FTAG"].dropna(), patch_artist=True,
                    boxprops={"facecolor": "tomato", "color": "darkred"})
    axes[1].set_title("Gols visitants (FTAG)")
    axes[1].set_ylabel("Gols")

    plt.tight_layout()

    ruta_base = os.path.dirname(__file__)
    nombre_img = f"grafica_ex1_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(os.path.join(ruta_base, "..", "img", nombre_img))
    plt.show()
