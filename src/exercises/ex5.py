"""
ex5.py – Exercici 5: Classificació global 1995‑2025.

Funcions:
    add_points(data) -> pd.DataFrame
    fun_total_points(data) -> tuple[pd.Series, pd.DataFrame]
    alltime_winner(df_total_points) -> str
"""
import pandas as pd


def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """Afegeix les columnes ``points_home`` i ``points_away`` al dataset.

    Cada columna pot prendre els valors 3 (victòria), 1 (empat) o 0 (derrota).

    Args:
        data: DataFrame del dataset de La Liga.

    Returns:
        DataFrame ampliat amb les dues columnes de punts.
    """
    pts_map_home = {"H": 3, "D": 1, "A": 0}
    pts_map_away = {"A": 3, "D": 1, "H": 0}
    data = data.copy()
    data["points_home"] = data["FTR"].map(pts_map_home)
    data["points_away"] = data["FTR"].map(pts_map_away)
    return data


def fun_total_points(
    data: pd.DataFrame,
) -> tuple[pd.Series, pd.DataFrame]:
    """Calcula els punts totals acumulats per cada equip des de 1995.

    Args:
        data: DataFrame que ja conté les columnes ``points_home`` i
            ``points_away`` (resultat de :func:`add_points`).

    Returns:
        Tupla ``(total_points_by_team, df_total_points_by_team)`` on el primer
        element és una :class:`pd.Series` i el segon un :class:`pd.DataFrame`,
        tots dos ordenats de major a menor puntuació.
    """
    home_pts = data.groupby("HomeTeam")["points_home"].sum()
    away_pts = data.groupby("AwayTeam")["points_away"].sum()
    total_points_by_team = (home_pts.add(away_pts, fill_value=0)
                            .rename("Punts")
                            .sort_values(ascending=False))
    df_total_points_by_team = total_points_by_team.to_frame()
    return total_points_by_team, df_total_points_by_team


def alltime_winner(df_total_points: pd.DataFrame) -> str:
    """Retorna el nom de l'equip amb més punts acumulats en tota la història.

    Args:
        df_total_points: DataFrame retornat per :func:`fun_total_points`.

    Returns:
        Nom de l'equip guanyador.
    """
    return str(df_total_points["Punts"].idxmax())
