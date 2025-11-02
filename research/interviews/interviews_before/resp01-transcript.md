# TRANSKRIPT ROZHOVORU - RESPONDENT 01
**Datum:** 17. října 2025  
**Platforma:** Google Meet  
**Délka:** 54 minut  
**Jazyk:** Čeština  
## Účastníci
- **Tazatel:** Výzkumník (diplomová práce VŠE)
- **Respondent 01:** Anonymizovaný odborník z praxe
## Demografické údaje respondenta
**Role:** Freelance datový konzultant  
**Délka praxe:** 10 let  
**Oblast působení:** Český a mezinárodní trh  
**Zkušenosti s platformami:** Microsoft Fabric, Databricks, Keboola, DIY stacky (AWS, GCP, Azure)  
**Typ projektů:** Digitální transformace, výběr datových platforem, enterprise i SMB klienti
## ROZHOVOR
### Úvod a informovaný souhlas
**Tazatel:** Děkuji, že jste si udělal čas na tento rozhovor. Rozhovor budu nahrávat pro účely transkriptu, který bude součástí mé diplomové práce. Všechny údaje budou anonymizovány. Souhlasíte s nahráváním a zpracováním odpovědí pro akademické účely?
**Respondent 01:** Ano, souhlasím.
**Tazatel:** Výborně. Rozhovor bude strukturovaný do sedmi tematických okruhů, plus jeden závěrečný prostor pro cokoliv, co považujete za důležité doplnit. Hlavní oblasti jsou: definice úspěchu datové implementace, technická efektivita a spolehlivost, kvalita dat a governance, automatizace a CI/CD, uživatelská přívětivost, business dopad a ekonomika, srovnávací pohled na jednotlivé platformy a experimentální scénář. 
U každého okruhu nejprve položím otevřené otázky a na závěr vás požádám o hodnocení několika metrik na škále 1 až 5, kde 1 znamená "nice to have" a 5 znamená "kriticky důležité". Pokud vám některá otázka nebude připadat relevantní k vaší praxi, klidně to zmíníte.
**Respondent 01:** Rozumím. Mám pevný časový limit, v jednu hodinu musím odejít na další schůzku.
**Tazatel:** To by mělo být v pořádku, odhaduji délku na 45-50 minut. Můžeme začít?
**Respondent 01:** Ano.

### C0. Představení respondenta
**Tazatel:** Pro kontext bych vás poprosil o krátké představení. Jakou roli zastáváte a jak dlouho se této práci věnujete?
**Respondent 01:** Jsem freelance datový konzultant a pomáhám zákazníkům převážně na českém, ale i mezinárodním trhu vytvářet strategii pro digitální transformaci, která je často založená na výběru datové platformy umožňující tuto transformaci. V tomto kontextu mám zkušenost s různými datovými platformami jako Microsoft Fabric, Databricks, Keboola, nebo DIY stacky na AWS, GCP nebo Azure cloudu.
**Tazatel:** Jak dlouho se této práci věnuješ?
**Respondent 01:** Deset let.
**Tazatel:** Takže máte zkušenost i s cloudovými providery i s in-house řešeními?
**Respondent 01:** Ano, byl jsem u toho, když začaly vznikat all-in-one platformy nebo mini-in-one platformy – u přerodu ze specializovaných nástrojů do platforem jako takových.

### C1. Definice úspěchu DataOps implementace
**Tazatel:** Přejdeme k první tematické oblasti. Co je pro vás úspěch datové implementace, kde byly aplikovány DataOps principy? Podle čeho posuzujete, že implementace funguje správně?
**Respondent 01:** V ideálním případě by implementace datové platformy měla být cesta, jak dosáhnout nějakého business cíle. Když máš svou víceletou business strategii – může to být růst, expanze, optimalizace nákladů – aby jsi dosáhl té strategie, často potřebuješ projít nějakou formou digitální transformace, která vyžaduje automatizaci a minimalizaci manuální práce. 
Úspěšnost implementace datové platformy je měřená metrikou byznysu. Pro digitální transformaci si vytýčíš metriku – když chceš expandovat, ta metrika je třeba, na kolik nových trhů jsi dokázal expandovat za určité období, nebo o kolik jsi dokázal vyrůst firmu.
Je těžké atribuovat to pouze datové platformě, ale měl bys tam být schopný najít pojítka mezi tím.
Když se na to díváš více technicky nebo budeš hodnotit úspěch týmu, který tu platformu implementuje, tak je to víceméně projektová perspektiva. Máš určený projekt pro implementaci s milestones a časovým začátkem a koncem. Úspěch projektu je, když tyto milestones dodržíš.
Když se budeš dívat na úspěch pouze týmu, který to implementuje, můžeš jim dávat metriky typu onboardování uživatelů, adopce systému, že to reálně uživatelé používají a nedělají to postaru v Excelu. Můžeš mít procento uživatelů pracujících s daty pomocí tvého nástroje do nějaké doby od toho, kdy to prohlásíš za produkci.

