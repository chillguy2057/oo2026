
class Kosmosesond:
    def __init__(self, nimi: str, sihtkoht: str):
        self.nimi = nimi
        self.sihtkoht = sihtkoht
        self.energia_protsent = 100  
        self.kogutud_andmed_gb = 0   

    def tee_teadustood(self, tundide_arv: int):
        """Sond teeb uurimistööd, mis kulutab energiat ja kogub andmeid."""
        energia_kulu = tundide_arv * 12
        if self.energia_protsent - energia_kulu >= 0:
            self.energia_protsent -= energia_kulu
             self.kogutud_andmed_gb += tundide_arv * 5
            print(f"[{self.nimi}] Töötas {tundide_arv} tundi sihtkohas {self.sihtkoht}.")
        else:
            print(f"[{self.nimi}] HOIATUS: Teadustöö tühistatud! Liiga vähe energiat.")

    def lae_päikesepaneele(self, laadimisaeg_h: int):
        """Päikesepaneelid taastavad sondi energiat."""
        self.energia_protsent = min(100, self.energia_protsent + (laadimisaeg_h * 15))
        print(f"[{self.nimi}] Laadis paneele {laadimisaeg_h} tundi.")

    def anna_staatus(self):
        """Tagastab sondi hetkeseisu."""
        return (f"Sond: {self.nimi} | Sihtkoht: {self.sihtkoht} | "
                f"Energia: {self.energia_protsent}% | Andmed: {self.kogutud_andmed_gb} GB")



if __name__ == "__main__":
    print("=== Kosmosesondide juhtimiskeskus ===\n")

   
    sond_mars = Kosmosesond("Curiosity_2", "Mars")
    sond_jupiter = Kosmosesond("Juno_X", "Jupiter")

    
    print("Algne seis:")
    print(sond_mars.anna_staatus())
    print(sond_jupiter.anna_staatus())
    print("-" * 60)

    
    print("Tegevused Marsi sondiga:")
    sond_mars.tee_teadustood(4)  
    sond_mars.tee_teadustood(5)  
    print(sond_mars.anna_staatus())
    print("-" * 60)

   
    print("Tegevused Jupiteri sondiga:")
    sond_jupiter.tee_teadustood(2)
    sond_jupiter.lae_päikesepaneele(3)  
    print(sond_jupiter.anna_staatus())
    print("-" * 60)

   
    print("Lõplik seisund juhtimiskeskuses:")
    print(sond_mars.anna_staatus())
    print(sond_jupiter.anna_staatus())
