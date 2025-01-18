import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.ex1 import importa_dataset, cinc_primers_valors, numero_participants, columnes_df


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = "/pac4_project/dataset/dataset.csv"
        self.df = importa_dataset(self.file_path)

    def test_importa_dataset(self):
        self.assertIsNotNone(self.df, "El dataset no s'ha carregat correctament.")
        self.assertGreater(len(self.df), 0, "El dataset està buit.")

    def test_cinc_primers_valors(self):
        resultat = cinc_primers_valors(self.df)
        self.assertEqual(len(resultat), 5, "No s'han retornat exactament 5 valors.")

    def test_numero_participants(self):
        num_participants = numero_participants(self.df)
        self.assertGreater(num_participants, 0, "El nombre de participants hauria de ser més gran que 0.")


if __name__ == "__main__":
    unittest.main()