### C2. Technická efektivita a spolehlivost
**Tazatel:** Jaké metriky v praxi používáte pro měření efektivity a spolehlivosti data pipeline? Například rychlost, bottlenecky, selhání?
**Respondent 01:** Metriky jsou vždycky důležité v určitém kontextu. Rychlost pipeline – jak dlouho běží datová trubka od ingestování dat přes transformace – může být někdy kritickou metrikou, pokud je to něco, co má běhat ve vysoké frekvenci.
Když je to use case, který každých pět minut musí obnovit data v dashboardu nebo aplikaci, pak je to hlavní metrika. Ve finále se to vždycky překládá do cost-benefit analýzy. Ta platforma v organizaci existuje proto, aby pomáhala dělat business. Jsi ochotný za infrastrukturu a lidi mít nějaký náklad, který by nikdy neměl přesahovat přínos.
Hlavní metrika je, že to musí být ekonomicky rozumné řešení. To se pak může rozpadat do různých konkrétnějších metrik v závislosti na kontextu.
Když máš use case, kde je hlavní potřeba real-time streamovat data, tvoje metrika bude jednak to, že vybrané řešení to umí, že tam je dostatečně nízká latence, že to dokáže zpracovávat určité množství eventů. Budeš sledovat throughput toho streamu.
Je to kontextuální, ale to, co vždycky platí, je cost-benefit pohled. Můžeš ho srovnávat u jednotlivých platforem. Jeden projekt může být náročný na data ingestion, druhý na transformation. Dvě řešení to obě umí dobře, ale jedno ti může být v konkrétním případu levnější, protože i cenové modely se různí.
Ultimátně se vždycky dívám na benefit a náklad na celý provoz.
**Tazatel:** Děkuji. Nyní bych vás poprosil o hodnocení následujících metrik na škále 1 až 5. První je rychlost pipeline.
**Respondent 01:** Dva.
**Tazatel:** Stabilita – uptime.
**Respondent 01:** Pět.
**Tazatel:** Škálování.
**Respondent 01:** Čtyři.
**Tazatel:** A observabilita – možnost sledovat běhy a debugovat.
**Respondent 01:** Čtyři.

### C3. Kvalita dat a governance
**Tazatel:** Další oblast je kvalita dat a governance. Co považujete za minimum funkcionalit, aby platforma obstála v auditu nebo compliance review? Například data lineage, testy kvality.
**Respondent 01:** V různých firmách se liší požadavky na observabilitu a lineage z pohledu auditů.
Typicky když jde o bankovní klienty nebo klienty z kritické infrastruktury, v rámci auditu musí být schopni dokázat přesně, jak byla konkrétní metrika spočítaná. Například když má banka proces, jak schvaluje nebo zamítá úvěry, musí být auditorovi schopni říct, jakým procesem, jakou transformací, jakým modelem byl konkrétní klient zamítnutý nebo schválený. Tam je požadavek kritický.
Pak jsou klienti, u kterých je to spíš pomoc inženýrovi při vývoji, aby se v tom vyznal.
Obecně u funkcionality lineage je důležitý pohled na úrovni objektu – od zdroje dat přes transformace až po konzumaci. Vidět v vizualizaci, že existuje sada reportů, které čtou dataset, že ten dataset přichází z určitého zdroje a prošel určitou cestou.
Někdy bývá hezké, ale ne nutné, vidět úrovně jednotlivých atributů a metrik – sloupce tabulky. To zatím vnímám na většině projektů jako nice to have. Je to spíš něco, co běžně vyžadují vývojáři a data inženýři.
**Tazatel:** Hodnocení na škále 1 až 5. Data lineage.
**Respondent 01:** Tři.
**Tazatel:** Data quality testy.
**Respondent 01:** Pět.
**Tazatel:** Access control – řízení přístupu k datům.
**Respondent 01:** Pět.
**Tazatel:** Metadata katalog.
**Respondent 01:** Tři.

