import json
with open("szkola.json", "r") as p:
    szkola = json.load(p)
# {"konkretnaklasa": [wychowawca, nauczyciel 1, nauczyciel 2, uczen 1, uczen 2],
# "konkretnaklasa n": [wychowawca, nauczyciel 1, nauczyciel 2, nauczyciel n, uczen 3] }


class Klasa:
    def __init__(self):
        self.klasa = {"nazwa": None, "uczniowie": [], "wychowawca": None, "nauczyciele": []}
# { "nazwa" = wychowawca.klasa lub uczen.klasa
#  "uczniowie" = []
# "wychowawca" = wychowawca.dane
# "nauczyciele" = [] }


class Uczen:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa
        self.nauczyciele = []


class Nauczyciel:
    def __init__(self, dane, przedmiot, klasy):
        self.dane = dane
        self.przedmiot = przedmiot
        self.klasy = klasy


class Wychowawca:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa


def wczytaj_ucznia():
    dane = input("Podaj imię i nazwisko: \n")
    klasa = input("Podaj klasę: \n")
    uczen = Uczen(dane=dane, klasa=klasa)
    return uczen


def wczytaj_nauczyciela():
    dane = input("Podaj imię i nazwisko: \n")
    przedmiot = input("Podaj nazwę przedmiotu: \n")
    klasy = []
    while True:
        k = input("Podaj nazwę klasy: \n")
        klasy.append(k)
        if not k:
            break
    nauczyciel = Nauczyciel(dane=dane, przedmiot=przedmiot, klasy=klasy)
    return nauczyciel


def wczytaj_wychowawce():
    dane = input("Podaj imię i nazwisko: \n")
    klasa = input("Podaj klasę: \n")
    wychowawca = Wychowawca(dane=dane, klasa=klasa)
    return wychowawca


menu_glowne = ("utwórz", "zarządzaj", "koniec")
podmenu_dla_utworz = ("uczeń", "nauczyciel", "wychowawca", "koniec")
podmenu_dla_zarzadzaj = ("klasa", "uczeń", "nauczyciel", "wychowawca", "koniec")


while True:
    print(*menu_glowne, sep='\n')
    polecenie = input("Wpisz polecenie: \n")
    if polecenie == "koniec":
        with open("szkola.json", "w") as p:
            json.dump(szkola, p)
            break
    elif polecenie == "utwórz":
        print(*podmenu_dla_utworz, sep='\n')
        tworzony_typ = input("Wybierz typ wpisu, który chcesz stworzyć \n"
                             "lub wróć do poprzedniego menu (koniec).\n")
        if tworzony_typ == "koniec":
            print("Wracam do poprzedniego menu.")
            continue
        elif tworzony_typ == "uczeń":
            uczen = wczytaj_ucznia()
            nowa_klasa = Klasa()
            nowa_klasa.klasa["nazwa"] = uczen.klasa
            nowa_klasa.klasa["uczniowie"].append(uczen.dane)
            nazwa_klasy = nowa_klasa.klasa["nazwa"]
            szkola[nazwa_klasy] = {}
            dane_klasy = szkola[nazwa_klasy]
            dane_klasy["uczniowie"] = []
            dane_klasy["uczniowie"].append(uczen.dane)
        elif tworzony_typ == "wychowawca":
            wychowawca = wczytaj_wychowawce()
            nowa_klasa = Klasa()
            nowa_klasa.klasa["nazwa"] = wychowawca.klasa
            nowa_klasa.klasa["wychowawca"] = wychowawca.dane
        elif tworzony_typ == "nauczyciel":
            nauczyciel = wczytaj_nauczyciela()








