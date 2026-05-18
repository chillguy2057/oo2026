
class Soiduk:
    def __init__(self, tootja: str, tippkiirus: int):
        self.tootja = tootja
        self.tippkiirus = tippkiirus

    def liigu(self):
        return f"{self.tootja} sõidab kiirusega kuni {self.tippkiirus} km/h."

    def anna_info(self):
        return f"Sõiduki tootja: {self.tootja}, tippkiirus: {self.tippkiirus} km/h"



class Auto(Soiduk):
    def __init__(self, tootja: str, tippkiirus: int, uste_arv: int):
       
        super().__init__(tootja, tippkiirus)
        self.uste_arv = uste_arv 

   
    def liigu(self):
        return f"Auto {self.tootja} veereb maanteel stabiilselt kiirusega {self.tippkiirus} km/h."

    def anna_info(self):
       
        return f"{super().anna_info()}, uksi: {self.uste_arv}"



class E_Auto(Auto):
    def __init__(self, tootja: str, tippkiirus: int, uste_arv: int, aku_mahtuvus: int):
       
        super().__init__(tootja, tippkiirus, uste_arv)
        self.aku_mahtuvus = aku_mahtuvus 
    
    def liigu(self):
        return f"Elektriauto {self.tootja} kiirendab hääletult tippkiiruseni {self.tippkiirus} km/h."

    def anna_info(self):
        return f"{super().anna_info()}, aku mahtuvus: {self.aku_mahtuvus} kWh"

    
    def lae_akut(self):
        return f"Laen {self.tootja} akut mahuga {self.aku_mahtuvus} kWh... Laetud!"



if __name__ == "__main__":
    print("=== Alamklasside puu demonstratsioon (Pärilus) ===\n")


    tavaline_soiduk = Soiduk("GeneerilineTehas", 60)
    print("1. Ülemklassi eksemplar:")
    print(tavaline_soiduk.anna_info())
    print(tavaline_soiduk.liigu())
    print("-" * 50)

    
    bensiini_auto = Auto("Audi", 220, 5)
    print("2. Esimese taseme alamklass (Auto):")
    print(bensiini_auto.anna_info())
    print(bensiini_auto.liigu())
    print("-" * 50)

   
    tesla = E_Auto("Tesla", 250, 4, 85)
    print("3. Teise taseme alamklass (Elektriauto):")
    print(tesla.anna_info()) 
    print(tesla.liigu())     
    print(tesla.lae_akut())  
    print("-" * 50)
