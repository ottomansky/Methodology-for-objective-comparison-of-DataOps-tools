# TRANSKRIPT ROZHOVORU - RESPONDENT 03
**Datum:** Říjen 2025  
**Platforma:** Videohovor (Google Meet)  
**Délka:** 42 minut  
**Jazyk:** Čeština  
## Účastníci
- **Tazatel:** Výzkumník (diplomová práce VŠE)
- **Respondent 03:** Anonymizovaný odborník z praxe
## Demografické údaje respondenta
**Role:** Datový konzultant (freelance)  
**Délka praxe:** 10+ let  
**Oblast působení:** SMB segment, český i mezinárodní trh  
**Zkušenosti s platformami:** Keboola (8+ let), Microsoft Stack (4+ let), Databricks (1+ rok), Modern Data Stack (5+ let)  
**Typ projektů:** AWS/GCP/Azure implementace, all-in-one platformy, konzultace výběru DataOps nástrojů
## ROZHOVOR
### Úvod a informovaný souhlas
**Tazatel:** Dobrý den, děkuji, že jste si našel čas na tento rozhovor. Rozhovor budu nahrávat pro účely transkriptu, který bude součástí mé diplomové práce. Všechny údaje budou anonymizovány. Souhlasíte s nahráváním a zpracováním odpovědí pro akademické účely?
**Respondent 03:** Ano, souhlasím.
**Tazatel:** Výborně. Rozhovor bude strukturovaný do několika tematických okruhů. U každého okruhu vás nejprve poprosím o otevřené odpovědi a na závěr o hodnocení několika metrik na škále 1 až 5, kde 1 znamená "nice to have" a 5 znamená "kriticky důležité". Pokud vám některá otázka nebude připadat relevantní, klidně to zmíníte. Můžeme začít?
**Respondent 03:** Samozřejmě, můžeme.

### C0. Představení respondenta
**Tazatel:** Pro kontext bych vás poprosil o krátké představení. Jakou roli zastáváte a jak dlouho se této práci věnujete?
**Respondent 03:** Pracuji jako freelance datový konzultant, věnuji se tomu přes deset let. Specializuji se hlavně na projekty pro malé a střední firmy, ale občas pracuji i na větších implementacích. Pomáhám firmám s výběrem a implementací datových platforem a nastavením jejich datové strategie.
**Tazatel:** S jakými platformami máte praktickou zkušenost?
**Respondent 03:** Nejdelší zkušenost mám s Kebulou, tam je to asi osm let. Microsoft stack znám asi čtyři roky, především Power BI a Azure služby. S Databricks jsem pracoval zhruba rok na jednom větším projektu. Kromě toho mám zkušenosti s různými nástroji z Modern Data Stack ekosystému, to je asi pět let.
**Tazatel:** To je velmi dobrý přehled napříč různými přístupy. Pracujete převážně na českém trhu?
**Respondent 03:** Ano, většinou ano, ale mám i několik zahraničních klientů. Primárně se zaměřuji na SMB segment, kde pomáhám firmám nastavit datové procesy od začátku nebo zmodernizovat stávající řešení.

### C1. Definice úspěchu DataOps implementace
**Tazatel:** První tematická otázka se týká definice úspěchu. Co je pro vás úspěch DataOps implementace? Podle čeho poznáte, že platforma funguje správně?
**Respondent 03:** Pro mě je klíčové, když se podaří vytvořit prostředí, kde spolu skutečně spolupracují business lidé a technické týmy. Nejde jen o to mít funkční pipeline nebo hezké dashboardy. Jde o to, že obchodní strana rozumí datům, umí je používat a zároveň dodržujeme governance pravidla.
Úspěch je, když analytik dokáže sám vytvořit novou metriku nebo report, aniž by musel čekat týden na data inženýra. Zároveň když data inženýr nemusí řešit každý drobný požadavek, ale může se věnovat složitějším věcem. A v tom celém musí být jasné, odkud data pocházejí, jak jsou zpracovaná a kdo k nim má přístup.
**Tazatel:** To znamená, že pro vás je governance součástí definice úspěchu, ne něco, co se řeší až následně?
**Respondent 03:** Přesně tak. Governance není overhead, je to základ. Pokud nemáte jasná pravidla, kdo co smí, jak se data validují a jak se verzují změny, pak to dlouhodobě nefunguje. Můžete mít sebevíc výkonnou platformu, ale pokud lidi nevěří datům nebo nevědí, jak s nimi pracovat, tak to není úspěch.

