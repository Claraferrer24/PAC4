import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.ex4 import clean_club, add_club_clean, ordenar_num_participants


class TestExercici4(unittest.TestCase):

    def setUp(self):
        """
        Es fa un df per poder aplicar les funcions
        """
        self.df = pd.DataFrame({
            "club": [
                "PENYA CICLISTA ANEM A FER BICI",
                "CLUB CICLISTA GIRONA",
                "AGRUPACIÓ CICLISTA TARRAGONA",
                "C.C. BARCELONA",
                "S.C. VILAFRANCA",
                "CLUB BARCELONA",
                "PENYA CICLISTA MARTORELL",
                "CLUB CICLISTA MARTORELL"
            ]
        })

    def test_clean_club(self):
        """
        Comprova que la funció `clean_club` netegi correctament els noms dels clubs.
        """
        self.assertEqual(clean_club("PENYA CICLISTA ANEM A FER BICI"), "ANEM A FER BICI")
        self.assertEqual(clean_club("CLUB CICLISTA GIRONA"), "GIRONA")
        self.assertEqual(clean_club("AGRUPACIÓ CICLISTA TARRAGONA"), "TARRAGONA")
        self.assertEqual(clean_club("C.C. BARCELONA"), "BARCELONA")
        self.assertEqual(clean_club("S.C. VILAFRANCA"), "VILAFRANCA")
        self.assertEqual(clean_club("CLUB BARCELONA"), "BARCELONA")
        self.assertEqual(clean_club("PENYA CICLISTA MARTORELL"), "MARTORELL")
        self.assertEqual(clean_club("CLUB CICLISTA MARTORELL"), "MARTORELL")

    def test_add_club_clean(self):
        """
        Comprova que la funció `add_club_clean` afegeixi correctament la columna 'club_clean'.
        """
        df_cleaned = add_club_clean(self.df)
        self.assertIn("club_clean", df_cleaned.columns)

    def test_ordenar_num_participants(self):
        """
        Comprova que la funció `ordenar_num_participants`
        ordeni els clubs per nombre de participants després de comptar.
        """
        df_cleaned = add_club_clean(self.df)
        df_sorted = ordenar_num_participants(df_cleaned)
        self.assertEqual(df_sorted.iloc[0]["club_clean"], "BARCELONA")
        self.assertEqual(df_sorted.iloc[0]["Num participants"], 2)
        self.assertEqual(df_sorted.iloc[1]["club_clean"], "MARTORELL")
        self.assertEqual(df_sorted.iloc[1]["Num participants"], 2)
        self.assertEqual(df_sorted.iloc[2]["club_clean"], "ANEM A FER BICI")
        self.assertEqual(df_sorted.iloc[2]["Num participants"], 1)
        self.assertEqual(df_sorted.iloc[3]["club_clean"], "GIRONA")
        self.assertEqual(df_sorted.iloc[3]["Num participants"], 1)
        self.assertEqual(df_sorted.iloc[4]["club_clean"], "TARRAGONA")
        self.assertEqual(df_sorted.iloc[4]["Num participants"], 1)

if __name__ == "__main__":
    unittest.main()
