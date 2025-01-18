import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.ex2 import name_surname, elimina_no_participants, recuperar_dorsals

class TestEx1(unittest.TestCase):
    def setUp(self):
        """
        Es fa un df per poder aplicar les funcions
        """
        self.df = pd.DataFrame({
            "biker": ["Clara Ferrer", "Laura Dayde-Crea", "Rassil Houli"],
            "time": ["00:00:00", "01:00:45", "02:44:44"],
            "dorsal": [3853, 1000, 2934],
        })


    def test_elimina_no_participants(self):
        """
        Comprova que els participants amb temps "00:00:00" no apareguin al dataset.
        """
        df_filtered = elimina_no_participants(self.df)
        self.assertNotIn("00:00:00", df_filtered["time"].values)

    def test_recuperar_dorsals(self):
        """
        Comprova s'obtingui info del participant amb el dorsal especificat.
        """
        df_dorsal = recuperar_dorsals(self.df, dorsal=1000)
        self.assertEqual(df_dorsal.iloc[0]["dorsal"], 1000)

if __name__ == "__main__":
        unittest.main()


