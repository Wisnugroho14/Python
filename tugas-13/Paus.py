from Animal import *
class Paus(Animal):
    def __init__(self,name,makanan,hidup,berkembang_biak,habitat,panjang):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.panjang = panjang
    def cetak(self):
        super().cetak()
        print(f"Habitatnya di {self.habitat}")
        print(f"panjang {self.panjang}")
    def bernapas(self):
        print(f"{self.name} bernapas dengan Paru-Paru.")
    def berenang(self):
        print(f"{self.name} berenang dengan sirip.")