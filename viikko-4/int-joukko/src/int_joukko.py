class IntJoukko:
    # jätetty konstruktori parametrit koska en koske testeihin.
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self._jono = set()

    def kuuluu(self, n):
        return n in self._jono

    def lisaa(self, n):
        self._jono.add(n)

    def poista(self, n):
        if n in self._jono:
            self._jono.remove(n)

    def mahtavuus(self):
        return len(self._jono)

    def to_int_list(self):
        return list(self._jono)

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        joukko._jono = a._jono.union(b._jono)

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        joukko._jono = a._jono.intersection(b._jono)

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        joukko._jono = a._jono.difference(b._jono)
        return joukko

    def __str__(self):
        return "{" + str(self.to_int_list())[1:-1] + "}"