### C2. Technická efektivita a spolehlivost
**Tazatel:** Přejdeme k technické efektivitě. Jaké metriky nebo signály v praxi nejlépe vystihují rychlost a stabilitu data pipeline?
**Respondent 03:** U mě jsou dvě hlavní věci, které sleduji pořád. První je fail rate – kolik běhů selže. To je pro mě absolutní priorita. Pokud máte pipeline, která párkrát týdně spadne, tak to zabíjí důvěru uživatelů. Oni pak začnou obcházet systém, dělají si vlastní excely a celý smysl centrální platformy se rozpadá.
Druhá věc je variabilita runtime. Pokud pipeline jeden den běží deset minut a druhý den hodinu, je s tím něco špatně. Chci, aby runtime byl předvídatelný, aby byl rozdíl maximálně dvacet procent. To mi dává jistotu, že systém je stabilní a že v tom nejsou nějaké skryté problémy.
**Tazatel:** A co rychlost samotná? Nezaměřujete se na to, jak rychle pipeline běží?
**Respondent 03:** Záleží na kontextu. Samozřejmě nechci, aby pipeline běžela zbytečně dlouho, ale rychlost sama o sobě není priorita. Pokud mám stabilní běh, který trvá třeba půl hodiny, a vím, že to bude pořád půl hodiny, tak to je lepší než nestabilní běh, který jednou trvá pět minut a podruhé spadne.
**Tazatel:** Co typicky bývají bottlenecky v těch projektech, se kterými pracujete?
**Respondent 03:** Téměř vždycky jde o závislosti na třetích stranách. API volání, přístup do databází, externí systémy. Tam nemáte kontrolu nad výkonem. Můžete mít sebelepší platformu, ale pokud čekáte na odpověď z nějakého pomalého API třetí strany, tak to prostě trvá.
Řešíme to různě – někdy cachováním, někdy asynchronním zpracováním, někdy prostě musíte klientovi říct, že to rychlejší nebude, dokud se nevyřeší ten externí systém.
**Tazatel:** Děkuji. Nyní bych vás poprosil o hodnocení na škále 1 až 5, kde 5 je kriticky důležité. První metrika je rychlost – nízká latence.
**Respondent 03:** Tři.
**Tazatel:** Stabilita – uptime, spolehlivost.
**Respondent 03:** Jednoznačně pět. To je nejdůležitější.
**Tazatel:** Škálovatelnost.
**Respondent 03:** Čtyři. Je to důležité, ale ne tak kritické jako stabilita.
**Tazatel:** A observabilita – monitoring, možnost debugovat.
**Respondent 03:** Také čtyři. Bez toho těžko řešíte problémy.

