"""
ex7.py – Exercici 7: Graf de connexions entre els 5 millors equips.

Funcions:
    graf(data, selected_teams) -> None
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import config


def graf(data: pd.DataFrame, selected_teams: list[str]) -> None:
    """Genera un graf de connexions entre els equips seleccionats.

    Per a cada parell d'equips es calcula el nombre total de partits jugats
    entre ells (partits com a local + com a visitant) i es representa com
    el pes de l'aresta.

    Args:
        data: DataFrame del dataset de La Liga.
        selected_teams: Llista amb els 5 equips de millor puntuació acumulada.
    """
    filtered = data[
        data["HomeTeam"].isin(selected_teams) & data["AwayTeam"].isin(selected_teams)
    ]

    graph = nx.Graph()
    graph.add_nodes_from(selected_teams)

    for team_a in selected_teams:
        for team_b in selected_teams:
            if team_a >= team_b:
                continue
            matches = len(
                filtered[
                    ((filtered["HomeTeam"] == team_a) & (filtered["AwayTeam"] == team_b))
                    | ((filtered["HomeTeam"] == team_b) & (filtered["AwayTeam"] == team_a))
                ]
            )
            if matches > 0:
                graph.add_edge(team_a, team_b, weight=matches)

    pos = nx.spring_layout(graph, seed=42)
    edge_labels = nx.get_edge_attributes(graph, "weight")

    _, ax = plt.subplots(figsize=(9, 7))
    nx.draw_networkx_nodes(graph, pos, ax=ax, node_size=1800,
                           node_color="steelblue", alpha=0.9)
    nx.draw_networkx_labels(graph, pos, ax=ax, font_size=9,
                            font_color="white", font_weight="bold")
    nx.draw_networkx_edges(graph, pos, ax=ax, width=2, edge_color="grey")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels,
                                 ax=ax, font_size=10)

    ax.set_title("Graf de partits entre els 5 millors equips (1995‑2025)", fontsize=13)
    ax.axis("off")
    plt.tight_layout()

    ruta_base = os.path.dirname(__file__)
    nombre_img = f"grafica_ex7_{config.nom_alumne}_{config.date_time}.png"
    plt.savefig(os.path.join(ruta_base, "..", "img", nombre_img))
    plt.show()
