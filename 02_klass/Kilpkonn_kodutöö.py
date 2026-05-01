class Kilpkonn: 
  def __init__(self)
  self.x = x
  self.y = y
  self.suund = "paremale"
  
 def keeraParemale(self)
  if self.suund == "paremale":
    self.suund = "alla"
elif self.suund == "alla":
 self.suund = "vasakule"
elif self.suund == "vasakule":
 self.suund = "yles"
elif self.suund == "yles":
self.suund = "paremale"

def edasi(self) 
 if self.suund == "paremale":
  self.x  += 1
elif self.suund = "yles":
 self.y += 1
elif self.suund = "vasakule"
 self.x -= 1
elif self.suund = "alla"
 self.y -= 1

k1 = kilpkonn(0;0)
k2 = kilpkonn(10;10)

k1.edasi()
k2.keeraParemale()
k1.edasi()

print("Esimene kilpkonn:", k1.kysi_koordinaadid())
print("Teine kilpkonn:", k2.kysi_koordinaadid())