### C4. Automatizace, verzování a CI/CD
**Tazatel:** Jak ve vaší praxi vypadá dobrá implementace CI/CD pro data? Například větve, prostředí, rollbacky?
**Respondent 01:** Tím, že implementujeme projekty pomocí různých platforem, využíváme různé přístupy. Některé platformy tě vedou k určitému způsobu práce. Například Keboola má development branches. Když používáš Databricks, jsi více závislý na vlastním přístupu k DevOps nebo DataOps, kdy typicky využíváš gitové prostředí.
Velmi často už klient používá nějaké svoje řešení, třeba GitLab, tak se používá to řešení, které už mají.
Důležitost je určitě kritická – ne konkrétně v tom mít git, ale mít možnost vyvíjet změny mimo produkční prostředí. Oddělení vývojového prostředí od produkčního je kritické.
Nutnost mít testovací prostředí ještě oddělené od vývojového nevnímám jako tak silnou. Ale určitě to rozdělení dev/prod je nutnost na jakémkoliv projektu.
Mít možnost kontrolovat jednotlivé verze a mít jasný přehled o tom, jaké verze jsou v jakém prostředí nasazené, je nutnost. Mít možnost dělat rozumným způsobem rollbacky deployovaných změn je také nutnost. Když něco nasadíme na produkci a nefunguje to, je nutné být schopný udělat jednoduše krok zpátky.
**Tazatel:** Hodnocení. Git integrace.
**Respondent 01:** Tři – za předpokladu, že když to nástroj nemá, nabízí alternativu.
**Tazatel:** API nebo CLI.
**Respondent 01:** Tři.
**Tazatel:** Automatizované testy.
**Respondent 01:** Pět.
**Tazatel:** Reproducibilita běhů – deterministické pipeline.
**Respondent 01:** Pět.

### C5. Uživatelská přívětivost a spolupráce
**Tazatel:** Jaký je váš pohled na no-code versus pro-code přístupy? Jak ovlivňují produktivitu týmu?
**Respondent 01:** Oba přístupy jsou hodné pro jiný typ uživatele a umožňují efektivitu. Oba umožňují naprosto nejvyšší možnou efektivitu v daném týmu, pokud jsou používány tím uživatelem, na který to řešení cílí.
Když máš data inženýra a platforma je více no-code, bude efektivní pro analytika nebo inženýra, který preferuje no-code. Když takovou platformu bude používat inženýr zvyklý pracovat v kódu, bude neefektivní UI klikání. A naopak.
Oba přístupy mají své místo. Důležité je vybírat podle týmu, který to staví, ale ultimátně hlavně podle celkových metrik projektu. Vědět, kdo bude hlavní typ uživatele, jak jednoduché bude se s tím naučit pracovat.
Oba přístupy jsou validní, nemám preference, záleží na konkrétním týmu.
V dnešní době se mění způsob práce s kódovými řešeními – inženýři už málo kdy píšou SQL dotazy samy, ale je to dělané s AI asistenty. Z pro-code nástrojů se vlastně stávají no-code nástroje. Očekává se, že user interface se velmi změní v následujících letech. Toto rozdělení a definice se pravděpodobně bude hodně měnit.
**Tazatel:** Může tedy existovat projekt, kde by se používal pouze jeden přístup?
**Respondent 01:** Může. Můžeš přijít k klientovi, který má datový tým složený z DevOps inženýrů, programátorů v Pythonu, a ti budou preferovat no-UI řešení. Některé platformy nabízí obě cesty. Některé platformy jsou vyloženy jenom jako kód nebo pro technické uživatele. Ale můžeš mít určitě projekty, kde bude stačit jedna cesta.
**Tazatel:** Hodnocení. Jednoduchost onboardingu pro nové uživatele.
**Respondent 01:** Čtyři.
**Tazatel:** Dokumentace.
**Respondent 01:** Čtyři.
**Tazatel:** Debugging tools.
**Respondent 01:** Pět.
**Tazatel:** Sdílení práce – kolaborace více uživatelů.
**Respondent 01:** Čtyři. Větší porce projektů vyžaduje dobrý způsob spolupráce na produktu.

