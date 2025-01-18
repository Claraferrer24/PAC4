
from modules.ex1 import importa_dataset, cinc_primers_valors, numero_participants, columnes_df
from modules.ex2 import name_surname, elimina_no_participants, recuperar_dorsals
from modules.ex3 import add_time_grouped, agrupar_time_grouped, save_histogram
from modules.ex4 import clean_club, add_club_clean, ordenar_num_participants
from modules.ex5 import filtrar_ucsc_ciclistes, filtrar_millor_ciclista, get_posicio_percentatge, get_posicio


file_path= "/pac4_project/dataset/dataset.csv"


def exercici_1():
    """
    Funció per resoldre l'Exercici 1.
    - Importació del dataset.
    - Mostrar els 5 primers valors.
    - Comptar el nombre de participants.
    - Mostrar les columnes del dataframe.
    """
    df = importa_dataset(file_path)

    if df is None:
        print("No s'ha pogut carregar el dataset.")
        return

    # 1. Mostrar els 5 primers valors
    print("5 primers valors del dataframe:")
    print(cinc_primers_valors(df))

    # 2. Comptar el nombre de participants
    num_participants = numero_participants(df)
    print(f"\nNombre de participants: {num_participants}")

    # 3. Mostrar les columnes del dataframe
    print("\nColumnes del dataframe:")
    print(columnes_df(df))


def exercici_2():
    """
    Funcio per resoldre exercici 2:
     - s'anonimitzen les dades
     - es veuren els 5 primers valors del dataframe
     - es filtren els ciclistes amb temps 00:00:00
     - es compta el nombre real de participants
     - es recuperen de nou els 5 primers participants
     - es recupera el ciclista amb el dorsal 1000
    """

    df = importa_dataset(file_path)

    if df is None:
        print("No s'ha pogut carregar el dataset.")
        return

    # 1. Anonimitzar els ciclistes (canviar els noms)
    df_anonimitzat = name_surname(df)
    print("\nDataframe amb noms anonimitzats:")
    print(df_anonimitzat.head())

    # 2. Eliminar els ciclistes amb temps "00:00:00"
    df_filtrat = elimina_no_participants(df_anonimitzat)
    print("\nDataframe després d'eliminar ciclistes amb temps '00:00:00':")
    print(df_filtrat.head())

    # 3. Comptar el nombre de ciclistes restants
    num_ciclistes_restants = numero_participants(df_filtrat)
    print(f"\nNombre de ciclistes restants després de l'eliminació: {num_ciclistes_restants}")

    # 4: Recuperar dorsal 1000
    dades_ciclista = recuperar_dorsals(df_filtrat, 1000)
    print(f"\nDades del ciclista amb dorsal 1000:")
    print(dades_ciclista)


def exercici_3():
    """
    Funció per realitzar exercici 3.
    - anàlisi dels temps dels ciclistes per generar franges de 20 minuts creant nova columna
    - agrupar les dades en un nou df
    - generar un histograma i guardar-lo
    """
    # Carregar el dataset
    df = importa_dataset(file_path)

    # Afegir la columna 'time_grouped' amb les franges de 20 minuts
    df_grouped = add_time_grouped(df)

    # Mostrar els 15 primers valors per verificar el resultat de la nova columna
    print("15 primers valors amb la columna 'time_grouped':")
    print(df_grouped.head(15))

    # Agrupar el dataframe per la columna 'time_grouped' i comptar els ciclistes per cada franja
    grouped_df = agrupar_time_grouped(df_grouped)

    # Mostrar els resultats del agrupament
    print("\nResultat de l'agrupament per 'time_grouped':")
    print(grouped_df)

    # Crear i guardar l'histograma
    save_histogram(grouped_df, "img/histograma.png")
    print("\nHistograma guardat a 'img/histograma.png'.")

def exercici_4():
    """
    Funció per realitzar exercici 4.
    - neteja del dataset amb les instruccions donades.
    - es crea unq nova columna amb valors nets.
    - es crea un altre df agrupat i s'ordena segons el num de participants.
    """
    # Carregar el dataset
    df = importa_dataset(file_path)

    if df is None:
        print("No s'ha pogut carregar el dataset.")
        return

    # Afegir columna amb els noms dels clubs netejats
    df_clubs_clean = add_club_clean(df)

    # Mostrar els 15 primers valors per verificar els clubs netejats
    print("\n15 primers valors amb la columna 'club_clean':")
    print(df_clubs_clean.head(15))

    # Agrupar els clubs pel nombre de participants
    df_agrupat = ordenar_num_participants(df_clubs_clean)

    # Mostrar els resultats ordenats (els 10 primers clubs)
    print("\nTop 10 clubs amb més participants:")
    print(df_agrupat.head(10))


def exercici_5():
    """
    Funció per resoldre l'exercici 5:
    - Filtra ciclistes de la UCSC.
    - Troba el ciclista amb millor temps.
    - Determina la posició i percentatge del millor ciclista.
    """

    df = importa_dataset(file_path)

    if df is None:
        print("No s'ha pogut carregar el dataset.")
        return

    # Afegir la columna 'club_clean' utilitzant l'exercici anterior
    df = add_club_clean(df)
    # Filtrem per obterir els ciclistes de la UCSC:
    df_usc = filtrar_ucsc_ciclistes(df)
    # Quin ciclista de la UCSC ha fet millor temps?
    millor_ucsc = filtrar_millor_ciclista(df_usc)
    print(f"\nEl millor ciclista de la UCSC és: {millor_ucsc['biker']}")

    # En quina posició sobre el total ha quedat aquest ciclista,
    posicio_millor_ciclista = get_posicio(df, millor_ucsc)
    print(f"Ha quedat en la posició: {posicio_millor_ciclista} sobre el total.")

    # Quin percentatge sobre el total representa?
    print(f"Això representa un {get_posicio_percentatge(df, posicio_millor_ciclista):.2f}% del total.")



def main():
    """
    Funció principal que coordina l'execució dels diferents exercicis.
    Aquesta funció pot executar tot el codi d'un cop o permetre executar
    els exercicis individualment.
    """
    print("Seleccioneu l'exercici que voleu executar o escriviu 'tots'")
    print("1. Exercici 1")
    # Afegeix opcions per als altres exercicis segons sigui necessari
    print("2. Exercici 2")
    print("3. Exercici 3")
    print("4 Exercici 4")
    print("5. Exercici 5")
    print("6. tots")

    opcio = input("Introduïu el número de l'exercici que voleu executar o si els voleu executar tots a la vegada: ")

    if opcio == "1":
        exercici_1()
    elif opcio == "2":
        exercici_2()
    elif opcio == "3":
        exercici_3()
    elif opcio == "4":
        exercici_4()
    elif opcio == "5":
        exercici_5()
    elif opcio == "tots":
        exercici_1()
        exercici_2()
        exercici_3()
        exercici_4()
        exercici_5()
        pass
    # Afegeix condicions per altres exercicis
    else:
        print("Opció no vàlida. Intenteu-ho de nou.")


if __name__ == "__main__":
    main()
