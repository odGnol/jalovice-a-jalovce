"""
jalovice-a-jalovce.py: druhý projekt do Engeto Online Python Akademie
author: Long Do
email: -
discord: -
"""

from herniFunkce import vygenerovatCislo, validaceCisla, vyhodnotitCisla, vyhodnoceniHry

oddelujici_cara = "-" * 60
beziHra, novaHra = True, False
vygenerovane_cislo = vygenerovatCislo(4)

print("Ahoj, vítejte ve hře Krávy a býci!", oddelujici_cara, "Právě bylo vygenerováno náhodné číslo.", "Započněme hru o krávách a býcích", oddelujici_cara, "Hádejte číslo: ", oddelujici_cara, sep="\n")

while beziHra:
  if novaHra:
    vygenerovane_cislo = vygenerovatCislo(4)
    novaHra = False
  try:
    print("Hra: ", vygenerovane_cislo)
    hadane_cislo = input(">>> ")
    
    jeValidni = validaceCisla(hadane_cislo, vygenerovane_cislo)
    
    if jeValidni == True:
      v = vyhodnotitCisla(hadane_cislo, vygenerovane_cislo)
      vysledek = vyhodnoceniHry(v)
      print(vysledek, oddelujici_cara, sep='\n')
      
      if v['býci'] == 4:
        pokracovaniVeHre = input("Hru jste vyhráli. Přejete si zahrát další hru? [A / Jakákoliv jiná klávesnice]")
        if pokracovaniVeHre.upper() == "A":
          novaHra = True
          continue
        else:
          print("Končí hra...")
          quit()
          
    else:
      print("Konec - nesplněno.")
      quit()
      
  except ValueError:
    print("Nezadali jste číslo. Hra končí.")
    quit()