### C6. Business dopad a ekonomika
**Tazatel:** Jak v praxi posuzujete celkový náklad vlastnictví – TCO? Licence, compute, správa, dovednosti týmu?
**Respondent 01:** Potřebujeme být schopní atribuovat náklad platformy na konkrétní use case. Use case je nějaký ohraničený projekt – řekněme automatizace reportingu je jeden use case, segmentace klientů je druhý.
Potřebujeme vědět, kolik platíme za realizaci jednotlivých use cases. Ideálně mít přehled nad tím, který tým vytváří největší náklad v platformě.
Ideální je mít přehled nad tím, za co přesně tam peníze utrácíš, a ne jen jedno celkové číslo na provoz. Abys byl schopný vyhodnocovat cost versus přínos jednotlivě a mohl vymyslet, co je dobré optimalizovat, co možná nedělat vůbec.
**Tazatel:** Setkal jste se s nějakými neočekávanými nebo skrytými náklady?
**Respondent 01:** U některých platforem můžeš cítit nutnost přinést si dodatečný datový tool, že vlastně v architektuře platforma pokrývá nějaké procento toho, co s daty děláš, ale pak ti může chybět něco jako data katalog nebo lineage. Často se přibírá extra tool.
Pro některé platformy je to nutný náklad, u některých je to pokryté v základní funkcionalitě.
Velmi skrytý náklad je ownership, maintenance a dodatečný vývoj a správa platformy. Kolik lidí a týmů okolo toho musí pracovat, aby to fungovalo.
Potom někdy nepřehlednost – pokud člověk není expert v dané platformě, může se dostat do nesnází. To platí typicky pro svépomocí postavená řešení třeba v AWS, kdy hledáme, jakou službu použít na dotazování do data lake, najdeme, že to jde přes Glue, ale už nevidíš, jaké služby v pozadí se nastartují. V pozadí se nastartuje spousta služeb, za které člověk platí, ani to na začátku neví.
**Tazatel:** Vnímáte jako výhodu platformy, že může zjednodušit billing?
**Respondent 01:** Ano. Ideální je, když k tomu nemusím mít dodatečné položky, když v tom mám dobrou přehlednost, za co přesně platím, a zároveň když mi tam nevzniká lineárně úměrný náklad na údržbu s tím, jak platformu používám.
U klientů, když rostou, roste i množství dat, roste potřeba dělat s platformou více. Nechceme, aby nám tam rostla potřeba týmu, který bude platformu udržovat.
**Tazatel:** Hodnocení. Time to value.
**Respondent 01:** Pět.
**Tazatel:** Total cost of ownership.
**Respondent 01:** Pět plus – nejvyšší důležitost.
**Tazatel:** Riziko vendor lock-in.
**Respondent 01:** Dva.
**Tazatel:** Auditovatelnost.
**Respondent 01:** Čtyři.

### C7. Srovnávací pohled (Keboola × Fabric × Databricks)
**Tazatel:** Máte zkušenost s několika platformami. Dokážete stručně popsat, v čem je silná stránka každé z nich a kde naopak narážíte?
**Respondent 01:** Ta komparace bude v každém kontextu jiná. Můžeš mít deset klientů a pro každého bude vhodné jiné řešení.
Když bych to zkusil srovnat obecně:
**Databricks:** Pro tým, který bude více technický, bude mít hodně dat – opravdu big data – a bude s daty chtít dělat něco velmi pokročilého z hlediska processingu a analytiky, tam už jde o data science. Databricks je go-to option, která bude mít pro tuto situaci nejvíce features a největší jistotu, že objem dat nebude problém.
**Keboola:** Když budu mít méně technický tým, který má hodně diverzní portfolio datových zdrojů, na které se potřebuje připojit, a má jasnou strukturu toho, co s nimi potřebuje dělat. Potřebuje flexibilitu – někdy SQL, někdy Python, nejednou něco úplně jiného. Chci otevřené řešení, které mi dovolí udělat cokoliv. Pak je to Keboola, která má spoustu konektorů, můžu tam vytvářet vlastní konektory, umožňuje automatizaci a je to i pro méně technického inženýra něco, co dokáže za pár dní se naučit používat.
**Microsoft Fabric:** Pro firmu, která už je hodně usazená v Microsoftím prostředí. Třeba už využívají Power BI, možná datové aplikace v Azure, možná SharePoint a Office, a jsou v tom ekosystému hodně zapečení. Pak Fabric dává smysl s tím, že je tam spousta nevýhod z toho, že to není maturované all-in-one řešení a je to dneska polepené řešení z více jednotlivých služeb. Ale dává smysl jako první pokus pro firmu v Microsoftím ekosystému.

