"""
tests_ex6.py – Tests unitaris per a les funcions de l'exercici 6.

Execució:
    python -m pytest tests/tests_ex6.py -v
"""
import sys
import os
import pandas as pd
import pytest

# Afegim src/ al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from exercises.ex6 import fun_total_goals


class TestFunTotalGoals:
    """Suite de tests per a fun_total_goals."""

    def _make_data(self, fthg: list[int], ftag: list[int]) -> pd.DataFrame:
        """Construeix un DataFrame mínim per a les proves.

        Args:
            fthg: Llista de gols locals per partit.
            ftag: Llista de gols visitants per partit.

        Returns:
            DataFrame amb columnes FTHG i FTAG.
        """
        return pd.DataFrame({"FTHG": fthg, "FTAG": ftag})

    def test_returns_tuple_of_three(self) -> None:
        """fun_total_goals ha de retornar una tupla de 3 elements."""
        data = self._make_data([1, 2], [0, 1])
        result = fun_total_goals(data)
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_types_are_int(self) -> None:
        """Els tres valors retornats han de ser enters."""
        data = self._make_data([1, 2], [0, 1])
        home, away, total = fun_total_goals(data)
        assert isinstance(home, int)
        assert isinstance(away, int)
        assert isinstance(total, int)

    def test_correct_values(self) -> None:
        """Comprova que els valors calculats siguin correctes."""
        data = self._make_data([3, 2, 0], [1, 1, 2])
        home, away, total = fun_total_goals(data)
        assert home == 5
        assert away == 4
        assert total == 9

    def test_total_equals_home_plus_away(self) -> None:
        """El total ha de ser igual a la suma de locals i visitants."""
        data = self._make_data([1, 0, 3], [2, 1, 0])
        home, away, total = fun_total_goals(data)
        assert total == home + away

    def test_zero_goals(self) -> None:
        """Amb tots els gols a zero, els tres valors han de ser 0."""
        data = self._make_data([0, 0], [0, 0])
        home, away, total = fun_total_goals(data)
        assert home == 0
        assert away == 0
        assert total == 0

    def test_single_row(self) -> None:
        """Prova amb un únic registre."""
        data = self._make_data([4], [2])
        home, away, total = fun_total_goals(data)
        assert home == 4
        assert away == 2
        assert total == 6
