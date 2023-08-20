def hodnoceni_hry(hadane_cislo: int, vygenerovane_cislo: int) -> bool:
  return hadane_cislo == vygenerovane_cislo

def slovni_hodnoceni(pocet_hadani: int) -> str:
  if pocet_hadani == 0:
    return f"Super práce! Pokusy: {pocet_hadani}"
  elif pocet_hadani == 1:
    return f"Slušné, ale není to tak super. Pokusy: {pocet_hadani}"
  else:
    return f"Příště to zmákneš jak pirát Threepwood! Pokusy: {pocet_hadani}"
  
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

  sklonovana_krava = "krav" if kravy == 0 else ("kráva"  if kravy == 1 else "krávy" )
  sklonovany_byk = "býků"  if byci == 0 else ("býk"  if byci == 1 else "býci" )
  prazdne = '⛔'
  
  return f"""Počty krav a býků jsou následující:
                                              {kravy} {sklonovana_krava} {kravy * '🐄' if kravy > 0 else prazdne}
                                              {byci} {sklonovany_byk} {byci * '🐂' if byci > 0 else prazdne}
          """