### C8. Experimentální scénář a objektivní srovnání
**Tazatel:** Existuje podle vás nějaký způsob, kterým objektivně porovnat tyto platformy? Jaké metriky považujete za objektivní a použitelné pro srovnání?
**Respondent 01:** Ano. Pokud máš dobře definovaný začátek, že znáš strategii firmy, do které platformu přinášíš – víš, kam firma míří – tak první měřítko, které se dá objektivně srovnávat, je **time to value**. Vždycky.
Od momentu, kdy začneš pracovat na implementaci, kdy uvidí v byznysu value toho, že jsi to udělal. To se promítá do toho, jestli potřebuješ platformu konfigurovat, jestli konfiguruješ infrastrukturu, nebo jestli to rozsvítíš a začneš implementovat use case. Jak složité je to celé udělat pro tým.
Do toho vstupuje skill toho týmu. Ale to je něco, co můžeš změřit třeba v proof of concept na všech platformách – v které z platforem tvůj tým bude schopný nejrychleji doručit daný use case. Někde to vyhraje jedna, někde druhá, záleží na týmu. Ale je to objektivní metrika, kterou můžeš měřit.
Jde neodpojitelně od toho **škálovatelnost toho time to value**. Můžeš mít platformu, kde za jeden den uděláš use case, v druhé ti to dá týden. Ale když takových use cases budeš potřebovat sto, možná tím, že má druhá platforma dobře vyřešenou replikovatelnost, ti může těch sto trvat jen dva týdny – že to není lineární.
**Time to value** a **škálovatelnost vývoje** jsou určitě objektivní metriky.
Do toho time to value spadá i **cena za provoz** na daný use case a na ownership.
Pak jsou tam **binární features** – jestli to má tu feature nebo ne, to je jednoduché. Ale u většiny důležitých features se dostaneš k tomu, že každá platforma to má. Víc není, má to buď hůř nebo lépe vytvořené pro tvůj konkrétní tým. Už je to strašně kontextuální a srovnání nebývá fair.
Ale i to binární srovnání někdy stačí k rozhodnutí. Například pokud budeš mít spoustu specifických datových zdrojů, budou to nějaké aplikace nebo systémy používané jen lokálně, tak pro tebe bude kritické binární ano nebo ne – jestli si můžeš vyvíjet vlastní konektory, jestli máš tuhle flexibilitu. V jedné platformě ano, v druhé ne nebo velmi složitě. 
Time to delivery nebo time to value můžeš vždycky srovnávat. To jsou hlavní metriky.
**Tazatel:** Chápu to správně, že většina platforem bude mít binární features podobné, ale budou tam konkrétní věci, které se budou lišit?
**Respondent 01:** Skoro. Když si vezmeme, že každá datová cesta začíná data sourcing nebo ingestion, potřebuješ někud stáhnout data. Budeme uvažovat Keboolu, Fabric a Databricks.
V Databricks dneska je velmi omezené množství konektorů, přidávají nové, v budoucnosti to bude jinak, ale dneska platí, že uživatelé používají ještě externí ETL nástroj. Databricks má partnerství s Fivetran exkluzivní, takže Fivetran je nabízený jako konektory Databricksu, za které se extra platí. Nebo si týmy vyvíjejí v Pythonu vlastní konektory.
Keboola má spousty konektorů, mají generické konektory, kterými se dá napojovat na různá API. Rozšiřitelnost je tam velká.
U Fabricu mají také hodně konektorů, ale rozšiřitelnost je tam horší. Napsat si vlastní konektory je zase podobné jako v Databricksu – člověk se musí od nuly sám naprogramovat.
Kdybych měl firmu, do které potřebuji vztahovat hodně různých zdrojů dat, v tomhle pro mě bude vyhrávat Keboola. Binárně možnost udělat konektor na data bude ve všech ano, ale v Keboole čas na to a složitost bude neporovnatelně nižší než u ostatních. To ano/ne tam je často, ale právě to není bez kontextu vše říkající.

### C9. Cokoli důležitého, na co jsem se nezeptal?
**Tazatel:** Je něco důležitého, co jsem vynechal a co by v metodice pro porovnávání platforem mělo být?
**Respondent 01:** Do rozhodování vždycky vstupuješ shora do rozhodovacího stromu, kde varianty, které zvažuješ, jsou determinované tvým kontextem a situací.
Nějaké hodnotící metriky toho, jak velký máš tým, jak velký chceš mít tým, jestli je to více technický tým nebo spíš byznesový. Odpovědi na tyto otázky ti pomůžou možná zúžit výběr, že někde se rozhoduješ mezi Kebulou a Fabricem, a někdy tě to zúží tak, že nic jiného než Databricks nemá cenu porovnávat.
Určení toho kontextu ti může kandidáty předfiltrovat a nemusíš se pouštět do metrik time to value, lineage, governance.
Tyto vstupní definice kontextu ti můžou pomoct. Pak to srovnání může vždycky vypadat jinak a v každé variantě můžeš používat nebo přikládat váhu jiným metrikám.
O tohle by se to dalo obohatit na začátku – tvůj základní úkol je správně definovat zadání, které obsahuje to, kdo ty jsi, co je tvůj cíl, jakým způsobem se k němu chceš dostat, za jak dlouho, co to má přinést. Tyto metriky pak ovlivní to, jaké si nastavíš pro výběr.

