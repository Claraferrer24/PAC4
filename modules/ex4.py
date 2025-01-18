import re

def clean_club(club):
    """
    Rep un club i ens retorna el club amb els valors netejats.
    :param club: Nom del club a netjar
    :return: club amb un nom estandar (net)
    """

    club=club.strip().upper()

    paraules_eliminar = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ',
        'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
        'CLUB CICLISTA ', 'CLUB ']
    for term in paraules_eliminar:
        club = club.replace(term, "")
    club = re.sub(
        r'^(C.C\. |C.C |CC |C.D\. |C.D |CD |A.C\. |A.C |AC |A.D\. |A.D |AD |A.E\. |A.E |AE |E.C\. |E.C |EC |S.C\. |S.C |SC |S.D\. |S.D |SD )',
        '', club)
    club = re.sub(
        r'( T\.T\.| T\.T| TT| T\.E\.| T\.E| TE| C\.C\.| C\.C| CC| C\.D\.| C\.D| CD| A\.D\.| A\.D| AD| A\.C\.| A\.C| AC)$',
        '', club)

    return club

def add_club_clean(df):
    """
    Afegeix una columna nova "club_clean" al df, on s'indica el club un cop s'ha aplicat la funció clean_club
    :param df: df original amb la columna 'club'.
    :return: df amb la nova columna 'club_clean'.
    """
    df["club_clean"]=df["club"].apply(clean_club)
    return df

def ordenar_num_participants(df):
    """
    Ordena els clubs ciclistes pel número de participants, en ordre descendent.

    :param df: df amb les dades dels participants, incloent la columna "clean_club".
    :return: df amb el nombre de participants per club, ordenat de manera descendent.
    """

    df_agrupat = df.groupby("club_clean").size().reset_index(name="Num participants")
    df_agrupat = df_agrupat.sort_values("Num participants", ascending=False)

    return df_agrupat

    return df_agrupat