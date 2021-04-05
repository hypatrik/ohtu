class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulokset = [tulos]

    def miinus(self, arvo):
        self.tulokset.append(self.tulos - arvo)

    def plus(self, arvo):
        self.tulokset.append(self.tulos + arvo)

    def nollaa(self):
        self.tulokset.append(0)

    def aseta_arvo(self, arvo):
        self.tulokset.append(arvo)

    def kumoa(self):
        del self.tulokset[-1]
    
    @property
    def tulos(self):
        return self.tulokset[-1]