### C10. Kalibrační cvičení (100 bodů)
**Tazatel:** Závěrečná část je kalibrační cvičení. Mám pět hlavních dimenzí: technická efektivita, kvalita dat, CI/CD, UX a business dopad. Kdybyste měl sto bodů a měl je rozdělit mezi těchto pět částí, přičemž více bodů znamená větší důležitost, jak byste je rozdělil?
**Respondent 01:** Tím, že je tam business dopad, tak bych vlastně nejvíc bodů dal business dopadu. To je vlastně to, proč to děláš. V bance neimplementuješ datovou platformu, aby tam data engineer měl hezké místo, kde píše SQL, ale děláš to, protože chceš co nejvíc peněz vydělat.
Business dopad je hlavní... Když to zkusím dát business dopadu padesát, aby zbývalo rozdělit mezi ostatní... Je složité to, že to jde ruku v ruce. CI/CD, technická efektivita a UX určitě jsou vzájemně se ovlivňující, ale kvalita dat mi z toho vystupuje jako něco důležitého.
Z těch padesáti bych dal kvalitě dat třicet. Když něco uděláš technicky efektivně a rychle a dobře nasadíš CI/CD, ale bude to špatně, tak je to k ničemu. Kvalita dat z těch padesáti je třicet.
Potom asi bych to rozdělal rovnoměrně mezi zbylé tři – deset každé, protože UX, CI/CD a technická efektivita jsou vzájemně se ovlivňující. Jsou pro mě srovnatelné a záleželo by na konkrétnější situaci.
**Tazatel:** Pro upřesnění – tedy Business dopad 50 bodů, Kvalita dat 30 bodů, a zbylých 20 bodů rovnoměrně mezi Technickou efektivitu, CI/CD a UX?
**Respondent 01:** Ano, přibližně. Technická efektivita by mě možná mrzela nejvíc, kdyby byla špatná, ale zároveň si myslím, že by byla způsobená tím UX. Nejsou od sebe moc oddělitelné.
### Závěr rozhovoru
**Tazatel:** To je ode mě vše. Moc vám děkuji za čas a za vyčerpávající odpovědi.
**Respondent 01:** Není zač. Hodně štěstí s tou prací.
**Tazatel:** Děkuji. Pošlu vám transkript k autorizaci a případným úpravám.
**Respondent 01:** Dobře, děkuji.
## ŠKÁLY A KALIBRACE - SOUHRN
### Škály 1-5 (1 = nice to have, 5 = kriticky důležité)
**C2. Technická efektivita:**
- Rychlost: 2
- Stabilita: 5
- Škálování: 4
- Observabilita: 4
**C3. Kvalita dat a governance:**
- Data lineage: 3
- Data quality testy: 5
- Access control (RBAC): 5
- Metadata katalog: 3
**C4. CI/CD:**
- Git integrace: 3 (pokud existuje alternativa)
- API/CLI: 3
- Automatizované testy: 5
- Reproducibilita běhů: 5
**C5. UX a spolupráce:**
- Onboarding: 4
- Dokumentace: 4
- Debugging tools: 5
- Sdílení artefaktů: 4
**C6. Business dopad:**
- Time to value: 5
- Total cost of ownership: 5+ (nejvyšší důležitost)
- Vendor lock-in riziko: 2
- Auditovatelnost: 4
### Kalibrace 100 bodů (C10)
**Rozdělení důležitosti mezi 5 dimenzí:**
- **Business dopad:** 50 bodů
- **Kvalita dat:** 30 bodů
- **Technická efektivita:** ~7 bodů
- **CI/CD:** ~6 bodů
- **UX:** ~7 bodů
*(Poznámka: Respondent zdůraznil, že poslední tři dimenze jsou vzájemně provázané a těžko oddělitelné, proto přibližně rovnoměrné rozdělení zbylých 20 bodů.)*
**KONEC TRANSKRIPTU**