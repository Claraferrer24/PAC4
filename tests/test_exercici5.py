import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.ex5 import (
    filtrar_ucsc_ciclistes,
    filtrar_millor_ciclista,
    get_posicio,
    get_posicio_percentatge
)
from modules.ex4 import add_club_clean


class TestExercici5(unittest.TestCase):

    def setUp(self):
        """
        Es fa un df per poder aplicar les funcions
        """
        self.df = pd.DataFrame({
            "dorsal": [101, 102, 103, 104, 105],
            "club": [
                "UCSC ",
                "Club Ciclista Martorell",
                "UCSC ",
                "Club Ciclista Martorell",
                "UCSC "
            ],
            "time": ["01:15:00", "00:45:30", "01:05:45", "00:50:15", "00:42:10"],
            "biker": ["Clara Ferrer", "Laura Dayde", "Rassil Houli", "Ale Gonzalez", "Joan Dausa"]
        })
        self.df = add_club_clean(self.df)  # Apliquem el 'club_clean'

    def test_filtrar_ucsc_ciclistes(self):
        """
        Comprova que al df només apareguin ciclistes de la UCSC.
        """
        df_ucsc = filtrar_ucsc_ciclistes(self.df)
        self.assertTrue(all(df_ucsc["club_clean"] == "UCSC"))

    def test_filtrar_millor_ciclista(self):
        """
        Comprova que es retorni el ciclista amb el millor temps.
        """
        millor_ciclista = filtrar_millor_ciclista(self.df)
        self.assertEqual(millor_ciclista["biker"], "Joan Dausa")
        self.assertEqual(str(millor_ciclista["time"]), "0 days 00:42:10")

    def test_get_posicio(self):
        """
        Comprova que es calculi correctament la posició del millor ciclista.
        """
        millor_ciclista = filtrar_millor_ciclista(self.df)
        posicio = get_posicio(self.df, millor_ciclista)
        self.assertEqual(posicio, 5)

    def test_get_posicio_percentatge(self):
        """
        Comprova que es calculi correctament el percentatge de posició del millor ciclista.
        """
        millor_ciclista = filtrar_millor_ciclista(self.df)
        posicio = get_posicio(self.df, millor_ciclista)
        percentatge = get_posicio_percentatge(self.df, posicio)
        self.assertAlmostEqual(percentatge, 100.0, places=2)


if __name__ == "__main__":
    unittest.main()
