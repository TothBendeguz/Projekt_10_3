class Jatek:
    def __init__(self, sor: str) -> None:
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.eladott = int(adatok[1])
        self.ar = int(adatok[2])
        self.ev = int(adatok[3])
        self.tipus = adatok[4]