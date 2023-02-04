# mozliwe klasy
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