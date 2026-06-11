"""
ex3.py – Exercici 3: Distribució de gols marcats.

Funcions:
    goals_distribution(data) -> tuple[pd.DataFrame, pd.DataFrame]
    plot_goals_distribution(distr_goals_home, distr_goals_away) -> None
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import config



def goals_distribution(
    data: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Calcula la distribució de gols locals i visitants.

    Args:
        data: DataFrame del dataset de La Liga.

    Returns:
        Tupla ``(distr_goals_home, distr_goals_away)``. Cada DataFrame té com
        a índex el nombre de gols i com a columna el nombre de partits en què
        s'han marcat aquells gols.
    """
    distr_goals_home = (
        data.groupby("FTHG").size()
        .rename("Partits")
        .to_frame()
    )
    distr_goals_home.index.name = "Gols"

    distr_goals_away = (
        data.groupby("FTAG").size()
        .rename("Partits")
        .to_frame()
    )
    distr_goals_away.index.name = "Gols"

    return distr_goals_home, distr_goals_away


def plot_goals_distribution(
    distr_goals_home: pd.DataFrame,
    distr_goals_away: pd.DataFrame,
) -> None:
    """Representa la distribució de gols locals i visitants en dos subplots.

    Args:
        distr_goals_home: DataFrame retornat per :func:`goals_distribution`.
        distr_goals_away: DataFrame retornat per :func:`goals_distribution`.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Distribució de gols – La Liga 1995‑2025", fontsize=14)

    distr_goals_home["Partits"].plot(
        kind="bar", ax=axes[0], color="steelblue", edgecolor="navy"
    )
    axes[0].set_title("Gols locals (FTHG)")
    axes[0].set_xlabel("Gols")
    axes[0].set_ylabel("Partits")

    distr_goals_away["Partits"].plot(
        kind="bar", ax=axes[1], color="tomato", edgecolor="darkred"
    )
    axes[1].set_title("Gols visitants (FTAG)")
    axes[1].set_xlabel("Gols")
    axes[1].set_ylabel("Partits")

    plt.tight_layout()

    ruta_base = os.path.dirname(__file__)
    nombre_img = f"grafica_ex3_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(os.path.join(ruta_base, "..", "img", nombre_img))
    plt.show()