### C3. Kvalita dat a governance
**Tazatel:** Další oblast je kvalita dat a governance. Co považujete za minimum funkcí, aby platforma obstála v auditu nebo compliance review?
**Respondent 03:** Musí být možné spustit pipeline znovu a dostat stejný výsledek. Reprodukovatelnost je základ. Pak potřebuji generované artefakty – logy, výstupy, aby bylo jasné, co přesně se stalo v každém běhu.
Dále musí být jasně definovaný lineage – odkud data přišla, jak byla zpracovaná, kam šla dál. A samozřejmě historie změn verzí. Když někdo něco změnil, musím vidět co, kdy a kdo to udělal.
**Tazatel:** Jakou úroveň lineage považujete za nutnou? Stačí table-level nebo je potřeba column-level?
**Respondent 03:** Závisí na případu. Pro běžné situace stačí table-level, abych viděl tok mezi tabulkami. Column-level je hezké mít, ale není to často nutné. Spíš je to nice to have.
**Tazatel:** Jak prakticky zavádíte testy kvality dat?
**Respondent 03:** Začínáme od základů. Validace schématu – explicitní výběr sloupců, které očekáváme. Kontrola datových typů, případně přetypování s chybovým hlášením, pokud to nejde. Pak ad-hoc kontroly konzistence, kontrolní součty.
Nesnažíme se hned vytvořit stoprocentní pokrytí všech možných chyb. Začneme od toho, co se nejčastěji pokazí, a postupně přidáváme další testy podle toho, co se v praxi objevuje.
**Tazatel:** Hodnocení. Jak důležitý je pro vás lineage?
**Respondent 03:** Pět. Naprosto kritické.
**Tazatel:** Data quality testy.
**Respondent 03:** Také pět. Bez testů nemáte kvalitní data.
**Tazatel:** Řízení přístupů – RBAC nebo ABAC.
**Respondent 03:** Tři. Je to důležité, ale ne tak kritické jako kvalita dat samotných.
**Tazatel:** Data katalog.
**Respondent 03:** Tři. Hezké mít, ale nejde to před kvalitu dat.
**Tazatel:** Metadata management obecně.
**Respondent 03:** To už je pro mě pět. Metadata jsou kritická pro pochopení dat.

### C4. Automatizace, verzování a CI/CD
**Tazatel:** Jak ve vaší praxi vypadá dobré CI/CD pro data? Můžete popsat větve, prostředí, promotion, rollbacky?
**Respondent 03:** Dobré CI/CD znamená úplnou kontrolu nad release managementem. Musí být automatické verzování všech změn, ideálně s rolovou strukturou, kdo co smí nasazovat.
Klíčové je, aby rollback byl jednoduchý. Ideálně na jedno kliknutí se dokážete vrátit o několik verzí zpátky. Ne jen o jednu, ale klidně o pět verzí, pokud zjistíte, že problém vznikl dávno a postupně se zhoršoval.
**Tazatel:** Jaké jsou konkrétní situace, kdy vám platforma práci s CI/CD usnadnila?
**Respondent 03:** Když můžete dělat hromadné změny konfigurace programově přes kód a pak to celé nasadit najednou s kontrolou verzí. Představte si, že potřebujete změnit nastavení v padesáti pipeline najednou. Pokud to dokážete udělat skriptem a následně to verzovat a nasadit, tak to je obrovská úspora času.
**Tazatel:** A kdy to naopak komplikuje?
**Respondent 03:** Hot fix release management. Když potřebujete rychle opravit kritickou chybu v produkci, ale máte nastavený složitý schvalovací proces s několika prostředími. Pak se snažíte najít způsob, jak proces obejít, a to vždycky vede k problémům.
Dobrá platforma musí mít možnost nějaké emergency deployment, které obejde standardní proces, ale pořád je to zalogované a verzované.
**Tazatel:** Hodnocení. Git integrace.
**Respondent 03:** Tři. Je to důležité, ale ne kritické, pokud existuje alternativní způsob verzování.
**Tazatel:** API nebo CLI pro automatizaci.
**Respondent 03:** Pět. Bez toho nejde dělat pořádná automatizace.
**Tazatel:** Automatizované testy.
**Respondent 03:** Čtyři. Velmi důležité, ale dají se dělat i manuálně, pokud je to nutné.
**Tazatel:** Reprodukovatelnost běhů – deterministické pipeline.
**Respondent 03:** Čtyři. Podobně jako testy – velmi důležité pro stabilitu.

