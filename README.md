# Metodika pro objektivní srovnání DataOps nástrojů

Diplomová práce implementující metodiku pro hodnocení DataOps platforem pomocí vícekriteriální rozhodovací analýzy (TOPSIS).

## 🚀 Live Demo

**Vyzkoušejte aplikaci online:** [https://dataops-comparison-thesis.streamlit.app/](https://dataops-comparison-thesis.streamlit.app/)

Aplikace je nasazená a plně funkční - můžete ji hned použít bez instalace.

## Struktura projektu

```
├── app/                             Webová aplikace (Streamlit)
│   ├── app.py                      Hlavní aplikace
│   ├── requirements.txt            Python závislosti
│   ├── data/                       Data pro hodnocení
│   │   ├── platform_scores.csv    Skóre platforem (1-5)
│   │   ├── weights.csv            Průměrné váhy z výzkumu
│   │   └── metrics.json           Definice 20 metrik
│   └── src/                        Zdrojové kódy
│       ├── topsis.py              TOPSIS algoritmus
│       ├── visualization.py       Grafy (Plotly)
│       ├── data_loader.py         Načítání dat
│       └── export.py              CSV/PDF export
│
├── research/                        Výzkumná data
│   ├── research_summary.md         Rešerše technických schopností platforem
│   ├── interviews/                 Kvalitativní výzkum
│   │   ├── interviews_before/     Přepisy před vytvořením metodiky
│   │   └── interviews_after/      Přepisy po validaci metodiky
│   └── benchmark/                  Kvantitativní měření
│       └── queries/                22 TPC-H SQL dotazů (query_01.sql - query_22.sql)
│
├── README.md                        Dokumentace projektu (tento soubor)
└── LICENSE                          MIT License
```

### Popis složek

**app/** - Funkční webová aplikace implementující TOPSIS metodiku
- Spustitelná lokálně i nasaditelná na Streamlit Cloud
- 2 režimy: průměrné váhy z výzkumu nebo vlastní kalibrace

**research/** - Veškerá data z výzkumu
- `research_summary.md` - Souhrn rešerše technických vlastností platforem
- `interviews_before/` - Rozhovory s experty před finalizací metodiky (zjišťování vah)
- `interviews_after/` - Validační rozhovory po vytvoření metodiky
- `benchmark/queries/` - SQL dotazy TPC-H pro měření výkonu platforem

## O projektu

Tato diplomová práce navrhuje metodiku pro objektivní srovnání DataOps nástrojů. Kombinuje kvalitativní výzkum (rozhovory s odborníky) a kvantitativní měření (benchmark) s implementací interaktivní aplikace.

**Hodnoticí metodika:**
- 5 dimenzí (Kvalita dat, Obchodní dopad, Technická efektivita, CI/CD, UX)
- 20 metrik
- 3 platformy (Keboola, Microsoft Fabric, Databricks)

**Metoda:** TOPSIS (vícekriteriální rozhodovací analýza)

## Rychlý start

### 1. Instalace závislostí

```bash
cd app
pip install -r requirements.txt
```

### 2. Spuštění aplikace

```bash
streamlit run app.py
```

Aplikace se automaticky otevře na `http://localhost:8501`

### 3. Zastavení

V terminálu stiskněte `Ctrl + C`

## Použití aplikace

### Režim 1: Průměrné váhy z výzkumu

1. Klikněte na "Průměrné váhy z výzkumu"
2. Prohlédněte si výsledky a vizualizace
3. Stáhněte CSV nebo PDF export

**Použití:** Rychlé hodnocení pomocí vah zjištěných z expertních rozhovorů. Reprodukuje výsledky diplomové práce.

### Režim 2: Vlastní kalibrace

1. Klikněte na "Vlastní kalibrace"
2. Ohodnoťte každou z 20 metrik na škále 1-5
3. Rozdělte 100 bodů mezi 5 dimenzí podle důležitosti
4. Klikněte na "Vypočítat TOPSIS skóre"
5. Stáhněte výsledky

**Použití:** Přizpůsobení hodnocení specifickým požadavkům vaší organizace.

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

**Aplikace je již nasazená a dostupná zde:** [https://dataops-comparison-thesis.streamlit.app/](https://dataops-comparison-thesis.streamlit.app/)

Pokud chcete nasadit vlastní instanci:

1. Nahrajte projekt na GitHub
2. Jděte na [share.streamlit.io](https://share.streamlit.io/)
3. Připojte GitHub repozitář
4. Nastavte cestu: `app/app.py`
5. Klikněte "Deploy"

**Důležité**: Každý uživatel má svou vlastní session. Data se nepřekrývají.

## Výsledky výzkumu

### Finální pořadí platforem

| Místo | Platforma | TOPSIS skóre |
|-------|-----------|--------------|
| 1. | Databricks | 0.674 |
| 2. | Keboola | 0.551 |
| 3. | Microsoft Fabric | 0.386 |

### Benchmark výkonu (TPC-H, 1GB)

| Platforma | Průměrný čas | Poznámka |
|-----------|--------------|----------|
| Databricks | ~20 min | Nejrychlejší |
| Keboola | ~25 min | Nejstabilnější |
| Microsoft Fabric | ~45 min | Nejpomalejší |

## Výzkumný proces

1. **Kvalitativní fáze**
   - 3 polostrukturované rozhovory s odborníky
   - Kalibrační cvičení pro určení vah
   - Přepisy v `research/interviews/`

2. **Kvantitativní fáze**
   - Hodnocení platforem (1-5 škála)
   - TPC-H benchmark (22 dotazů)
   - Data v `research/benchmark/`

3. **Analýza a validace**
   - Aplikace TOPSIS metody
   - Validace s respondenty

## Technologie

- **Python 3.8+**
- **Streamlit** - webový framework
- **Pandas, NumPy** - zpracování dat
- **Plotly** - interaktivní grafy
- **ReportLab** - PDF export

## Použití metodiky

### Pro studenty
- Příklad vícekriteriálního rozhodování
- Šablona pro podobný výzkum

### Pro organizace
- Objektivní srovnání DataOps platforem
- Přizpůsobení vah vlastním prioritám

### Pro konzultanty
- Strukturovaný přístup k vendor selection
- Podklady pro doporučení

## Citace

```bibtex
@mastersthesis{dataops_comparison_2025,
  author = {Maxmilián Ottomanský},
  title = {Metodika pro objektivní porovnávání DataOps nástrojů},
  school = {Vysoká škola ekonomická v Praze, Fakulta informatiky a statistiky},
  year = {2025},
  type = {Diplomová práce},
  program = {Data a analytika pro business}
}
```

## Kontakt

**Autor**: Bc. Maxmilián Ottomanský  
**Email**: [doplňte váš email]  
**Univerzita**: Vysoká škola ekonomická v Praze  
**Fakulta**: Fakulta informatiky a statistiky  
**Vedoucí práce**: Ing. Karel Maršálek

## Licence

MIT License - projekt je volně dostupný pro akademické i komerční použití.

---

**Poznámka**: Tento repozitář obsahuje kompletní implementaci diplomové práce včetně funkční webové aplikace, výzkumných materiálů a dokumentace.
