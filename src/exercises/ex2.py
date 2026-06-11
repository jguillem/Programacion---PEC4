"""
ex2.py – Exercici 2: Partits totals jugats per equip.

Funcions:
    total_matches(data) -> pd.DataFrame
    plot_matches_team_total(matches_team_total) -> None
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import config



def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula el nombre total de partits jugats per cada equip (local + visitant).

    Args:
        data: DataFrame del dataset de La Liga.

    Returns:
        DataFrame ``matches_team_total`` amb index=equip i columna ``Partits``,
        ordenat de major a menor.
    """
    home = data.groupby("HomeTeam").size()
    away = data.groupby("AwayTeam").size()
    matches_team_total = (home.add(away, fill_value=0)
                          .rename("Partits")
                          .sort_values(ascending=False))
    return matches_team_total.to_frame()


def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """Representa el nombre de partits totals per equip en un gràfic de barres.

    Args:
        matches_team_total: DataFrame retornat per :func:`total_matches`.
    """
    _, ax = plt.subplots(figsize=(14, 6))
    matches_team_total["Partits"].plot(
        kind="bar", ax=ax, color="steelblue", edgecolor="navy"
    )
    ax.set_title("Partits totals jugats per equip (1995‑2025)", fontsize=13)
    ax.set_xlabel("Equip")
    ax.set_ylabel("Nombre de partits")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    ruta_base = os.path.dirname(__file__)
    nombre_img = f"grafica_ex2_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(os.path.join(ruta_base, "..", "img", nombre_img))
    plt.show()
