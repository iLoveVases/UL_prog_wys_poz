import math

def pole_kwadratu(bok):
    return bok ** 2

def obwod_kwadratu(bok):
    return 4 * bok

def pole_prostokata(dlugosc, szerokosc):
    return dlugosc * szerokosc

def obwod_prostokata(dlugosc, szerokosc):
    return 2 * (dlugosc + szerokosc)

def pole_kola(promien):
    return math.pi * promien ** 2

def obwod_kola(promien):
    return 2 * math.pi * promien