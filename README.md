# PEC4 – Anàlisi La Liga 1995‑2025

**Alumne:** Jordi Guillem Fragoso
**Assignatura:** Programación para la ciencia de datos - Aula 5 
**Data:** Juny 2026

---

## Descripció del projecte

Anàlisi de les dades històriques de la Lliga espanyola de futbol des de 1995 fins al 2025,
utilizant Python, pandas, matplotlib i networkx. El projecte segueix la guia d'estil PEP 8,
disposa de documentació generada amb pydoc, tests unitaris amb pytest i anàlisi estàtic amb pylint.

---

## Estructura de carpetes

```
PEC4/
├── data/
│   └── LaLiga_Matches.csv          # Dataset original
├── doc/                            # Documentació generada per pydoc
├── img/                            # Gràfiques generades per cada exercici
├── screenshots/                    # Captures de pantalla (autoria, linting, tests)
├── src/
│   ├── config.py                   # Variables globals (nom_alumne, date_time)
│   ├── main.py                     # Punt d'entrada principal
│   └── exercises/
│       ├── __init__.py
│       ├── ex1.py                  # Exercici 1: EDA
│       ├── ex2.py                  # Exercici 2: Partits per equip
│       ├── ex3.py                  # Exercici 3: Distribució de gols
│       ├── ex4.py                  # Exercici 4: FTR
│       ├── ex5.py                  # Exercici 5: Punts acumulats
│       ├── ex6.py                  # Exercici 6: Resum i pòdium
│       └── ex7.py                  # Exercici 7: Graf networkx
├── tests/
│   └── tests_ex6.py                # Tests de fun_total_goals (exercici 6)
├── .pylintrc                       # Configuració de Pylint
├── LICENSE                         # Llicència MIT
├── README.md                       # Aquest fitxer
└── requirements.txt                # Dependències del projecte
```

---

## Instal·lació

### 1. Crea i activa un entorn virtual net

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instal·la les dependències

```bash
pip install -r requirements.txt
```

---

## Execució del projecte

Des de la carpeta arrel del projecte:

```bash
# Ajuda
python src/main.py -h

# Executa tots els exercicis (1‑7)
python src/main.py -ex 7

# Executa només els exercicis 1 al 5
python src/main.py -ex 5

# Executa només el primer exercici
python src/main.py -ex 1
```

> Les gràfiques es guarden automàticament a `img/` amb el nom definit a l'arxiu config.py i un timestamp.

---

## Anàlisi estàtic del codi (Linting)

S'utilitza **pylint** amb la configuració `.pylintrc` inclosa al projecte.

```bash
# Anàlisi de tots els mòduls
pylint src/config.py src/exercises/ex1.py src/exercises/ex2.py \
       src/exercises/ex3.py src/exercises/ex4.py src/exercises/ex5.py \
       src/exercises/ex6.py src/exercises/ex7.py src/main.py

```

> Consulta `screenshots/` per veure el resultat del linting amb el nom de l'alumne visible.

---

## Generació de documentació

S'utilitza **pydoc** per generar la documentació HTML a `doc/`.

```bash
# Instal·la pydoc (inclòs a la llibreria estàndard de Python)
# Genera la documentació de tots els mòduls
python -m pydoc -w src.config
python -m pydoc -w src.exercises.ex1
python -m pydoc -w src.exercises.ex2
python -m pydoc -w src.exercises.ex3
python -m pydoc -w src.exercises.ex4
python -m pydoc -w src.exercises.ex5
python -m pydoc -w src.exercises.ex6
python -m pydoc -w src.exercises.ex7
python -m pydoc -w src.main

# Mou els .html generats a la carpeta doc/
mv *.html doc/
```

> Consulta `screenshots/` per veure la documentació generada amb el nom de l'alumne visible.

---

## Execució dels tests

S'utilitza **pytest**:

```bash
# Executa els tests
python -m pytest tests/tests_ex6.py -v

```

> Consulta `screenshots/` per veure la captura dels tests passant correctament.

---

## Publicació a GitHub

```bash
# Inicialitza el repositori (primera vegada)
git init
git add .
git commit -m "PEC4: anàlisi La Liga 1995-2025"

# Connecta amb el repositori remot i puja els canvis
git remote add origin https://github.com/<usuari>/<repositori>.git
git branch -M main
git push -u origin main
```

# Vaig afegir la carpeta .venv i __pycache__ al .gitignore per tal de no pujar-les a GitHub.

---

## Llicència

Distribuït sota la llicència **MIT**. Consulta el fitxer [LICENSE](LICENSE) per a més informació.
