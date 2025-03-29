import math

def objetosc_szescianu(bok):
    return bok ** 3

def pole_powierzchni_szescianu(bok):
    return 6 * bok ** 2

def objetosc_prostopadloscianu(dlugosc, szerokosc, wysokosc):
    return dlugosc * szerokosc * wysokosc

def pole_powierzchni_prostopadloscianu(dlugosc, szerokosc, wysokosc):
    return 2 * (dlugosc * szerokosc + dlugosc * wysokosc + szerokosc * wysokosc)

def objetosc_kuli(promien):
    return (4/3) * math.pi * promien ** 3

def pole_powierzchni_kuli(promien):
    return 4 * math.pi * promien ** 2