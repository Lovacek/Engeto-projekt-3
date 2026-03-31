# Engeto projekt 3 Python akademie

Třetí projekt pro Python akademii od Engeta

## Popis projektu

Tento program složí k extrahování výsledků parlamentních voleb z roku 2017.

## Instalace knihoven

Knihovny, které jsou použity v kódu jsou uloženy v souboru requirements.txt. Pro instalaci doporučuji použít nové virtualní prostředí a spustit v termiálu následovně:

`pip install -r requirements.txt` # nainstaluje knihovny 

## Spuštění Programu 

Spuštění souboru main.py v ramci příkazového řádku požaduje dva povinne argumenty:

`main.py <url_požadovaného_uzemního_celku> <název_výstupního_souboru.csv>`

Následně se vám stáhnou výsledky jako soubor s příponou .csv.

V případě špatného zadání argumentu je uživatel upozorněn a program se následně ukončí.

## Ukázka projektu

### Výsledky hlasování pro okres Nový jičín:

1. `argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104`
2. `argument: vysledky_novy_jicin.csv`

### Spuštění Programu:

`main.py https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104 vysledky_novy_jicin.csv`

### Průběh Stahování:

`Stahuji data z https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8104` #URL se mění v návaznosti na URL zadané v argumentu 1.

`Zpracovávám: <název_aktualne_scrapovane_obce>` #tento výstup se opakuje dokud se program nedokončí

`Stahování dokončeno. Data uložena do vysledky_novy_jicin.csv` #název souboru se mění v návaznosti na název zadaný v argumentu 2.

### Částečný výstup:
```
kód obce;název obce;voliči v seznamu;vydané obálky;platné hlasy;Občanská demokratická strana;Řád národa...	
568741; Albrechtičky;559;358;355;36;0;1;23;1;12;23;3;2;1;2;1;39;0;1;22;106;0;1;47;0;1;0;0;33;0
599212; Bartošovice;1341;735;734;39;3;0;56;2;6;104;13;2;9;0;0;38;0;0;7;281;1;2;23;0;1;3;2;140;2
568481; Bernartice nad Odrou;779;547;542;70;1;0;25;1;18;21;12;2;4;1;6;47;0;1;11;163;0;0;110;0;6;0;0;43;0
546984; Bílov;442;264;264;16;0;0;13;0;3;42;3;2;3;1;0;20;0;0;2;103;0;2;10;0;2;1;0;41;0
599247; Bílovec;6025;3496;3475;301;2;3;277;4;85;280;36;25;39;2;1;375;2;2;127;1192;6;7;194;0;20;11;11;458;15
554936; Bítov;357;254;249;12;0;0;42;1;7;20;2;5;5;0;0;14;0;0;8;100;0;0;14;0;2;1;0;14;2
568431; Bordovice;478;332;332;28;0;0;25;3;9;31;4;5;9;0;0;17;0;0;8;123;0;0;23;0;3;1;1;41;1
```

