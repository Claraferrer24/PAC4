PAC PROJECT



Aquest projecte té com a objectiu respondre les preguntes plantejades a la PAC 4, que es divideix en cinc exercicis principals, cadascun amb el seu conjunt de qüestions específiques.

Aquest projecte serveix per analitzar i processar unes dades proporcionades.
Aquestes dades corresponen a la classificació dels ciclistes que han participat a una prova de ciclisme de muntanya (BTT) anomenada l'Ormea Montenegros.

Entre altres funcionalitats, el projecte inclou la neteja de dades, l’agrupació de temps en franges, l’estandardització dels noms dels clubs ciclistes i la generació d’histogrames. Totes aquestes tasques es gestionen de manera estructurada a través de mòduls independents i es validen a través d'una serie de tests per tal d'assegurar un funcionament correcte.


Funcionament del Projecte

1. Execució del main.py:

El fitxer main.py és el fitxer principal del quan s'executen totes les funcions dels diferents mòduls. Per executar-lo, l'usuari pot triar entre:

Executar un exercici concret (Exercici 1, 2, 3, 4 o 5).
Executar tots els exercicis d'una vegada.
L'usuari introdueix una opció al terminal per seleccionar l'acció desitjada. Les opcions disponibles són:

1: Executa l'Exercici 1.
2: Executa l'Exercici 2.
3: Executa l'Exercici 3.
4: Executa l'Exercici 4.
5: Executa l'Exercici 5.
tots: Executa tots els exercicis seqüencialment.

2. Descripció dels exercicis

Exercici 1: Importa el dataset, mostra els primers valors, compta els participants i llista les columnes del dataframe.

Exercici 2: Anonimitza els noms, filtra participants sense temps, compta els participants reals i recupera dades per dorsal.

Exercici 3: Agrupa els temps en franges de 20 minuts, crea un dataframe agrupat i genera un histograma.

Exercici 4: Neteja els noms dels clubs, crea una columna amb valors nets i ordena els clubs pel nombre de participants.

Exercici 5: Filtra ciclistes de la UCSC, troba el millor temps, calcula la seva posició i el percentatge sobre el total.

3. Requisits i dependències

El projecte utilitza llibreries com pandas per al tractament de dades. Les dependències estan especificades al fitxer requirements.txt.
El dataset es troba a la ruta pac_project/dataset/dataset.csv.

4. Tests

Es realitzen alguns tests amb unittest amb el propòsit de garantitzar el bon funcionament de les funcions creades. 