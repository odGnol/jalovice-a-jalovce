
import nastaveni as n
import herni_funkce as hf

# TODO nastavení jazyka
lang = "cs"
nastaveni_jazyka = n.nastavit_jazyk(lang)

def spustitHru() -> None:
    hra_je_spustena = True
    pocet_hadani, hranice_pokracovani = 0, 5
    vysledek, stav_hry = "", ""

    hf.uvod_hry()
    vygenerovane_cislo = hf.vygenerovat_cislo(4)

    while hra_je_spustena:
      #debug
      print("nové číslo: ", vygenerovane_cislo)
      
      hadane_cislo = input(">>> ")
      kontrola_hodnot = hf.validovat_cislo(hadane_cislo)
      
      #debug
      print("---- hádané číslo: ", hadane_cislo)

      if kontrola_hodnot == True:
        vysledek = hf.pocet_kravobyku(hadane_cislo, vygenerovane_cislo)
        stav_hry = hf.vyhodnotit_hru(vysledek)

      je_uhadnuto = hf.hodnoceni_hry(hadane_cislo, vygenerovane_cislo)

      if je_uhadnuto == True:
      # stav výhry a vyhodnocení
         hodnoceni_hrace = hf.slovni_hodnoceni(pocet_hadani)

         print(hodnoceni_hrace)
         print(stav_hry)

         if hf.pokracovat_ve_hre(nastaveni_jazyka["new_game"], lang):
            pocet_hadani = 0
            vygenerovane_cislo = hf.vygenerovat_cislo(4)
            continue
         else:
            break
      else:
         # TODO vynulovat, ale počítat s celkovým počtem hádání
         pocet_hadani += 1
         if hranice_pokracovani == pocet_hadani:
            print(stav_hry)
            if hf.pokracovat_ve_hre(nastaveni_jazyka["continue_game"], lang):
              pocet_hadani = 0
              continue
            else:
              break
         continue

if __name__ == "__main__":
    spustitHru()

# TODO zvuk
# TODO ukládání žebříčku [nick / nejvyšší skóre]