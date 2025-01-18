import pandas as pd
from modules.ex1 import importa_dataset
from modules.ex4 import clean_club, add_club_clean, ordenar_num_participants

def filtrar_ucsc_ciclistes(df):
    """
    Filtra els ciclistes de la Unió Ciclista Sant Cugat (UCSC).
    :param df: df amb les dades dels ciclistes.
    :return: df amb els ciclistes de la UCSC.
    """
    return df[df['club_clean'] == 'UCSC']


def filtrar_millor_ciclista(df):
    """
    Troba el ciclista amb el millor temps.
    :param df: dataframe
    :return: ciclista amb el millor temps.
    """
    df['time'] = pd.to_timedelta(df['time'])
    millor_temps_ciclista = df.loc[df['time'].idxmin()]
    return millor_temps_ciclista

def get_posicio(df, millor_ciclista):
    """
    Obtén la posició del millor ciclista sobre el total i el percentatge sobre el total.
    :param df: DataFrame amb totes les dades dels ciclistes.
    :param millor_ciclista: El millor ciclista amb el millor temps.
    :return: Posició i percentatge sobre el total.
    """
    total_ciclistes = len(df)
    posicio_millor_ciclista = df[df['dorsal'] == millor_ciclista['dorsal']].index[
                                  0] + 1
    return posicio_millor_ciclista

def get_posicio_percentatge(df, posicio_millor_ciclista):
    """
    Obtén la posició del millor ciclista sobre el total i el percentatge sobre el total.
    :param df: DataFrame amb totes les dades dels ciclistes.
    :param millor_ciclista: El millor ciclista amb el millor temps.
    :return: Posició i percentatge sobre el total.
    """
    total_ciclistes = len(df)

    percentatge_total = (posicio_millor_ciclista / total_ciclistes) * 100

    return percentatge_total




#
# file_path= "/Users/claraferrerrodriguez/PycharmProjects/PythonProject/pac_project/dataset/dataset.csv"
# df = importa_dataset(file_path)
# df = add_club_clean(df)
# df_usc=filtrar_ucsc_ciclistes(df)
# millor_ucsc=filtrar_millor_ciclista(df_usc)
# posicio_millor_ciclista=get_posicio(df,millor_ucsc)
# print(posicio_millor_ciclista)
# print(get_posicio_percentatge(df, posicio_millor_ciclista))