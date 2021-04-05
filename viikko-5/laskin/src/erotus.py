class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.lue_syote = lue_syote
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.miinus(self.lue_syote())

