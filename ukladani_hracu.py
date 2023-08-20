def kontrolovat_existenci(soubor: str) -> bool:
    try:
        my_file = open(soubor)
        my_file.close()
        return True
    except FileNotFoundError:
        return False
    
def pocitat_radky(existuje_soubor: bool) -> int:
  pocet_radku = 1

  if existuje_soubor:
    with open("./seznam.txt", 'r') as fp:
      pocet_radku += sum(1 for line in fp if line.rstrip())
  
  return pocet_radku

def ulozit_data(pocet_pokusu: int) -> str:
  from datetime import datetime as dt

  cas_ulozeni = f"{dt.now().day}. {dt.now().month}. {dt.now().year} {dt.now().hour}:{dt.now().minute}:{dt.now().second}"
  # TODO validace souboru / data jsou napsaná správným postupem
  soubor_existuje = kontrolovat_existenci("./seznam.txt")
  pozice = pocitat_radky(soubor_existuje)

  jmeno_hrace = input("Jméno hráče: ")
  if soubor_existuje == False:
    with open("./seznam_hracu.txt", mode="x") as f: 
      f.write("") 

  with open("./seznam_hracu.txt", "a") as f:

      f.write(f"{pozice}) {jmeno_hrace} - Pokusy: {pocet_pokusu} / {cas_ulozeni} \n")
  return "Data uložena."