### C5. Uživatelská přívětivost a spolupráce
**Tazatel:** Kde vidíte přínos no-code versus pro-code přístupů? Jak ovlivňují produktivitu týmu?
**Respondent 03:** No-code přístupy pozitivně přispívají k demokratizaci dat. Snižují bariéru vstupu pro lidi, kteří nejsou programátoři, ale potřebují pracovat s daty. To výrazně zvyšuje rychlost vývoje v mnoha případech.
Když má obchodní analytik možnost vytvořit si vlastní transformaci bez toho, aby musel čekat na data inženýra, který mu to naprogramuje, tak se věci dějí rychleji. Samozřejmě jsou situace, kde potřebujete plnohodnotný kód – složité transformace, ML modely, integrace s externími systémy. Tam je pro-code nutný.
Ideální je hybridní přístup, kdy máte možnost začít v no-code prostředí a když narazíte na limity, tak přejít do kódu.
**Tazatel:** Co vám nejvíc pomáhá při ladění a incident response?
**Respondent 03:** Komplexní logování všech událostí. Musím vidět, co se přesně stalo v každém kroku. Pak alerting – automatické upozornění, když něco selže nebo se chová neobvykle.
Někdy vytváříme i QA dashboardy speciálně na sledování kritických metrik dat – počty řádků, kontrolní součty, distribuce hodnot. To nám pomáhá zachytit problémy dřív, než si jich všimnou uživatelé.
**Tazatel:** Hodnocení. Jak důležitá je jednoduchost onboardingu?
**Respondent 03:** Tři. Je to důležité, ale zkušený tým se naučí pracovat s čímkoliv.
**Tazatel:** Dokumentace.
**Respondent 03:** Čtyři. Velmi důležité, hlavně při předávání projektů.
**Tazatel:** Debugging tools.
**Respondent 03:** Také čtyři. Bez toho těžko řešíte problémy.
**Tazatel:** Sdílení artefaktů – možnost spolupráce více lidí.
**Respondent 03:** Pět. To je kritické pro týmovou práci.

### C6. Business dopad a ekonomika
**Tazatel:** Jak v praxi posuzujete celkový náklad vlastnictví – TCO?
**Respondent 03:** Dívám se na tři až pětileté období. Není to jen o licencích a výpočetních nákladech. Musíte počítat s lidskými zdroji – kolik lidí potřebujete na provoz, jak dlouho trvá jejich zaškolení, jaké dovednosti musí mít.
Do toho spadá onboarding nových lidí, ramp-up čas, než jsou produktivní. Na straně technologie pak náklady na běh plus jakékoliv dodatečné licence – třeba pro dodatečné nástroje, které musíte dokoupit, protože platforma sama nestačí.
**Tazatel:** Máte příklady, kdy volba platformy výrazně ovlivnila rychlost doručení hodnoty?
**Respondent 03:** Platformy zaměřené na rychlost dodání, rychlé prototypování a snižování složitosti mají pozitivní dopad na rychlost doručení a získání business hodnoty.
Viděl jsem projekt, kde firma přešla z vlastnoručně sestavené infrastruktury v AWS na integrovanou platformu. Čas od nápadu k produkčnímu nasazení se zkrátil z měsíců na týdny. To mělo přímý dopad na business – mohli rychleji reagovat na změny trhu.
Na druhou stranu jsem viděl i opačný případ, kdy firma zvolila příliš komplexní platformu, která sice dokázala všechno, ale tým strávil půl roku jen učením se s ní pracovat.
**Tazatel:** Hodnocení. Time to value – čas do prvního využití.
**Respondent 03:** Pět. Naprosto kritické, zvlášť v SMB segmentu.
**Tazatel:** Total cost of ownership.
**Respondent 03:** Čtyři. Velmi důležité, ale někdy se vyplatí zaplatit víc za rychlejší dodání.
**Tazatel:** Riziko vendor lock-in.
**Respondent 03:** Tři. Je to téma, ale není to dealbreaker.
**Tazatel:** Auditovatelnost.
**Respondent 03:** Čtyři. Důležité pro compliance, ale ne všude stejně kritické.

