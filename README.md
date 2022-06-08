# APBI: asynchronous Python Bazos interface

Python knižnica, určená na uľahčenie komunikácie s Bazošom, prostredníctvom jednoduchého rozhrania.

Táto knižnica povoľuje vyhľadávanie na Bazoši (aj cez RSS kanál), a tiež sledovanie nových inzerátov v reálnom čase.

Knižnica sa stará o to, aby sa neprekročil zadaný počet požiadaviek na server za sekundu (10 by default), a aby sa zbytočne často nevolali nové požiadavky.

&nbsp;


## Disclaimer

Táto knižnica nie je oficiálna knižnica od Bazošu, a s jeho tvorcami nie je nijako prepojená.

Bazoš nemá <ins>**ŽIADNU**</ins> verejne dostupnú dokumentáciu, a ani žiadne API endpoint-y. Z tohoto dôvodu musí knižnica neustále posielať požiadavky na server.

Maximálny povolený počet požiadaviek (za minútu) nie je nikde zverejnený, preto ak prekročíte odporúčaný limit, môžete stratiť prístup na Bazoš (či už na určitý, alebo neurčitý čas).

&nbsp;


## Installation

Na nainštalovanie knižnice je potrebný Python, verzia 3.7 alebo vyššie.

```
pip install apbi
```

&nbsp;


## Examples

Ukážkové súbory sa nachádzajú v priečinku [examples](/examples/).

&nbsp;


## Documentation and Questions

Celá dokumentácia je dostupná na [Wiki](https://github.com/Mahrkeenerh/apbi/wiki) stránke.

Všetky otázky je možné smerovať na [Discussions](https://github.com/Mahrkeenerh/apbi/discussions).

&nbsp;


## Bazos refresh cycle


Z vlastného testovania vyšlo, že stránka Bazošu a jej kategórie limit asi nemajú (prešlo približne 40 000 požiadaviek). Konkrétne inzeráty asi tiež nie sú obmedzené (prešlo viac ako 10 000 požiadaviek). Čo ale limitované je, je vyhľadávanie, a je limitované globálne pre celý Bazoš. Maximálny počet požiadaviek je 98. Za vyhľadávanie sa považuje hocičo, kde je obsiahnutý vyhľadávací reťazec (teda aj preklik na druhú stranu). Aj RSS kanál má limit maximálne 50 požiadaviek. Tieto limity sa obnovia až po internej aktualizácii serveru.

Bazoš nepridáva nové inzeráty okamžite, ako ich používatelia pridajú, ale server sa obnovuje každých približne 5-20 minút, kedy sú pridané všetky chýbajúce inzeráty, a vymazané všetky staré. Vždy pri tomto internom obnovení sa aj obnovia limity na požiadavky.
