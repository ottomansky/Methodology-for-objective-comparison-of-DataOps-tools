# Rychlý start

Návod pro spuštění aplikace a práci s projektem.

## Spuštění aplikace

### 1. Instalace závislostí

```bash
cd app
pip install -r requirements.txt
```

### 2. Spuštění

```bash
streamlit run app.py
```

Aplikace se automaticky otevře na `http://localhost:8501`

### 3. Zastavení

V terminálu stiskněte `Ctrl + C`

## Použití aplikace

### Režim 1: Průměrné váhy

1. Klikněte na "Průměrné váhy z výzkumu"
2. Prohlédněte si výsledky a vizualizace
3. Stáhněte CSV nebo PDF export

### Režim 2: Vlastní kalibrace

1. Klikněte na "Vlastní kalibrace"
2. Ohodnoťte každou z 20 metrik (1-5)
3. Rozdělte 100 bodů mezi 5 dimenzí
4. Klikněte na "Vypočítat TOPSIS skóre"
5. Stáhněte výsledky

## Struktura projektu

```
├── thesis/          Diplomová práce (PDF)
├── app/             Webová aplikace
├── research/        Výzkumná data
│   ├── interviews/  Přepisy rozhovorů
│   └── benchmark/   TPC-H výsledky
└── README.md        Dokumentace
```

## Řešení problémů

### Port je obsazený
```bash
streamlit run app.py --server.port 8502
```

### Chyba při importu
```bash
# Zkontrolujte, že jste ve složce app/
cd app
streamlit run app.py
```

### Reinstalace závislostí
```bash
pip install --upgrade -r requirements.txt
```

## Hostování aplikace

### Pro sdílení s ostatními

Aplikace je připravená pro hosting na Streamlit Cloud:

1. Nahrajte projekt na GitHub
2. Jděte na [share.streamlit.io](https://share.streamlit.io/)
3. Připojte GitHub repozitář
4. Nastavte cestu: `app/app.py`
5. Klikněte "Deploy"

**Důležité**: Každý uživatel má svou vlastní session. Data se nepřekrývají.

Detailní návod viz `HOSTING.md`

## Co doplnit

Před odevzdáním práce doplňte:

1. `thesis/diploma_thesis.pdf` - finální PDF práce
2. `research/interviews/interviews_before/` - přepisy rozhovorů (min. 3)
3. `research/interviews/interviews_after/` - validační přepisy (min. 3)
4. `research/benchmark/queries/` - dokončit SQL dotazy (query_02.sql - query_22.sql)
5. `research/research_summary.md` - rešerše platforem
6. `README.md` - váš email
