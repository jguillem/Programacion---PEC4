"""
ex4.py – Exercici 4: Partits guanyats en casa / fora / empat (FTR).

Funcions:
    ftr(data) -> pd.DataFrame
    plot_ftr(ftr_df) -> None
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import config



def ftr(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula el nombre de partits guanyats per locals, visitants i empats.

    Args:
        data: DataFrame del dataset de La Liga.

    Returns:
        DataFrame ``ftr_df`` amb índex [H, A, D] i columna ``Partits``.
    """
    ftr_df = (
        data.groupby("FTR").size()
        .rename("Partits")
        .to_frame()
    )
    return ftr_df


def plot_ftr(ftr_df: pd.DataFrame) -> None:
    """Representa el recompte de resultats (H/A/D) en un gràfic de barres.

    Args:
        ftr_df: DataFrame retornat per :func:`ftr`.
    """
    colors = {"H": "steelblue", "A": "tomato", "D": "goldenrod"}
    color_list = [colors.get(idx, "grey") for idx in ftr_df.index]

    _, ax = plt.subplots(figsize=(6, 5))
    ftr_df["Partits"].plot(kind="bar", ax=ax, color=color_list, edgecolor="black")
    ax.set_title("Resultats finals – La Liga 1995‑2025", fontsize=13)
    ax.set_xlabel("Resultat (H=local, A=visitant, D=empat)")
    ax.set_ylabel("Nombre de partits")
    ax.set_xticklabels(ftr_df.index, rotation=0)
    plt.tight_layout()

    ruta_base = os.path.dirname(__file__)
    nombre_img = f"grafica_ex4_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(os.path.join(ruta_base, "..", "img", nombre_img))
    plt.show()
