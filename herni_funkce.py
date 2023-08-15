
import nastaveni as n

# TODO nastavení jazyka
lang = "cs"
nastaveni_jazyka = n.nastavit_jazyk(lang)

def uvod_hry() -> None:
  oddelujici_cara = "-" * 60

  print(nastaveni_jazyka["welcome"], oddelujici_cara,
        nastaveni_jazyka["gen_number"],
        nastaveni_jazyka["start_game"], oddelujici_cara,
        nastaveni_jazyka["guess_num"], oddelujici_cara, sep="\n")

def pokracovat_ve_hre(dotaz_na_pokracovani: str, lang: str) -> bool:
  pokracuje_hra = input(f"{dotaz_na_pokracovani} ")

  return pokracuje_hra.upper() == "A" if lang == "cs" else pokracuje_hra.upper() == "Y"
    
def hodnoceni_hry(hadane_cislo: int, vygenerovane_cislo: int) -> bool:
  return hadane_cislo == vygenerovane_cislo

def slovni_hodnoceni(pocet_hadani: int) -> str:
  if pocet_hadani == 0:
    return f"{nastaveni_jazyka['we_1']} {nastaveni_jazyka['attempts']}{pocet_hadani}"
  elif pocet_hadani == 1:
    return f"{nastaveni_jazyka['we_2']} {nastaveni_jazyka['attempts']}{pocet_hadani}"
  else:
    return f"{nastaveni_jazyka['we_3']} {nastaveni_jazyka['attempts']}{pocet_hadani}"

      
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
      print(nastaveni_jazyka["not_a_number"])
      return False
    
    maDuplikaci = any(hadane_cislo.count(cislice) > 1 for cislice in hadane_cislo)
    
    if hadane_cislo[0].isnumeric() and int(hadane_cislo[0]) == 0:
      print(nastaveni_jazyka["not_a_zero"])
      return False

    if len(hadane_cislo) > 4:
      print(nastaveni_jazyka["less_digits"])
      return False
    
    if len(hadane_cislo) < 4:
      print(nastaveni_jazyka["more_digits"])
      return False
    
    if maDuplikaci:
      print(nastaveni_jazyka["not_duplications"])
      return False
    
    return True

def pocet_kravobyku(hracovo_cislo: str, vygenerovane_cislo: int) -> object:
    vyhodnoceni = {"krávy": 0, "býci": 0}
    for index, char in enumerate(vygenerovane_cislo):
      if char == hracovo_cislo[index]:
        vyhodnoceni["býci"] += 1
      elif hracovo_cislo[index] in vygenerovane_cislo and char != hracovo_cislo[index]:
        vyhodnoceni["krávy"] += 1
    return vyhodnoceni

def vyhodnotit_hru(pocetKravByku: int) -> str:
  kravy: int = pocetKravByku['krávy']
  byci: int = pocetKravByku['býci']

  sklonovana_krava = nastaveni_jazyka["cf_5"] if kravy == 0 else (nastaveni_jazyka["cf_1"]  if kravy == 1 else nastaveni_jazyka["cf_2"] )
  sklonovany_byk = nastaveni_jazyka["bf_5"]  if byci == 0 else (nastaveni_jazyka["bf_1"]  if byci == 1 else nastaveni_jazyka["bf_2"] )
  prazdne = '⛔'
  
  return f"""{nastaveni_jazyka["num_cb"]}
                                              {kravy} {sklonovana_krava} {kravy * '🐄' if kravy > 0 else prazdne}
                                              {byci} {sklonovany_byk} {byci * '🐂' if byci > 0 else prazdne}
          """