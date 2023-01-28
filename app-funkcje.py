class Uczen:
    def __init__(self):
        self.dane = imie_i_nazwisko
        self.klasa = klasa
class Nauczyciel:
    def __init__(self):
        self.dane = imie_i_nazwisko
        self.przedmiot = przedmiot
        self.klasa = klasa
class Wychowawca:
    def __init__(self):
        self.dane = imie_i_nazwisko
        self.klasa = klasa

menu_glowne = ("utwórz", "zarządzaj", "koniec")
podmenu_dla_utworz = ("uczeń", "nauczyciel", "wychowawca", "koniec")
podmenu_dla_zarzadzaj = ("klasa", "uczeń", "nauczyciel", "wychowawca", "koniec")

while True:
    print(*menu_glowne, sep='\n')
    polecenie = input("Wpisz polecenie: \n")
    if polecenie not in menu_glowne:
        print(f"Polecenie {polecenie} nieprawidłowe. \n"
              f"Wpisz poprawne polecenie.")
        continue
    elif polecenie == "utwórz":
        print(*podmenu_dla_utworz, sep='\n')
        tworzony_typ = input("Wybierz typ wpisu, który chcesz stworzyć \n"
                             "lub wróć do poprzedniego menu (koniec).")
        if tworzony_typ == "koniec":
            print("Wracam.")
            continue
        elif tworzony_typ == "uczeń":
            imie_i_nazwisko = input("Wpisz imię i nazwisko: ")
            klasa = input("Do której klasy chodzi uczeń?")
            #TODO
        elif tworzony_typ == "nauczyciel":
            imie_i_nazwisko= input("Wpisz imię i nazwisko: ")
            przedmiot = input("Wpisz nazwę nauczanego przedmiotu.")
            klasa = input("Wpisz klasę, w której uczy i naciśnij enter. \n"
                          "Aby zakończyć wpisywanie pozostaw pole puste i naciśnij enter.")
            #TODO dodac klasy do listy?
        elif tworzony_typ == "wychowawca":
            imie_i_nazwisko = input("Wpisz imię i nazwisko. ")
            klasa = input("Wpisz klasę, w której jest wychowawcą. ")
    elif polecenie == "zarządzaj":
        print(*podmenu_dla_zarzadzaj, sep='\n')
    elif polecenie == "koniec":
        print("Koniec pracy programu.")
        break