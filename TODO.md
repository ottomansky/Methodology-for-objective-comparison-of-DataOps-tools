# Co doplnit před odevzdáním

## KRITICKÉ (musí být)

- [ ] **thesis/diploma_thesis.pdf** - Vaše diplomová práce (finální PDF)
- [ ] **README.md** - Doplnit váš email (řádek 136)
- [ ] **research/interviews/interviews_before/** - Min. 3 anonymizované přepisy rozhovorů před vytvořením metodiky
- [ ] **research/interviews/interviews_after/** - Min. 3 přepisy validačních rozhovorů po vytvoření metodiky
- [ ] **research/benchmark/queries/** - Doplnit zbývající TPC-H SQL dotazy (query_02.sql - query_22.sql)
- [ ] **research/research_summary.md** - Doplnit rešerši technických schopností platforem

## DŮLEŽITÉ (doporučeno)

- [ ] **app/data/platform_scores.csv** - Zkontrolovat a případně upravit hodnocení platforem
- [ ] **app/data/weights.csv** - Zkontrolovat průměrné váhy z rozhovorů

## Kontrola před odevzdáním

```bash
# Zkontrolujte placeholder texty
grep -r "\[název univerzity\]" .
grep -r "\[jméno vedoucího\]" .

# Otestujte aplikaci
cd app
streamlit run app.py

# Zkontrolujte strukturu
tree -L 2
```

## Odhad času

- Doplnění osobních info: 10 minut
- Nahrání přepisů a dat: 1-2 hodiny
- Finální kontrola: 30 minut

**Celkem: 2-3 hodiny čisté práce**