### C7. Srovnávací pohled na platformy
**Tazatel:** Máte zkušenost s několika platformami. Dokážete stručně popsat, v čem je silná stránka každé z nich a kde naopak narážíte?
**Respondent 03:** Rád. Začnu Kebulou, protože s ní mám nejdelší zkušenost.
**Keboola** – největší síla je nulový time to value. Dokážete velmi rychle postavit něco funkčního. Snižuje komplexitu, snižuje bariéru dovedností pro tým. Prakticky nemusíte spravovat platformu, to dělají oni. To je obrovská výhoda pro menší týmy.
Slabiny se objevují při škálování. Když začnete mít velké objemy dat nebo hodně komplexní použití, narážíte na cenu. Pricing při škálování může být problém. Nedoporučil bych to pro pokročilé AI use case nebo pro real-time zpracování. Na to to není postavené.
**Microsoft Fabric** – síla je v integraci s Power BI a celým Microsoft ekosystémem. Pokud už máte investice do Microsoftu, dává to smysl. Pricing pro Power BI je také výhodný, když to správně nastavíte.
Slabiny – není to zatím feature-complete platforma, některé věci jsou složitější, než by měly být. A komplexita je někdy překvapivá. Nedoporučil bych to firmám, které nejsou v Microsoft ekosystému. Snažit se integrovat Fabric do ne-Microsoft prostředí je bolest.
**Databricks** – obrovská síla je ve výkonu, škálovatelnosti a AI features. Když potřebujete zpracovat velké objemy dat nebo dělat pokročilé ML, Databricks je nejlepší volba.
Slabiny – pricing může být problém, je tam vyšší bariéra dovedností pro tým. Musíte mít lidi, kteří rozumí Sparku. A správa platformy není triviální. Nedoporučil bych to jako platformu pro celofirmovou data demokratizaci. Je to spíš pro datové inženýry a data scientisty než pro business analytiky.
**Tazatel:** To je velmi jasné shrnutí. Je nějaký konkrétní use case, kde byste určitě nedoporučil některou z těchto platforem?
**Respondent 03:** Ano. Keboolu bych nedoporučil pro real-time případy nebo pokročilé AI projekty. Fabric nedávejte firmě, která nemá Microsoft stack. A Databricks není vhodný, pokud chcete, aby s daty pracovali i lidé z byznysu bez technického zázemí.

### C8. Experimentální scénář a objektivní měření
**Tazatel:** Jak byste nastavil férové srovnání těchto platforem? Jaké metriky by se měly měřit a jak zajistit objektivitu?
**Respondent 03:** Vytvořil bych pipeline v různých datových jazycích a měřil je odděleně. SQL transformace měřte zvlášť, Python transformace zvlášť. Pak opakujte zpracování dat po několik dní, abyste viděli variabilitu.
Měřte náklady na běh. Pak zkuste odhadnout čas potřebný k výstavbě – kolik trvá implementovat daný use case. A důležité je i to, jak rychle dokážete najít a opravit chyby – to souvisí s observability.
**Tazatel:** Jaké artefakty by měly být zveřejněny pro replikovatelnost?
**Respondent 03:** Job logy určitě. Pak vyprodukované artefakty – skripty, konfigurace. A důležité jsou data v časových snapshotech – aby bylo jasné, jaká data byla v jakém čase, ideálně s timestampovanými řádky.
Pokud někdo bude chtít experiment zopakovat, musí vidět přesně, co jste dělali, s jakými daty a v jakém pořadí.

### C9. Cokoli důležitého, na co jsme se nezeptali?
**Tazatel:** Je něco důležitého, co jsem vynechal a co by v metodice mělo být?
**Respondent 03:** Ano, dvě věci. První je rozdíl mezi vendor lock-in a people lock-in. Všichni se bojí, že budou zamčení u jednoho dodavatele. Ale je tu i people lock-in – jaká je dostupnost lidí na trhu, kteří umí s platformou pracovat? Kolik stojí najít a udržet lidi, kteří umí spravovat tu platformu?
Můžete mít technicky nejlepší řešení, ale pokud nenajdete lidi, kteří s tím umí pracovat, nebo jsou příliš drazí, tak to není udržitelné.
Druhá věc je data democratization. To není jen buzzword. Je důležité měřit, jak dobře platforma podporuje to, aby s daty mohli pracovat různé role v organizaci, ne jen datový inženýři. To je často klíčové pro úspěch celé implementace.
**Tazatel:** To jsou velmi dobré body. Děkuji.

