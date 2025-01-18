import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.ex3 import minutes_002040, add_time_grouped, agrupar_time_grouped, save_histogram

class TestExercici3(unittest.TestCase):

    def setUp(self):
        """
        Es fa un df per poder aplicar les funcions
        """
        self.df = pd.DataFrame({
            "time": ["02:15:30", "02:35:00", "02:55:45", "01:10:10", "01:25:30", "01:50:00"],
            "biker": ["Clara Ferrer", "Laura Dayde-crea", "Rassil Houli", "Ale Gonzalez", "Yannick", "Joan Dausa"]
        })
        self.output_path = "test_histograma.png"

    def tearDown(self):
        """
        S'executa després de cada test i eliminar fitxers que creen les funcions.
        """
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_minutes_002040(self):
        """
        Comprova que la funció `minutes_002040` agrupi el temps en franges de 20min.
        """
        self.assertEqual(minutes_002040("00:15:30"), "00:00")
        self.assertEqual(minutes_002040("00:35:00"), "00:20")
        self.assertEqual(minutes_002040("00:55:45"), "00:40")
        self.assertEqual(minutes_002040("01:10:10"), "01:00")
        self.assertEqual(minutes_002040("01:25:30"), "01:20")

    def test_add_time_grouped(self):
        """
        Comprova que la funció `add_time_grouped` afegeixi correctament la columna 'time_grouped'.
        """
        df_grouped = add_time_grouped(self.df)
        self.assertIn("time_grouped", df_grouped.columns)
        expected_groups = ["02:00", "02:20", "02:40", "01:00", "01:20", "01:40"]
        self.assertEqual(df_grouped["time_grouped"].tolist(), expected_groups)

    def test_agrupar_time_grouped(self):
        """
        Comprova que la funció `agrupar_time_grouped` agrupi correctament el DataFrame.
        """
        df_grupada_franges= add_time_grouped(self.df)
        df_agrupada = agrupar_time_grouped(df_grupada_franges)
        self.assertEqual(df_agrupada.iloc[0]["time_grouped"], "01:00")
        self.assertEqual(df_agrupada.iloc[0]["Número Ciclistes"], 1)

    def test_save_histogram(self):
        """
        Comprova que la funció `save_histogram` faci el fitxer

        """
        df_grupada_franges = add_time_grouped(self.df)
        df_agrupada = agrupar_time_grouped(df_grupada_franges)
        save_histogram(df_agrupada, output_path=self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

if __name__ == "__main__":
    unittest.main()
