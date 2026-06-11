"""
main.py – Punt d'entrada principal de la PEC4.

Ús:
    python main.py -h
    python main.py -ex 7

El paràmetre -ex indica fins a quin exercici s'executa (de forma acumulada).
Per exemple, ``-ex 5`` executa els exercicis 1 al 5.
"""
import argparse
import os
import sys

# sys.path manipulation nécessaire pour importer config et exercises depuis src/
sys.path.insert(0, os.path.dirname(__file__))  # pylint: disable=wrong-import-position

import config  # pylint: disable=wrong-import-position
from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7  # pylint: disable=wrong-import-position

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "LaLiga_Matches.csv")


def parse_args() -> argparse.Namespace:
    """Analitza els arguments de línia de comandes.

    Returns:
        Namespace amb el camp ``ex`` (enter de 1 a 7).
    """
    parser = argparse.ArgumentParser(
        description="PEC4 – Anàlisi La Liga 1995‑2025",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples:\n"
            "  python main.py -ex 1   -> executa l'exercici 1\n"
            "  python main.py -ex 5   -> executa els exercicis 1‑5\n"
            "  python main.py -ex 7   -> executa tots els exercicis\n"
        ),
    )
    parser.add_argument(
        "-ex",
        type=int,
        choices=range(1, 8),
        default=7,
        metavar="N",
        help="Executa els exercicis de l'1 fins a N (1‑7). Per defecte: 7.",
    )
    return parser.parse_args()


def run(max_ex: int) -> None:  # pylint: disable=too-many-locals,too-many-statements
    """Executa seqüencialment els exercicis fins a ``max_ex``.

    Args:
        max_ex: Nombre màxim d'exercici a executar (inclusiu).
    """
    print(f"\n{'='*55}")
    print(f"  PEC4 – La Liga 1995‑2025  |  Alumne: {config.nom_alumne}")
    print(f"  Timestamp: {config.date_time}")
    print(f"{'='*55}\n")

    # ── Exercici 1 ─────────────────────────────────────────────
    data = ex1.load_and_eda(DATA_FILE)
    if max_ex >= 1:
        print("\n── Ex 1: Gràfica distribució de gols (boxplot) ──")
        ex1.plot_home_away_goals(data)

    if max_ex < 2:
        return

    # ── Exercici 2 ─────────────────────────────────────────────
    print("\n── Ex 2: Partits totals per equip ──")
    matches_team_total = ex2.total_matches(data)
    print(matches_team_total.head(10))

    max_matches = matches_team_total["Partits"].max()
    always_first = matches_team_total[
        matches_team_total["Partits"] == max_matches
    ]
    print(f"\nEquips sempre en 1a divisió (màx. {int(max_matches)} partits):")
    print(always_first)

    ex2.plot_matches_team_total(matches_team_total)

    if max_ex < 3:
        return

    # ── Exercici 3 ─────────────────────────────────────────────
    print("\n── Ex 3: Distribució de gols ──")
    distr_home, distr_away = ex3.goals_distribution(data)
    print("Distribució gols locals:")
    print(distr_home)
    print("\nDistribució gols visitants:")
    print(distr_away)
    ex3.plot_goals_distribution(distr_home, distr_away)

    if max_ex < 4:
        return

    # ── Exercici 4 ─────────────────────────────────────────────
    print("\n── Ex 4: Resultats finals (FTR) ──")
    ftr_df = ex4.ftr(data)
    print(ftr_df)
    total = ftr_df["Partits"].sum()
    home_pct = ftr_df.loc["H", "Partits"] / total * 100
    print(f"\nPercentatge de victòries locals: {home_pct:.2f}%")
    ex4.plot_ftr(ftr_df)

    if max_ex < 5:
        return

    # ── Exercici 5 ─────────────────────────────────────────────
    print("\n── Ex 5: Classificació global 1995‑2025 ──")
    data = ex5.add_points(data)
    print(data.head(10))
    total_pts, df_total_pts = ex5.fun_total_points(data)
    print("\nTop 10 equips per punts acumulats:")
    print(df_total_pts.head(10))
    winner = ex5.alltime_winner(df_total_pts)
    print(f"\nGuanyador històric: {winner}")

    if max_ex < 6:
        return

    # ── Exercici 6 ─────────────────────────────────────────────
    print("\n── Ex 6: Resum i pòdium ──")
    home_g, away_g, total_g = ex6.fun_total_goals(data)
    print(f"Gols locals: {home_g} | Gols visitants: {away_g} | Total: {total_g}")

    hg_team, ag_team, tg_team = ex6.fun_total_goals_by_team(data)
    print("\nTop 10 equips per gols totals:")
    print(tg_team.head(10))

    summary = ex6.fun_summary_1996_2025(total_pts, hg_team, ag_team, tg_team)
    print("\nResum (primeres files):")
    print(summary.head())

    ex6.podium(summary)

    if max_ex < 7:
        return

    # ── Exercici 7 ─────────────────────────────────────────────
    print("\n── Ex 7: Graf de connexions ──")
    top5 = list(df_total_pts.head(5).index)
    print(f"Top 5 equips: {top5}")
    ex7.graf(data, top5)


def main() -> None:
    """Funció principal: analitza arguments i llença l'execució."""
    args = parse_args()
    run(args.ex)


if __name__ == "__main__":
    main()
