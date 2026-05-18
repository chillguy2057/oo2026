
class Nutiseade:
    def __init__(self, nimi: str, tuup: str):
        self.nimi = nimi
        self.tuup = tuup
        self.on_sisse_lulitatud = False  

    def lulita_sisse(self):
        self.on_sisse_lulitatud = True
        print(f"[{self.nimi}] on nüüd SISSE lülitatud.")

    def lulita_valja(self):
        self.on_sisse_lulitatud = False
        print(f"[{self.nimi}] on nüüd VÄLJA lülitatud.")

    def anna_info(self):
        olek = "SEES" if self.on_sisse_lulitatud else "VÄLJAS"
        return f"{self.nimi} ({self.tuup}) -> Olek: {olek}"



class Nutikodu:
    def __init__(self, kodu_nimi: str):
        self.kodu_nimi = kodu_nimi
       
        self.seadmed = []

    def lisa_seade(self, seade: Nutiseade):
        """Lisab uue seadme süsteemi hoidlasse"""
        self.seadmed.append(seade)
        print(f"Nutikoju '{self.kodu_nimi}' lisati seade: {seade.nimi}")

    def kuva_seadmete_nimekiri(self):
        """Käib läbi kogu hoidla ja kuvab iga eksemplari info"""
        print(f"\n--- {self.kodu_nimi} seadmete hetkeseis ---")
        if not self.seadmed:
            print("Kodus pole ühtegi nutiseadet.")
        else:
            for seade in self.seadmed:
                print(seade.anna_info())
        print("-" * 40)

    def lulita_koik_valja(self):
        """Hariv/kasulik funktsioon: lülitab energiasäästuks kõik seadmed korraga välja"""
        print(f"\n[Käsk: Lülita kõik välja] Süsteem lülitab välja kõik seadmed asukohas {self.kodu_nimi}...")
        for seade in self.seadmed:
            if seade.on_sisse_lulitatud:
                seade.lulita_valja()



if __name__ == "__main__":
    print("=== Nutikodu Klassikomplekti Käivitamine ===\n")

    
    minu_korter = Nutikodu("Tallinna Kesklinna Korter")

    
    lamp_elutuba = Nutiseade("Elutoa põhilamp", "Valgusti")
    konditsioneer = Nutiseade("Köögi kliimaseade", "Kliima")
    tv = Nutiseade("Magamistoa teler", "Meelelahutus")

    
    print("--- Seadmete registreerimine süsteemis ---")
    minu_korter.lisa_seade(lamp_elutuba)
    minu_korter.lisa_seade(konditsioneer)
    minu_korter.lisa_seade(tv)
    
    
    minu_korter.kuva_seadmete_nimekiri()

    
    print("--- Seadmete käsitsi juhtimine ---")
    lamp_elutuba.lulita_sisse()
    konditsioneer.lulita_sisse()
    
    
    minu_korter.kuva_seadmete_nimekiri()

   
    minu_korter.lulita_koik_valja()

   
    minu_korter.kuva_seadmete_nimekiri()
