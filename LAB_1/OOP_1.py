import json


class ModelAI:
    liczba_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        ModelAI.nowy_model(self)

    def nowy_model(self):
        ModelAI.liczba_modeli += 1

    @classmethod
    def ile_modeli(cls):
        return cls.liczba_modeli

    @classmethod
    def z_pliku(cls, nazwa_pliku):
        with open(nazwa_pliku, "r") as file:
            data = json.load(file)

        return cls(data["name"], data["version"])


AI_1 = ModelAI(nazwa_modelu="SVM", wersja="1.0")
AI_2 = ModelAI(nazwa_modelu="XGBOOST", wersja="2.4")
AI_3 = ModelAI(nazwa_modelu="K-nearest", wersja="3.1")
AI_4 = ModelAI.z_pliku("data.json")
print(AI_1.ile_modeli())
