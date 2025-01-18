import pandas as pd


def importa_dataset(file_path):
    """
    Importa un dataset des d'un fitxer CSV i el retorna com un dataframe.
    :param file_path: Ruta al fitxer CSV.
    :return: DataFrame amb el dataset importat.
    """
    try:
        return pd.read_csv(file_path,sep=";")
    except Exception as e:
        print(f"Error carregant el dataset: {e}")
        return None


def cinc_primers_valors(df):
    """
    Mostra els 5 primers valors del dataframe

    :param df: dataframe a retornar els 5 primers valors
    :return: 5 primers valors del df
    """
    return df.head()

def numero_participants(df):
    """
    Mostra el nombre de participants.
    :param df: dataframe
    :return: el nombre de participants
    """
    return len(df["dorsal"].unique())


def columnes_df(df):
    """
    Mostra les columnes del dataframe.
    :param df: dataframe.
    :return: columnes del dataframe.
    """
    return df.columns