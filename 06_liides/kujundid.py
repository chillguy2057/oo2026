from abc import ABC, abstractmethod
import math


class Kujund(ABC):
    
    @abstractmethod
    def arvuta_pindala(self):
        """Arvutab ja tagastab kujundi pindala"""
        pass

    @abstractmethod
    def arvuta_ymbermoot(self):
        """Arvutab ja tagastab kujundi ümbermõõdu"""
        pass

    @abstractmethod
    def anna_nimi(self):
        """Tagastab kujundi nime ja parameetrid stringina"""
        pass



class Ristkylik(Kujund):
    def __init__(self, kylg_a, kylg_b):
        self.kylg_a = kylg_a
        self.kylg_b = kylg_b

    def arvuta_pindala(self):
        return self.kylg_a * self.kylg_b

    def arvuta_ymbermoot(self):
        return 2 * (self.kylg_a + self.kylg_b)

    def anna_nimi(self):
        return f"Ristkülik mõõtudega {self.kylg_a}x{self.kylg_b}"



class Ring(Kujund):
    def __init__(self, raadius):
        self.raadius = raadius

    def arvuta_pindala(self):
        return math.pi * (self.raadius ** 2)

    def arvuta_ymbermoot(self):
        return 2 * math.pi * self.raadius

    def anna_nimi(self):
        return f"Ring raadiusega {self.raadius}"



if __name__ == "__main__":
    print("=== Kujundite töötlemine läbi liidese (Python) ===")
    

    kujundite_list = [
        Ristkylik(5.0, 4.0),
        Ring(3.0),
        Ristkylik(2.5, 10.0)
    ]
    
    for k in kujundite_list:
        print(f"\nKujund: {k.anna_nimi()}")
        print(f"Pindala: {k.arvuta_pindala():.2f}")
        print(f"Ümbermõõt: {k.arvuta_ymbermoot():.2f}")
