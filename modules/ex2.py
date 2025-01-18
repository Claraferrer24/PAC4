from faker import Faker
from modules.ex1 import importa_dataset
def name_surname(df):
    """
    Retorna el dataframe amb els noms inventats anglesos.
    :param df: dataframe
    :return: dataframe amb els noms canviats.
    """
    fake=Faker('en_US')
    df["biker"]=[fake.name() for _ in range(len(df))]
    return df


def elimina_no_participants(df):
    """
    Retorna el dataframe sense els participants amb un temps 00:00:00
    :param df: dataframe
    :return: dataframe amb només participants reals.  
    
    """
    df= df[df["time"]!="00:00:00"]
    return df


def recuperar_dorsals(df,dorsal=1000):
    """
    Retorna les dades d'un participant que porta un dorsal concret.

    :param df: dataframe
    :param dorsal: dorsal del participant
    :return: dataframe amb només participants reals.
    """
    return df[df["dorsal"]==1000]

