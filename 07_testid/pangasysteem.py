from abc import ABC, abstractmethod
import unittest


class RahakottLiides(ABC):
    
    @abstractmethod
    def pane_raha(self, summa: float) -> None:
        """Lisab rahakotti raha."""
        pass

    @abstractmethod
    def vota_raha(self, summa: float) -> bool:
        """Võtab rahakotist raha. Tagastab True kui õnnestus, muidu False."""
        pass

    @abstractmethod
    def kysi_jaak(self) -> float:
        """Tagastab hetke kontojäägi."""
        pass



class DigiRahakott(RahakottLiides):
    def __init__(self, algne_jaak: float = 0.0):
        self._jaak = algne_jaak

    def pane_raha(self, summa: float) -> None:
        if summa > 0:
            self._jaak += summa

    def vota_raha(self, summa: float) -> bool:
       
        if 0 < summa <= self._jaak:
            self._jaak -= summa
            return True
        return False 

    def kysi_jaak(self) -> float:
        return self._jaak


def naitprogramm():
    print("=== Näitprogramm: Digirahakoti kasutamine ===")
    minu_konto = DigiRahakott(50.0) 
    
    print(f"Algne jääk: {minu_konto.kysi_jaak()} €")
    
 
    minu_konto.pane_raha(25.50)
    print(f"Pärast 25.50 € lisamist on jääk: {minu_konto.kysi_jaak()} €")
    
    
    edukas = minu_konto.vota_raha(100.0)
    print(f"Kas 100 € võtmine õnnestus? {edukas}")
    
   
    edukas = minu_konto.vota_raha(30.0)
    print(f"Kas 30 € võtmine õnnestus? {edukas}")
    print(f"Lõplik jääk: {minu_konto.kysi_jaak()} €\n")



class TestDigiRahakott(unittest.TestCase):
    
    def setUp(self):
        """Käivitatakse enne igat testi. Loob värske rahakoti."""
        self.kott = DigiRahakott(100.0)

    def test_algne_jaak(self):
        """Kontrollib, kas algne jääk määratakse õigesti."""
        self.assertEqual(self.kott.kysi_jaak(), 100.0)

    def test_raha_lisamine(self):
        """Kontrollib, kas raha lisamine suurendab jääki."""
        self.kott.pane_raha(50.0)
        self.assertEqual(self.kott.kysi_jaak(), 150.0)

    def test_raha_votmine_edukas(self):
        """Kontrollib, kas korrektse summa võtmine õnnestub ja vähendab jääki."""
        onnestus = self.kott.vota_raha(40.0)
        self.assertTrue(onnestus)
        self.assertEqual(self.kott.kysi_jaak(), 60.0)

    def test_raha_votmine_liiga_palju(self):
        """Kontrollib, et liiga suurt summat ei lubata võtta ja jääk ei muutu."""
        onnestus = self.kott.vota_raha(150.0)
        self.assertFalse(onnestus)
        self.assertEqual(self.kott.kysi_jaak(), 100.0) 



if __name__ == "__main__":
  
    naitprogramm()
    
  
    print("=== Automaattestide käivitamine ===")
    unittest.main()
