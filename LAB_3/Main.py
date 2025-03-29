from geompy import figury2d as d2
from geompy import figury3d as d3

# 2D
print(f"Kwadrat: pole = {d2.pole_kwadratu(4)}, obwód = {d2.obwod_kwadratu(4)}")
print(f"Prostokąt: pole = {d2.pole_prostokata(4, 5)}, obwód = {d2.obwod_prostokata(4, 5)}")
print(f"Koło: pole = {d2.pole_kola(3)}, obwód = {d2.obwod_kola(3)}")

# 3D
print(f"Sześcian: objętość = {d3.objetosc_szescianu(3)},"
      f" pole powierzchni = {d3.pole_powierzchni_szescianu(3)}")
print(f"Prostopadłościan: objętość = {d3.objetosc_prostopadloscianu(3, 4, 5)},"
      f" pole powierzchni = {d3.pole_powierzchni_prostopadloscianu(3, 4, 5)}")
print(f"Kula: objętość = {d3.objetosc_kuli(3)},"
      f" pole powierzchni = {d3.pole_powierzchni_kuli(3)}")