from herni_funkce import vygenerovat_cislo, validovat_cislo
from vyhodnocovani import slovni_hodnoceni, vyhodnotit_hru, srovnani_cisel, pocet_kravobyku
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
    celkove_pokusy = 0
    pocet_hadani_po_validaci = 0
    hranice_pokracovani = 5
    hodnoceni_hrace = slovni_hodnoceni(celkove_pokusy)
    vysledek: object = {"krávy": 0, "býci": 0}
    stav_hry: str

    uvod_hry()

    while True:
        if je_hra_nova:
            vygenerovane_cislo = vygenerovat_cislo(4)
            celkove_pokusy = 0
            je_hra_nova = False
        elif ma_hra_pokracovat:
            celkove_pokusy = 0
            ma_hra_pokracovat = False
      
        hadane_cislo = input(">>> ")
        kontrola_hodnot = validovat_cislo(hadane_cislo)
        celkove_pokusy += 1
        stav_hry = vyhodnotit_hru(vysledek)

        if kontrola_hodnot == True:
            vysledek = pocet_kravobyku(hadane_cislo, vygenerovane_cislo)
            cisla_se_rovnaji = srovnani_cisel(hadane_cislo, vygenerovane_cislo)

            print("if - True", vysledek)

            if cisla_se_rovnaji == True:
                pocet_vitezstvi += 1
                stav_hry = vyhodnotit_hru(vysledek)

                print(stav_hry)
                print(hodnoceni_hrace)
                ulozeni_vysledku = True if input ("Chcete uložit výsledky? ").upper() == "A" else False
                
                if ulozeni_vysledku:
                    ulozit_data(celkove_pokusy, pocet_vitezstvi)

                je_hra_nova = True if pokracovat_ve_hre("Chceš novou hru? [A / Jakákoli klávesa]") else quit()
            
        else:
            print("Číslo jsi zatím neuhádl. To dáš! Zaber.")
            pocet_hadani_po_validaci += 1
            print("else - False: ", vysledek)

        if (celkove_pokusy % hranice_pokracovani) == 0:
            stav_hry = vyhodnotit_hru(vysledek) if kontrola_hodnot == True else vyhodnotit_hru({"krávy": 0, "býci": 0})

            print(stav_hry)

            ma_hra_pokracovat = True if pokracovat_ve_hre("Moc to nejde. Chceš pokračovat? [A / Jakákoli klávesa]") else quit()

def pokracovat_ve_hre(dotaz_na_pokracovani: str) -> bool:
  pokracuje_hra = input(f"{dotaz_na_pokracovani} ")
  return pokracuje_hra.upper() == "A"