# Wystepujace klasy obiektow:

class Szkola:
    def __init__(self):
        self.klasy = {}
        self.nauczyciele = {}

    def dodaj_nowa_klase(self, klasa):
        if klasa in self.klasy:
            return
        self.klasy[klasa] = self.pusta_klasa()

    def dodaj_nauczyciela(self, nauczyciel):
        self.nauczyciele[nauczyciel.dane] = nauczyciel

    def pusta_klasa(self):
        return {
            "uczniowie": [],
            "wychowawca": [],
            "nauczyciele": []
        }


class Klasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.uczniowie = []
        self.nauczyciele = []
        self.wychowawca = None


class Uczen:
    def __init__(self, dane, klasa):
        self.dane = dane
        self.klasa = klasa
        self.nauczyciele = []

    def pokaz_dane_ucznia(self):
        print(f"Imię i nazwisko ucznia to {Uczen.dane}. ")

    def pokaz_klase_ucznia(self):
        print(f"Uczeń chodzi do klasy {Uczen.klasa}. ")


class Nauczyciel:
    def __init__(self, dane, przedmiot, klasy=[]):
        self.dane = dane
        self.przedmiot = przedmiot
        self.klasy = klasy

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


# Funkcje
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

