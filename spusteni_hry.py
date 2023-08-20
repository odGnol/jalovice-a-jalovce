from herni_funkce import vygenerovat_cislo, validovat_cislo
from vyhodnocovani import slovni_hodnoceni, vyhodnotit_hru, hodnoceni_hry, pocet_kravobyku
from ukladani_hracu import ulozit_data 

def uvod_hry() -> None:
  oddelujici_cara = "-" * 60

  print("Ahoj, vítej ve hře Krávy a býci!", oddelujici_cara,
        "Právě bylo vygenerováno náhodné číslo.",
        "Započněme hru o krávách a býcích", oddelujici_cara,
        "Hádej číslo: ", oddelujici_cara, sep="\n")

def spustit_hru() -> None:
    je_hra_nova: bool = True
    ma_hra_pokracovat: bool = False
    kontrola_hodnot: bool = False
    pocet_vitezstvi = 0
    pocet_hadani = 0
    hranice_pokracovani = 5
    vysledek = ""
    stav_hry = ""
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
            ulozit_data(pocet_hadani)

          je_hra_nova = True if pokracovat_ve_hre("Chceš novou hru? [A / Jakákoli klávesa]") else quit()
        else:
          pocet_hadani += 1

          if pocet_hadani == hranice_pokracovani:
            print(stav_hry)
            ma_hra_pokracovat = True if pokracovat_ve_hre("Moc to nejde. Chceš pokračovat? [A / Jakákoli klávesa]") else quit()

def pokracovat_ve_hre(dotaz_na_pokracovani: str) -> bool:
  pokracuje_hra = input(f"{dotaz_na_pokracovani} ")
  return pokracuje_hra.upper() == "A"