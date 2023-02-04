# mozliwe Classes
class Uczen:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa

    def pokaz_dane_ucznia(self):
        print(f"Imię i nazwisko ucznia to {Uczen.dane}. ")

    def pokaz_klase_ucznia(self):
        print(f"Uczeń chodzi do klasy {Uczen.klasa}. ")

class Nauczyciel:
    def __init__(self, dane, przedmiot, klasy):
        self.dane = dane
        self.przedmiot = przedmiot
        self.klasy = klasy # klasy = []

    def pokaz_dane_nauczyciela(self):
        print(f"Imię i nazwisko nauczyciela to {Nauczyciel.dane}.")

    def pokaz_nauczany_przedmiot(self):
        print(f"{Nauczyciel.dane} uczy przedmiotu o nazwie {Nauczyciel.przedmiot}.")

    def pokaz_klasy_nauczyciela(self):
        print(f"{Nauczyciel.dane} uczy w następujących klasach: {Nauczyciel.klasy}")

class Wychowawca:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa

    def pokaz_dane_wychowawcy(self):
        print(f"Imię i nazwisko wychowawcy to {Wychowawca.dane}.")

    def pokaz_klase_wychowawcy(self):
        print(f"{Wychowawca.dane} jest wychowawcą w klasie {Wychowawca.klasa}.")

# funkcje
def zapytaj_o_dane():
    dane = input("Podaj imię i nazwisko: ")
    return dane

# menu
menu_glowne = ("utwórz", "zarządzaj", "koniec")
podmenu_dla_utworz = ("uczeń", "nauczyciel", "wychowawca", "koniec")
podmenu_dla_zarzadzaj = ("klasa", "uczeń", "nauczyciel", "wychowawca", "koniec")
# trzymanie danych
nauczyciele = []
uczniowie = []
wychowawcy = []

#
while True:
    print(*menu_glowne, sep='\n')
    polecenie = input("Wpisz polecenie: \n")
    if polecenie == "utwórz":
        print(*podmenu_dla_utworz, sep='\n')
        tworzony_typ = input("Wybierz typ wpisu, który chcesz stworzyć \n"
                             "lub wróć do poprzedniego menu (koniec).")
        if tworzony_typ == "koniec":
            print("Wracam do poprzedniego menu.")
            continue
        elif tworzony_typ == "uczeń":
            zapytaj_o_dane()
        elif tworzony_typ == "nauczyciel":
            zapytaj_o_dane()
            #TODO
        elif tworzony_typ == "wychowawca":
            zapytaj_o_dane()
            #TODO
    elif polecenie == "zarządzaj":
        #TODO
    elif polecenie == "koniec":
        print("Dziękuję za wypowiedź, żegnam.")
        break
    else:
        print(f"Nie znam polecenia \"{polecenie}\". Wracam do poprzedniego menu.")
        continue




