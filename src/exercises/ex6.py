"""
ex6.py – Exercici 6: Resum 1995‑2025 i pòdium.

Funcions:
    fun_total_goals(data) -> tuple[int, int, int]
    fun_total_goals_by_team(data) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
    fun_summary_1996_2025(total_pts, home_goals, away_goals, total_goals) -> pd.DataFrame
    podium(summary_df) -> None
"""
import pandas as pd
import matplotlib.pyplot as plt
import config


def fun_total_goals(data: pd.DataFrame) -> tuple[int, int, int]:
    """Calcula els gols locals, visitants i totals del dataset.

    Args:
        data: DataFrame del dataset de La Liga.

    Returns:
        Tupla ``(home_goals, away_goals, total_goals)`` d'enters.
    """
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals
    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(
    data: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Calcula els gols per equip (local, visitant i total).

    Args:
        data: DataFrame del dataset de La Liga.

    Returns:
        Tupla ``(home_goals_by_team, away_goals_by_team, total_goals_by_team)``,
        cada element és un DataFrame ordenat per gols descendentment.
    """
    home_goals_by_team = (
        data.groupby("HomeTeam")["FTHG"]
        .sum()
        .rename("GolsLocal")
        .to_frame()
        .sort_values("GolsLocal", ascending=False)
    )
    away_goals_by_team = (
        data.groupby("AwayTeam")["FTAG"]
        .sum()
        .rename("GolsVisitant")
        .to_frame()
        .sort_values("GolsVisitant", ascending=False)
    )
    total = (
        home_goals_by_team["GolsLocal"]
        .add(away_goals_by_team["GolsVisitant"], fill_value=0)
        .rename("GolsTotal")
        .sort_values(ascending=False)
    )
    total_goals_by_team = total.to_frame()
    home_goals_by_team.index.name = "Equip"
    away_goals_by_team.index.name = "Equip"
    total_goals_by_team.index.name = "Equip"
    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(
    total_points_by_team: pd.Series,
    home_goals_by_team: pd.DataFrame,
    away_goals_by_team: pd.DataFrame,
    total_goals_by_team: pd.DataFrame,
) -> pd.DataFrame:
    """Crea el DataFrame resum a partir de la concatenació dels 4 dataframes.

    Args:
        total_points_by_team: Series de punts per equip.
        home_goals_by_team: DataFrame de gols locals per equip.
        away_goals_by_team: DataFrame de gols visitants per equip.
        total_goals_by_team: DataFrame de gols totals per equip.

    Returns:
        DataFrame ``summary_1996_2025`` amb totes les mètriques per equip,
        ordenat per punts descendentment.
    """
    summary = pd.concat(
        [total_points_by_team, home_goals_by_team,
         away_goals_by_team, total_goals_by_team],
        axis=1,
    )
    summary = summary.sort_values("Punts", ascending=False)
    return summary


def podium(summary_1996_2025: pd.DataFrame) -> None:
    """Genera una gràfica de pòdium amb els tres primers equips del resum.

    El primer equip es col·loca al centre i a major altura; el segon a
    l'esquerra i el tercer a la dreta, ambdós a menor altura.

    Args:
        summary_1996_2025: DataFrame retornat per :func:`fun_summary_1996_2025`.
    """
    top3 = summary_1996_2025.head(3)
    teams = list(top3.index)
    points = list(top3["Punts"])

    # Ordre del pòdium: 2n, 1r, 3r
    podium_order = [teams[1], teams[0], teams[2]]
    podium_heights = [points[1], points[0], points[2]]
    colors = ["silver", "gold", "#cd7f32"]  # plata, or, bronze

    _, ax = plt.subplots(figsize=(7, 6))
    bar_rects = ax.bar(range(3), podium_heights, color=colors, edgecolor="black", width=0.5)

    for rect, team in zip(bar_rects, podium_order):
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            rect.get_height() + 5,
            team,
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Pòdium La Liga 1995‑2025", fontsize=14)
    plt.tight_layout()
    plt.savefig(
        f"img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png"
    )
    plt.show()
