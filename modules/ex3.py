import matplotlib.pyplot as plt

def minutes_002040(hora):

    """
    Agrupa un valor de temps (hh:mm:ss) en franges de 20 minuts.
    :param hora: Temps en format hh:mm:ss
    :return: Temps agrupat en format hh:mm (on mm pot ser:00, 20 o 40).
    """
    hora, min, seg= map(int,hora.split(":"))

    if min<20:
        min="00"
    elif min<40:
        min="20"
    elif min<=59:
        min="40"

    time=f"{hora:02d}:{min}"
    return time

def add_time_grouped(df):
    """
    Afegeix una columna nova "time_grouped" al df. La columna agrupa els temps en franges de 20 minuts.
    :param df: df original amb la columna 'time' en format hh:mm:ss.
    :return: df amb la nova columna 'time_grouped'.
    """
    df["time_grouped"]=df["time"].apply(minutes_002040)
    return df

def agrupar_time_grouped(df):
    """
    Agrupa el df per la columna 'time_grouped' i compta els ciclistes en cada franja.
    :param df: df amb la columna 'time_grouped'.
    :return: df amb les franges de temps i el número de ciclistes.
    """

    df_agrupada=df.groupby("time_grouped").size().reset_index(name="Número Ciclistes")
    return df_agrupada

def save_histogram(grouped_df, output_path="img/histograma.png"):
    """
    Fa i guarda un histograma a partir d'un df ja agrupat segons el temps.
    :param grouped_df: df amb les franges de temps ("time_grouped") i el número de ciclistes ("Número Ciclistes").
    :param output_path: path on guardar el fitxer PNG de l'histograma.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_df['time_grouped'], grouped_df["Número Ciclistes"])
    plt.xlabel("Temps")
    plt.ylabel("Número Ciclistes")
    plt.title("Distribució de ciclistes segons temps")
    plt.xticks(rotation=45)
    plt.savefig(output_path)
    plt.close()