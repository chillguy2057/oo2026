class Akvaarium:
    def __init__(self, pikkus: float, laius: float, korgus: float):
        self.__pikkus = pikkus
        self.__laius = laius
        self.__korgus = korgus
        self.__vesi = 0.0

    def ruumala(self) -> float:
        """Tagastab ruumala liitrites (cm3 / 1000)."""
        return (self.__pikkus * self.__laius * self.__korgus) / 1000

    def __max_vesi(self) -> float:
        return (self.__pikkus * self.__laius * self.__korgus) / 1000

    def __hoiatus_kontroll(self):
        vaba_cm = self.__korgus - (self.__vesi * 1000 / (self.__pikkus * self.__laius))
        if vaba_cm < 2:
            print("Hoiatus: servani jääb alla 2 cm!")

    def lisa_vesi(self, kogus: float):
        """Lisab vett liitrites."""
        if self.__vesi + kogus > self.__max_vesi():
            raise ValueError("Akvaarium täituks üle ääre!")
        self.__vesi += kogus
        self.__hoiatus_kontroll()


    def vee_kogus(self) -> float:
        """Tagastab praeguse vee koguse liitrites."""
        return self.__vesi

    def vala_teise(self, teine: "Akvaarium", kogus: float):
        """Valab kogus liitrit sellest akvaariumist teise."""
        if kogus > self.__vesi:
            raise ValuseError("Pole piisavalt vett!")
        self.__vesi -= kogus
        teine.lisa_vesi(kogus)

    def __str__(self):
        return (f"Akvaarium {self.__pikkus}x{self.__laius}x{self.__korgus} cm | "
                f"ruumala: {self.ruumala():.1f} L | vett: {self.__vesi:.1f} L")




a1 = Akvaarium(60, 30, 40)
a2 = Akvaarium(40, 20, 30)

a1.lisa_vesi(50)
a2.lisa_vesi(10)

print(a1)
print(a2)

print(f"\nValame 8 L akvaariumist 1 akvaariumisse 2:")
a1.vala_teise(a2, 8)

print(a1)
print(a2)








