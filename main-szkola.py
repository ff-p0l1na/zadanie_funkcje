class Szkola:
    def __init__(self):
        self.klasy = {}
        self.nauczyciele = {}

    def wez_klase(self, nazwa_klasy):
        if nazwa_klasy not in self.klasy:
            self.dodaj_nowa_klase(nazwa_klasy)
        return self.klasy[nazwa_klasy]

    def dodaj_nauczyciela(self,nauczyciel):
        self.nauczyciele[nauczyciel.dane] = nauczyciel

    def dodaj_nowa_klase(self, klasa):
        if klasa in self.klasy:
            return
        self.klasy[klasa] = self.pusta_klasa(klasa)

    def pusta_klasa(self, klasa):
        return {
            "nazwa": klasa,
            "uczniowie": [],
            "wychowawca": [],
            "nauczyciele": [],
        }


class Uczen:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa
        self.nauczyciele = []

    def __repr__(self):
        return f'({self.dane}, {self.klasa})'


class Nauczyciel:
    def __init__(self, dane, przedmiot, klasy=None):
        self.dane = dane
        self.przedmiot = przedmiot
        if klasy:
            self.klasy = klasy
        else:
            self.klasy = []

    def __repr__(self):
        return f'({self.dane}, {self.przedmiot})'


class Wychowawca:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa

    def __repr__(self):
        return f'({self.dane}, {self.klasa})'


def wczytaj_ucznia():
    dane = input("Podaj imię i nazwisko: \n")
    klasa = input("Podaj klasę: \n")
    uczen = Uczen(dane=dane, klasa=klasa)
    return uczen


def wczytaj_nauczyciela(szkola):
    dane = input("Podaj imię i nazwisko: \n")
    przedmiot = input("Podaj nazwę przedmiotu: \n")
    nauczyciel = Nauczyciel(dane, przedmiot)
    szkola.dodaj_nauczyciela(nauczyciel)
    while True:
        nazwa_klasy = input("Podaj klasę. (Naciśnij [enter] żeby zakończyć wpisywanie klas.) \n")
        if not nazwa_klasy:
            break
        klasa = szkola.wez_klase(nazwa_klasy)
        klasa['nauczyciele'].append(nauczyciel)
        nauczyciel.klasy.append(klasa)


def wczytaj_wychowawce():
    dane = input("Podaj imię i nazwisko: \n")
    klasa = input("Podaj klasę: \n")
    wychowawca = Wychowawca(dane=dane, klasa=klasa)
    return wychowawca

# menu:
menu_glowne = ("utwórz", "zarządzaj", "koniec")
podmenu_dla_utworz = ("uczeń", "nauczyciel", "wychowawca", "koniec")
podmenu_dla_zarzadzaj = ("klasa", "uczeń", "nauczyciel", "wychowawca", "koniec")
#
szkola = Szkola()
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
            uczen = wczytaj_ucznia()
            klasa = szkola.wez_klase(uczen.klasa)
            klasa['uczniowie'].append(uczen)
        elif tworzony_typ == "wychowawca":
            wychowawca = wczytaj_wychowawce()
            klasa = szkola.wez_klase(wychowawca.klasa)
            klasa['wychowawca'] = wychowawca
        elif tworzony_typ == "nauczyciel":
            wczytaj_nauczyciela(szkola)
    elif polecenie == "zarządzaj":
        pass
    elif polecenie == "koniec":
        break






