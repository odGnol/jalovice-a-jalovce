
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
    
    #if reset == True:
    #  vyhodnoceni["krávy"] = vyhodnoceni["krávy"] = 0

    return vyhodnoceni

def vyhodnotit_hru(pocetKravByku: int) -> str:
  kravy: int = pocetKravByku['krávy']
  byci: int = pocetKravByku['býci']

  sklonovana_krava = jazyk_hry["cf_5"] if kravy == 0 else (jazyk_hry["cf_1"]  if kravy == 1 else jazyk_hry["cf_2"] )
  sklonovany_byk = jazyk_hry["bf_5"]  if byci == 0 else (jazyk_hry["bf_1"]  if byci == 1 else jazyk_hry["bf_2"] )
  prazdne = '⛔'
  
  return f"""{jazyk_hry["num_cb"]}
                                              {kravy} {sklonovana_krava} {kravy * '🐄' if kravy > 0 else prazdne}
                                              {byci} {sklonovany_byk} {byci * '🐂' if byci > 0 else prazdne}
          """

def spustitHru() -> None:
    hra_je_spustena = True
    pocet_hadani, hranice_pokracovani = 0, 5
    vysledek, stav_hry = "", ""

    uvod_hry()
    vygenerovane_cislo = vygenerovat_cislo(4)

    while hra_je_spustena:
      
      hadane_cislo = input(">>> ")
      kontrola_hodnot = validovat_cislo(hadane_cislo)
      
      #debug
      print("hádané číslo: ", hadane_cislo, "nové číslo: ", vygenerovane_cislo, sep="\n")

      if kontrola_hodnot == True:
        vysledek = pocet_kravobyku(hadane_cislo, vygenerovane_cislo)
        stav_hry = vyhodnotit_hru(vysledek)

        je_uhadnuto = hodnoceni_hry(hadane_cislo, vygenerovane_cislo)

        if je_uhadnuto == True:
          hodnoceni_hrace = slovni_hodnoceni(pocet_hadani)

          print(stav_hry)
          print(hodnoceni_hrace)

          if pokracovat_ve_hre(jazyk_hry["new_game"], lang):
              pocet_hadani = 0
              vygenerovane_cislo = vygenerovat_cislo(4)
              continue
          else:
              break
        else:
          # TODO vynulovat, ale počítat s celkovým počtem hádání
          # Počet chyb vliv na hodnocení?
          pocet_hadani += 1
          if hranice_pokracovani == pocet_hadani:
              # stav hry po nezdařených odhadech - validace
              print(stav_hry)
              if pokracovat_ve_hre(jazyk_hry["continue_game"]):
                pocet_hadani = 0
                continue
              else:
                break