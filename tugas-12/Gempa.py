class Gempa:
  #Variabel Property
  lokasi = ""
  skala = 0

  #Konstruktor 
  def __init__ (self, lokasi, skala):
    self.lokasi = lokasi
    self.skala = skala 
  
  #Method 
  def dampak (self): 
    if (self.skala < 2): ket = "Tidak Berasa"
    elif (self.skala >= 2 and self.skala <4): ket = "Bangunan Retak-retak"
    elif (self.skala >= 4 and self.skala <6): ket = "Bangunan Roboh"
    else: ket = "Bangunan Roboh dan Berpotensi Tsunami"
    print (
      "Lokasi Gempa\t:",self.lokasi, "\nSkala\t\t:",self.skala, "Richter", "\nDampak\t\t:",ket,"\n-----------------------------"
    ) 