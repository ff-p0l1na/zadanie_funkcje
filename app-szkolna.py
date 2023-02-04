# mozliwe Classes:
class Uczen:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa

    def pokaz_dane_ucznia(self):
        print(f"Imię i nazwisko ucznia to {Uczen.dane}. ")

    def pokaz_klase_ucznia(self):
        print(f"Uczeń chodzi do klasy {Uczen.klasa}. ")

class Nauczyciel:
    def __init__(self, dane, przedmiot, klasa):
        self.dane = dane
        self.przedmiot = przedmiot
        self.klasa = klasa # klasy = []

    def pokaz_dane_nauczyciela(self):
        print(f"Imię i nazwisko nauczyciela to {Nauczyciel.dane}.")

    def pokaz_nauczany_przedmiot(self):
        print(f"{Nauczyciel.dane} uczy przedmiotu o nazwie {Nauczyciel.przedmiot}.")

    def pokaz_klasy_nauczyciela(self):
        print(f"{Nauczyciel.dane} uczy w następujących klasach: {Nauczyciel.klasa}")

class Wychowawca:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa

    def pokaz_dane_wychowawcy(self):
        print(f"Imię i nazwisko wychowawcy to {Wychowawca.dane}.")

    def pokaz_klase_wychowawcy(self):
        print(f"{Wychowawca.dane} jest wychowawcą w klasie {Wychowawca.klasa}.")

# funkcje:
def wczytaj_ucznia():
    dane = input("Podaj imię i nazwisko: \n")
    klasa = input("Podaj klasę: \n")
    uczen = Uczen(dane=dane, klasa=klasa)
    return uczen

def wczytaj_nauczyciela():
    dane = input("Podaj imię i nazwisko: \n")
    przedmiot = input("Podaj nazwę przedmiotu: \n")
    klasa = input("Podaj klasę: \n")
    nauczyciel = Nauczyciel(dane=dane, przedmiot=przedmiot, klasa=klasa)
    return nauczyciel

def wczytaj_wychowawce():
    dane = input("Podaj imię i nazwisko: \n")
    klasa = input("Podaj klasę: \n")
    wychowawca = Wychowawca(dane=dane, klasa=klasa)
    return wychowawca

# menu:
menu_glowne = ("utwórz", "zarządzaj", "koniec")
podmenu_dla_utworz = ("uczeń", "nauczyciel", "wychowawca", "koniec")
podmenu_dla_zarzadzaj = ("klasa", "uczeń", "nauczyciel", "wychowawca", "koniec")
# trzymanie danych:
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
         nowy_uczen = wczytaj_ucznia()
         print(f"Stworzono ucznia {nowy_uczen.dane}, w klasie {nowy_uczen.klasa} .")
        elif tworzony_typ == "nauczyciel":
            nowy_nauczyciel = wczytaj_nauczyciela()
            #TODO
        elif tworzony_typ == "wychowawca":
            nowy_wychowawca = wczytaj_wychowawce()
            #TODO
    elif polecenie == "zarządzaj":
        print(*podmenu_dla_zarzadzaj, sep='\n')
        zarzadzany = input("Wybierz z menu jeden z elementów.")
        if zarzadzany == "uczeń":
            #TODO
        elif zarzadzany == "nauczyciel":
            #TODO
        elif zarzadzany == "wychowawca":
            #TODO
        elif zarzadzany == "klasa":
            #TODO
        else:
            print(f"Nie ma takiej opcji jak {zarzadzany}. Spróbuj ponownie.")
            continue
    elif polecenie == "koniec":
        print("Dziękuję za wypowiedź, żegnam.")
        break
    else:
        print(f"Nie znam polecenia \"{polecenie}\". Wracam do poprzedniego menu.")
        continue




