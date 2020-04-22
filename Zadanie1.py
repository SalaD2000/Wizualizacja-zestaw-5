import sys

class Material:
    def __init__(self, rodzaj, długosc, szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=długosc
        self.szerokosc=szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)
 
class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo

    def wyswietl_dane(self):
        print(self.rozmiar)
        print(self.kolor)
        print(self.dla_kogo)

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra

    def wyswietl_danee(self):
        print(self.rodzaj_swetra)

Poliester=Material("poliester", 12, 15)
Spodnie=Ubrania("100", "biały", "młodzieży")
Sweter=Sweter("duży")

Poliester.wyswietl_nazwe()
Spodnie.wyswietl_dane()
Sweter.wyswietl_danee()