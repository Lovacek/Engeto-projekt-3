
"""projekt_3.py: Třetí projekt do Engeto Online Tester s Pythonem

author: Vítězslav Dlábek
email: vitezslavdlabek@gmail.com
"""

import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from urllib.parse import urlparse, parse_qs
import csv
import sys

 

def ziskej_link_mest(polivka, zakladni_url): # Funkce projde postupně tagy odkazujicí na url odkazy jednotlivých měst v okrese a následně vrátí seznam linků těchto obcí.

    mesta = []

    vsechny_odkazy = polivka.find_all("a") 

    for odkaz in vsechny_odkazy:

        relativni_cesta = odkaz.get("href")
        
        if relativni_cesta and "vyber=" in relativni_cesta: 
            url_obce = urljoin(zakladni_url, relativni_cesta)
            mesta.append(url_obce)
            
    return list(dict.fromkeys(mesta))
        
       

def vytvoreni_hlavicky(polivka, zakladni_url): # Funkce pro vytvoření hlavičky výsledného souboru, funkce použije předepsaný seznam, obsahující prvních 5 hodnot a následně k ním přidá politické strany z tabulky.

    hlavicka = ["kód obce", "název obce", "voliči v seznamu", "vydané obálky", "platné hlasy"]

    linky_obci = ziskej_link_mest(polivka, zakladni_url)

    odpoved_linku_obce = requests.get(linky_obci[0])

    polivka_obce = bs(odpoved_linku_obce.text, "html.parser")

    tag = polivka_obce.find_all("td", {'class': "overflow_name" })
    for ps in tag:
        hlavicka.append(ps.get_text())

  
    return hlavicka

def ziskej_data_obci(linky_obci): # funkce navštíví každý link obce získaný pomocí funkce ziskej_link_mest() a následně si z něj vybere všechna potřebná data a uloží je jako řádek do seznamu, který se nahraje do proměnné vysledny_seznam, který i funkce po dokončení vrátí.
    vysledny_seznam = []

    for link in linky_obci:
        radek = []
        parsed_url = urlparse(link)
        kod_obce = parse_qs(parsed_url.query).get('xobec', [None])[0]
        radek.append(kod_obce)

        odpoved_linku = requests.get(link)
        polivka_linku = bs(odpoved_linku.text, "html.parser")

        tag_nazvu_obci = polivka_linku.find_all('h3')
        for obec in tag_nazvu_obci:
            if 'Obec:' in obec.get_text(strip=True):
                nazev_obce = obec.get_text(strip=True).removeprefix("Obec:")
                radek.append(nazev_obce)

        cisla_tagu = ['sa2','sa3','sa6']

        for tag in cisla_tagu:
            hodnota = polivka_linku.find('td', {"headers":{tag}})
            if hodnota:
                cisty_vysledek =hodnota.get_text(strip=True).replace('\xa0','')
                radek.append(int(cisty_vysledek))

        tag = polivka_linku.find_all("td", {'class': "overflow_name" })

        for t in tag:
            soused = t.find_next_sibling("td")
            if soused:
                vysledek = soused.get_text(strip=True).replace('\xa0','')
                radek.append(int(vysledek))
            else:
                pass
        vysledny_seznam.append(radek)
        print(f"Zpracovávám: {nazev_obce}")
    return vysledny_seznam



def main(): # Hlavní funkce programu, která zkontroluje  správnost zadání vstupních argumentů a následně vyvolá funkce pro získání potřebných dat, ze kterých následně vytvoří CSV soubor 
    if len (sys.argv) != 3:
        print("\nŠpatně zadané hodnoty, prosím opakujte zadání")
        print("Fromát vstupu: python_soubor.py, URL, nazev_souboru.csv\n")
        return
    if not ".csv" in sys.argv[2]:
        print("\nVýstupní soubor není CSV, prosím opakujte zadání")
        print("Fromát vstupu: python_soubor.py, URL, nazev_souboru.csv\n")
        return
    zakladni_url = sys.argv[1] 
    vystupni_soubor = sys.argv[2]

    print(f"\nStahuji data z {zakladni_url}\n")

    try:
        odpoved_serveru = requests.get(zakladni_url)
        odpoved_serveru.raise_for_status()
        polivka = bs(odpoved_serveru.text, "html.parser")
        
        linky_obci = ziskej_link_mest(polivka, zakladni_url)
        
        if not linky_obci:
            print("\nNenalezeny žádné obce. Zkontrolujte URL.\n")
            return

        
        hlavicka = vytvoreni_hlavicky(polivka, zakladni_url)
        data = ziskej_data_obci(linky_obci)

        with open(vystupni_soubor, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(hlavicka)
            writer.writerows(data)
            
        print(f"\nStahování dokončeno. Data uložena do {vystupni_soubor}\n")

    except Exception as e:
        print(f"Nastala chyba: {e}")
     

if __name__ == "__main__":
    main()

