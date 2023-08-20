def vygenerovat_cislo(pocetCislic: int) -> int:
  import random as r

  rozsah = range(1,9)
  novaCisla = r.sample(rozsah, pocetCislic)
  vygenerovaneCislo = str()
  
  for cislo in novaCisla:
    vygenerovaneCislo += str(cislo)

  return vygenerovaneCislo

def validovat_cislo(hadane_cislo: any) -> bool:
    if hadane_cislo is "":
      print ("Nebylo nic doplněno, zkus to ještě jednou.")
      return False
    
    if not hadane_cislo.isnumeric():
      print("Nejedná se o číslo.")
      return False
    
    maDuplikaci = any(hadane_cislo.count(cislice) > 1 for cislice in hadane_cislo)
    
    if hadane_cislo[0].isnumeric() and int(hadane_cislo[0]) == 0:
      print("Člověče, číslo nemůže začínat nulou.")
      return False

    if len(hadane_cislo) < 4:
      print( "A jé, musí se jednat o čtyřmístní číslo. Přidej číslice.")
      return False
    
    if len(hadane_cislo) > 4:
      print("Musí se jednat o čtyřmístní číslo. Uber číslice. Bože!")
      return False
    
    if maDuplikaci:
      print("Číslo nesmí obsahovat duplikace číslic.")
      return False
    
    return True

