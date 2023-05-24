import random as r

def vygenerovatCislo(pocetCislic):
  rozsah = range(1,9)
  novaCisla = r.sample(rozsah, pocetCislic)
  vygenerovaneCislo = str()
  
  for cislo in novaCisla:
    vygenerovaneCislo += str(cislo)

  return vygenerovaneCislo

def validaceCisla(hracovoCislo, hadaneCislo) -> bool:
  delkaCisla = len(str(hracovoCislo))
  if delkaCisla < 4 or 4 < delkaCisla:
    return False
  
  if hadaneCislo[0] == 0:
    return False

  maDuplicitniCisla = obsahujeDuplikaciCisla(hracovoCislo)
  
  if maDuplicitniCisla == True:
    return False
  
  if hracovoCislo.isnumeric():
    return True
  
  return True

def obsahujeDuplikaciCisla(posuzovaneCislo):
  cislo_str = str(posuzovaneCislo)
  cislice_lst = list(cislo_str)
  
  posuzovane_lst = []
  duplikace = []
  
  for c in cislice_lst:
    if c not in posuzovane_lst:
      posuzovane_lst.append(c)
    else:
      duplikace.append(c)
  
  return True if len(duplikace) > 0 else False

def vyhodnotitCisla(cislo, hadaneCislo):
    vyhodnoceni = {"krávy": 0, "býci": 0}
    for index, char in enumerate(hadaneCislo):
      if char == cislo[index]:
        vyhodnoceni["býci"] += 1
      elif cislo[index] in hadaneCislo and char != cislo[index]:
        vyhodnoceni["krávy"] += 1
    return vyhodnoceni

def vyhodnoceniHry(pocetKravByku) -> str:
  kravy: int = pocetKravByku['krávy']
  byci:int = pocetKravByku['býci']
  
  sklonovanaKrava = "krav" if kravy == 0 else ("kráva" if kravy == 1 else "krávy")
  sklonovanyByk = "býků" if byci == 0 else ("býk" if byci == 1 else "býci")
  prazdne = '⛔'
  
  return f"""Počty krav a býků je následující:
                                              {kravy} {sklonovanaKrava} {kravy * '🐄' if kravy > 0 else prazdne}
                                              {byci} {sklonovanyByk} {byci * '🐂' if byci > 0 else prazdne}
          """