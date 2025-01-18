# PAC Project

Aquest projecte té com a objectiu respondre les preguntes plantejades a la PAC 4, que es divideix en cinc exercicis principals. Cada exercici aborda un conjunt específic de qüestions, treballant amb un conjunt de dades proporcionades per analitzar i processar.

Les dades corresponen a la classificació dels ciclistes que han participat a una prova de ciclisme de muntanya (BTT) anomenada **l'Ormea Montenegros**.

## Funcionalitats del Projecte

El projecte inclou diverses funcionalitats relacionades amb la manipulació de dades i la generació de resultats:

- **Neteja de dades**: Eliminació de valors incorrectes o incomplets.
- **Agrupació de temps**: Organització de temps en franges de 20 minuts.
- **Estandardització de noms**: Neteja i uniformització dels noms dels clubs ciclistes.
- **Generació d'histogrames**: Creació d'histogrames per a la visualització de dades.

Totes aquestes tasques es gestionen de manera estructurada a través de mòduls independents i es validen mitjançant **tests** per garantir un funcionament correcte.

---

## Funcionament del Projecte

### 1. Execució del fitxer `main.py`

El fitxer `main.py` és el punt d'entrada del projecte, des d'on es poden executar totes les funcions dels diferents mòduls. L'usuari pot triar entre:

- Executar un exercici concret (Exercici 1, 2, 3, 4 o 5).
- Executar tots els exercicis a la vegada.


### 2. Descripció dels Exercicis

- **Exercici 1**: 
  - Importa el dataset.
  - Mostra els primers valors.
  - Comptabilitza els participants.
  - Llista les columnes del dataframe.

- **Exercici 2**: 
  - Anonimitza els noms dels participants.
  - Filtra els participants sense temps.
  - Comptabilitza els participants reals.
  - Recupera les dades per dorsal.

- **Exercici 3**: 
  - Agrupa els temps en franges de 20 minuts.
  - Crea un dataframe agrupat.
  - Genera un histograma.

- **Exercici 4**: 
  - Neteja els noms dels clubs ciclistes.
  - Crea una columna amb valors nets.
  - Ordena els clubs pel nombre de participants.

- **Exercici 5**: 
  - Filtra els ciclistes de la UCSC.
  - Troba el millor temps.
  - Calcula la seva posició i el percentatge sobre el total.

---

## Requisits i Dependències

El projecte utilitza les següents llibreries per al tractament de les dades:

- `pandas` per al processament de dades.
- Altres dependències estan especificades al fitxer `requirements.txt`.

El dataset es troba a la ruta: `pac4_project/dataset/dataset.csv`.

---

## Tests

El projecte inclou una sèrie de **tests** utilitzant `unittest` per garantir que les funcions creades es comportin correctament.

Per tal d'executar-ho es pot fer servir:

Per a MacOS
```bash

python3 -m unittest nom_fitxer.py
```

Si no s'utilitza MacOS es pot fer servir:

```bash

python -m unittest nom_fitxer.py
```


## Instal·lació

### 1. Clonar el repositori

Per començar, clona el repositori amb:

```bash
git clone https://github.com/Claraferrer24/PAC4.git
cd PAC4
```

### 2. Crear un entorn virtual
```bash
python3 -m venv venv 
```

### 3. Activar l'entorn virtual

#### Per a Linux/macOS:

```bash
source venv/bin/activate
```

#### Per a Windows (si utilitzes PowerShell):
```bash
# .\venv\Scripts\Activate.ps1
```

### 4. Instal·lar les dependències

```bash
pip install -r requirements.txt
```

