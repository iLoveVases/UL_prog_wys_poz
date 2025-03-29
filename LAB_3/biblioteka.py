""""
Super fajna biblioteka
"""

class Ksiazka:
    """
    Ta klasa to klasa ksiazki
    """
    def __init__(self, tytul, autor, dostepna=True):
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna


class Biblioteka:
    """
    Ta klasa to klasa biblioteka
    """
    def __init__(self):
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """
        Metoda dodaj_ksiazke
        """
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """
        Metoda wypozycz_ksiazke
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                if ksiazka.dostepna:
                    ksiazka.dostepna = False
                    return f"Wypozyczono: {tytul}"
        return f"Brak ksiazki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """
        Metoda zwroc_ksiazke
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """
        Metoda dostepne_ksiazki
        """
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka.dostepna:
                dostepne.append(ksiazka.Tytul)
        return dostepne


def main():
    """
    Metoda main - glowna petla
    """
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedzmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki: ", biblioteka.dostepne_ksiazki())


main()
