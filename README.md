# Metodika pro objektivní srovnání DataOps nástrojů

Diplomová práce implementující metodiku pro hodnocení DataOps platforem pomocí vícekriteriální rozhodovací analýzy (TOPSIS).

## Struktura projektu

```
├── thesis/                          Diplomová práce
│   └── diploma_thesis.pdf          Finální PDF práce (doplnit před odevzdáním)
│
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
├── QUICKSTART.md                    Rychlý start
├── TODO.md                          Co zbývá doplnit
└── LICENSE                          MIT License
```

### Popis složek

**thesis/** - Kompletní text diplomové práce ve formátu PDF

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

**Hodnoticí rámec:**
- 5 dimenzí (Kvalita dat, Obchodní dopad, Technická efektivita, CI/CD, UX)
- 20 metrik
- 3 platformy (Keboola, Microsoft Fabric, Databricks)

**Metoda:** TOPSIS (vícekriteriální rozhodovací analýza)

## Rychlý start

### Lokální spuštění

```bash
cd app
pip install -r requirements.txt
streamlit run app.py
```

Aplikace se otevře na `http://localhost:8501`

### Hostování a sdílení

Aplikace je připravena pro hosting na Streamlit Cloud. Každý uživatel má svou vlastní session - data se nepřekrývají.

Viz `HOSTING.md` pro detailní návod na nasazení.

### Struktura aplikace

- **Režim 1**: Průměrné váhy z výzkumu (rychlé hodnocení)
- **Režim 2**: Vlastní kalibrace (přizpůsobené priority)
- **Export**: CSV a PDF zprávy

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

## Co doplnit před odevzdáním

### Kritické
1. **thesis/diploma_thesis.pdf** - Vaše diplomová práce
2. **Osobní informace** - Aktualizovat v tomto README (níže)
3. **research/interviews/transcripts/** - Anonymizované přepisy (min. 3)
4. **research/benchmark/results/** - CSV soubory s naměřenými časy

### Doporučené
5. **research/interviews/calibration.xlsx** - Data z kalibračního cvičení
6. **research/benchmark/queries/** - SQL dotazy (nebo odkaz na TPC-H)

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
