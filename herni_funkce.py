
import nastaveni_jazyka as n

lang = n.vyber_jazyk()
jazyk_hry = n.nastavit_jazyk(lang)

def uvod_hry() -> None:
  oddelujici_cara = "-" * 60

  print(jazyk_hry["welcome"], oddelujici_cara,
        jazyk_hry["gen_number"],
        jazyk_hry["start_game"], oddelujici_cara,
        jazyk_hry["guess_num"], oddelujici_cara, sep="\n")

def pokracovat_ve_hre(dotaz_na_pokracovani: str) -> bool:
  pokracuje_hra = input(f"{dotaz_na_pokracovani} ")

  return pokracuje_hra.upper() == "A" if lang == "cs" else pokracuje_hra.upper() == "Y"
    
def hodnoceni_hry(hadane_cislo: int, vygenerovane_cislo: int) -> bool:
  return hadane_cislo == vygenerovane_cislo

def slovni_hodnoceni(pocet_hadani: int) -> str:
  if pocet_hadani == 0:
    return f"{jazyk_hry['we_1']} {jazyk_hry['attempts']}{pocet_hadani}"
  elif pocet_hadani == 1:
    return f"{jazyk_hry['we_2']} {jazyk_hry['attempts']}{pocet_hadani}"
  else:
    return f"{jazyk_hry['we_3']} {jazyk_hry['attempts']}{pocet_hadani}"
      
def vygenerovat_cislo(pocetCislic: int) -> int:
  import random as r

  rozsah = range(1,9)
  novaCisla = r.sample(rozsah, pocetCislic)
  vygenerovaneCislo = str()
  
  for cislo in novaCisla:
    vygenerovaneCislo += str(cislo)

  return vygenerovaneCislo

def validovat_cislo(hadane_cislo: any) -> bool:
    if not hadane_cislo.isnumeric():
      print(jazyk_hry["not_a_number"])
      return False
    
    maDuplikaci = any(hadane_cislo.count(cislice) > 1 for cislice in hadane_cislo)
    
    if hadane_cislo[0].isnumeric() and int(hadane_cislo[0]) == 0:
      print(jazyk_hry["not_a_zero"])
      return False

    if len(hadane_cislo) > 4:
      print(jazyk_hry["less_digits"])
      return False
    
    if len(hadane_cislo) < 4:
      print(jazyk_hry["more_digits"])
      return False
    
    if maDuplikaci:
      print(jazyk_hry["not_duplications"])
      return False
    
    return True

def pocet_kravobyku(hracovo_cislo: str, vygenerovane_cislo: int) -> object:
    vyhodnoceni = {"krávy": 0, "býci": 0}
    for index, char in enumerate(vygenerovane_cislo):
      if char == hracovo_cislo[index]:
        vyhodnoceni["krávy"] += 1
      elif hracovo_cislo[index] in vygenerovane_cislo and char != hracovo_cislo[index]:
        vyhodnoceni["krávy"] += 1

    return vyhodnoceni

def vyhodnotit_hru(pocetKravByku = {"krávy": 0, "býci": 0}) -> str:
  kravy: int = pocetKravByku['krávy']
  byci: int = pocetKravByku['býci']

  sklonovana_krava = jazyk_hry["cf_5"] if kravy == 0 else (jazyk_hry["cf_1"]  if kravy == 1 else jazyk_hry["cf_2"] )
  sklonovany_byk = jazyk_hry["bf_5"]  if byci == 0 else (jazyk_hry["bf_1"]  if byci == 1 else jazyk_hry["bf_2"] )
  prazdne = '⛔'
  
  return f"""{jazyk_hry["num_cb"]}
                                              {kravy} {sklonovana_krava} {kravy * '🐄' if kravy > 0 else prazdne}
                                              {byci} {sklonovany_byk} {byci * '🐂' if byci > 0 else prazdne}
          """

def kontrolovat_existenci(soubor: str) -> bool:
    try:
        my_file = open(soubor)
        my_file.close()
        return True
    except FileNotFoundError:
        return False


def ulozit_data(pocet_vitezstvi: int) -> str:
  from datetime import datetime as dt

  current_time = f"{dt.now().day}. {dt.now().month}. {dt.now().year} {dt.now().hour}:{dt.now().minute}:{dt.now().second}"

  soubor_existuje = kontrolovat_existenci("./seznam.txt")

  player_name = input("Jméno hráče: ")
  if soubor_existuje == False:
    with open("./seznam.txt", mode="x") as f: 
      f.write("") 

  with open("./seznam.txt", "a") as f:
      f.write(f"{player_name} - {pocet_vitezstvi} / {current_time} \n")

  return "Data uložena."
  

def spustitHru() -> None:
    je_hra_nova: bool = True
    ma_hra_pokracovat: bool = False
    kontrola_hodnot: bool = False
    pocet_vitezstvi, pocet_hadani, hranice_pokracovani = 0, 0, 5
    vysledek, stav_hry = "", ""
    hodnoceni_hrace = slovni_hodnoceni(pocet_hadani)

    uvod_hry()

    while True:
      
      if je_hra_nova:
        vygenerovane_cislo = vygenerovat_cislo(4)
        pocet_hadani = 0
        je_hra_nova = False
      elif ma_hra_pokracovat:
        pocet_hadani = 0
        ma_hra_pokracovat = False
      
      hadane_cislo = input(">>> ")
      kontrola_hodnot = validovat_cislo(hadane_cislo)
      pocet_hadani += 1

      if pocet_hadani == hranice_pokracovani:
        print(stav_hry)
        ma_hra_pokracovat = True if pokracovat_ve_hre(jazyk_hry["continue_game"]) else quit()
      
      #debug
      print("hádané číslo: ", hadane_cislo, "nové číslo: ", vygenerovane_cislo, "stav hadani: ", kontrola_hodnot, "pocet hadani ", pocet_hadani, sep="\n")

      if kontrola_hodnot is True:
        vysledek = pocet_kravobyku(hadane_cislo, vygenerovane_cislo)
        stav_hry = vyhodnotit_hru(vysledek)
        je_uhadnuto = hodnoceni_hry(hadane_cislo, vygenerovane_cislo)

        if je_uhadnuto == True:
          pocet_vitezstvi += 1
          print(stav_hry)
          print(hodnoceni_hrace)

          ulozeni_vysledku = True if input ("Chcete uložit výsledky? ").upper() == "A" else False

          if ulozeni_vysledku:
            ulozit_data(pocet_vitezstvi)

          # + umístění v žebříčku
          # 1. Kontrolovat body a podle toho přeorganizovat 

          je_hra_nova = True if pokracovat_ve_hre(jazyk_hry["new_game"]) else quit()