### C10. Kalibrační cvičení (100 bodů)
**Tazatel:** Poslední část je kalibrační cvičení. Mám pět hlavních dimenzí: technická efektivita, kvalita dat, CI/CD, uživatelská přívětivost a business dopad. Kdybyste měl sto bodů a měl je rozdělit mezi těchto pět částí podle jejich důležitosti, jak byste je rozdělil?
**Respondent 03:** To je zajímavá otázka. Musím chvíli přemýšlet...
Pro mě je kvalita dat naprosto kritická. Bez kvalitních dat nemá smysl nic dalšího. Tomu bych dal třicet bodů.
Business dopad je také velmi důležitý – pro co to celé děláme. Tomu dám dvacet pět bodů.
Technická efektivita je základem stability, tam také dvacet pět bodů.
CI/CD a automatizace jsou důležité pro udržitelnost dlouhodobě. Patnáct bodů.
A uživatelská přívětivost – také důležitá pro adopci – pět bodů. Ne že by nebyla důležitá, ale pokud mám kvalitní data a stabilní systém, tak uživatelé se naučí s tím pracovat.
**Tazatel:** Pro upřesnění – tedy Kvalita dat 30, Business dopad 25, Technická efektivita 25, CI/CD 15 a UX 5 bodů?
**Respondent 03:** Přesně tak.
### Závěr rozhovoru
**Tazatel:** To je ode mě vše. Moc vám děkuji za čas a za velmi podrobné odpovědi.
**Respondent 03:** Není zač. Bylo to zajímavé, rád jsem pomohl.
**Tazatel:** Pošlu vám transkript k autorizaci a případným úpravám. Pokud bude zájem, můžu vás kontaktovat ještě jednou po dokončení experimentů, abych s vámi validoval výsledky.
**Respondent 03:** Určitě, budu rád, když se podívám na výsledky.
**Tazatel:** Děkuji a hezký den.
**Respondent 03:** Také, hodně štěstí s prací.
## ŠKÁLY A KALIBRACE - SOUHRN
### Škály 1-5 (1 = nice to have, 5 = kriticky důležité)
**C2. Technická efektivita:**
- Rychlost/Low Latency: 3
- Stabilita/Uptime: 5
- Škálovatelnost: 4
- Observabilita: 4
**C3. Kvalita dat a governance:**
- Data Lineage: 5
- Data Quality testy: 5
- Access Control (RBAC/ABAC): 3
- Metadata Katalog: 3
- Metadata Management: 5
**C4. CI/CD:**
- Git integrace: 3
- API/CLI: 5
- Automatizované testy: 4
- Reproducibilita běhů: 4
**C5. UX a spolupráce:**
- Onboarding: 3
- Dokumentace: 4
- Debugging tools: 4
- Sdílení artefaktů: 5
**C6. Business dopad:**
- Time to Value: 5
- Total Cost of Ownership: 4
- Vendor Lock-in riziko: 3
- Auditovatelnost: 4
### Kalibrace 100 bodů (C10)
**Rozdělení důležitosti mezi 5 dimenzí:**
- **Kvalita dat:** 30 bodů
- **Business dopad:** 25 bodů
- **Technická efektivita:** 25 bodů
- **CI/CD:** 15 bodů
- **UX:** 5 bodů
*(Poznámka: Respondent zdůraznil, že kvalita dat je naprosto kritická a bez ní nemá smysl nic dalšího. Business dopad a technická efektivita jsou rovnocenně důležité. UX dostal nejméně bodů ne proto, že by nebyl důležitý, ale proto, že ostatní dimenze považuje za kritičtější pro úspěch implementace.)*
**KONEC TRANSKRIPTU**