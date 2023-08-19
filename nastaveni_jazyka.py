def nastavit_jazyk(vybrany_jazyk: str) -> object:
  welcome_txt = {"cs": "Ahoj, vítej ve hře Krávy a býci!", "en": "Hello, welcome to the game of Bulls and Cows!"}
  generated_num_info = {"cs": "Právě bylo vygenerováno náhodné číslo.", "en": "The new number has been generated."}
  starting_game_info = {"cs": "Započněme hru o krávách a býcích", "en": "Let´s the game of Bulls and Cows begins!"}
  guess_num_txt = {"cs": "Hádej číslo: ", "en": "Enter a number!"}
  not_a_number_validated_state = {"cs": "Nejedná se o číslo.", "en": "It´s not a number."}
  not_zero_validated_state = {"cs": "Číslo nemůže začínat nulou", "en": "The number can not begins with a zero."}
  not_duplicated_number_validated_state = {"cs": "Číslo nesmí obsahovat duplikace číslic.", "en": "The number can not consist of duplicated digit."}
  less_digits_validated_state = {"cs": "Musí se jednat o čtyřmístní číslo. Přidejte číslice.", "en": "The number should be a 4 digit long. Add a digit."}
  more_digits_validated_state = {"cs": "Musí se jednat o čtyřmístní číslo. Uberte číslice.", "en": "The number should be a 4 digit long. Remove a digit."}
  new_game_status = {"cs": "Chceš novou hru? [A / Jakákoli klávesa]", "en": "Are you ready for the new game? [Y / Other key] "}
  continue_game_status = {"cs": "Moc to nejde. Chceš pokračovat? [A / Jakákoli klávesa]", "en": "Rubbish game. Do you want to continue? [Y / Other key] "}
  word_evaluation_1 = {"cs": "Super práce!", "en": "Nice job!"}
  word_evaluation_2 = {"cs": "Slušné, ale není to tak super.", "en": "Quite good, could have been better."}
  word_evaluation_3 = {"cs": "Příště to zmákneš jak pirát Threepwood!", "en": "Next time you will nail it like Guybrush Threepwood."}
  number_of_cb = {"cs": "Počty krav a býků jsou následující:", "en": "The numbers of cows and bulls are as follows:"}
  cow_flex_1 = {"cs": "kráva", "en": "cow"}
  cow_flex_2 = {"cs": "krávy", "en": "cows"}
  cow_flex_5 = {"cs": "krav", "en": "cows"}
  bull_flex_1 = {"cs": "býk", "en": "bull"}
  bull_flex_2 = {"cs": "býci", "en": "bulls"}
  bull_flex_5 = {"cs": "býků", "en": "bulls"}
  number_of_attempts = {"cs": "Počet pokusů: ", "en": "The number of attempts: "}

  nastaveni = {
    "welcome": welcome_txt[vybrany_jazyk],
    "gen_number": generated_num_info[vybrany_jazyk],
    "start_game": starting_game_info[vybrany_jazyk],
    "guess_num": guess_num_txt[vybrany_jazyk],
    "not_a_number": not_a_number_validated_state[vybrany_jazyk],
    "not_a_zero": not_zero_validated_state[vybrany_jazyk],
    "not_duplications": not_duplicated_number_validated_state[vybrany_jazyk],
    "less_digits": less_digits_validated_state[vybrany_jazyk],
    "more_digits": more_digits_validated_state[vybrany_jazyk],
    "new_game": new_game_status[vybrany_jazyk],
    "continue_game": continue_game_status[vybrany_jazyk],
    "we_1": word_evaluation_1[vybrany_jazyk],
    "we_2": word_evaluation_2[vybrany_jazyk],
    "we_3": word_evaluation_3[vybrany_jazyk],
    "cf_1": cow_flex_1[vybrany_jazyk],
    "cf_2": cow_flex_2[vybrany_jazyk],
    "cf_5": cow_flex_5[vybrany_jazyk],
    "bf_1": bull_flex_1[vybrany_jazyk],
    "bf_2": bull_flex_2[vybrany_jazyk],
    "bf_5": bull_flex_5[vybrany_jazyk],
    "num_cb": number_of_cb[vybrany_jazyk],
    "attempts": number_of_attempts[vybrany_jazyk]
              }
  return nastaveni

def vyber_jazyk() -> str:
  i = ''
  oddelujici_cara = "-" * 60
  vyber_jazyka = ["Čeština", "English"]

  while i not in vyber_jazyka:
    print("Vyber prosím jazyk. / Please choose the language. ? ", oddelujici_cara, sep="\n")

    for index, jazyk in enumerate(vyber_jazyka):
      print("{}) {}".format(index + 1, jazyk))

    i = input(">>-> ")
    print(oddelujici_cara, sep="\n")

    if i is "" or not i.isnumeric():
      vyber_jazyk()
    elif 0 < int(i) <= len(vyber_jazyka):
      return "cs" if vyber_jazyka[int(i) - 1] == "Čeština" else "en"
    else:
      print("Pro češtinu klikni prosím na klávesu 1. / For the english please click on key 2. ")
      vyber_jazyk()
  