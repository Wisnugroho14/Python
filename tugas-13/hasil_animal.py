from Animal import *
from Badak import *
from Paus import *
from Ular import *

# Objek
b1 = Badak('Badak Jawa','Buah','Darat','Melahirkan','Dataran Rendah','> 1 ton')
b1.cetak()
b1.bernapas()
b1.karakteristik()

print("="*50)

i1 = Paus('Paus Biru','Plankton','Laut','Melahirkan','Perairan Terbuka','23 - 24 cm')
i1.cetak()
i1.bernapas()
i1.berenang()

print("="*50)

u1 = Ular('Ular Cobra','Tikus','Amphibi','Bertelur','Sawah & Hutan','1-75 kg')
u1.cetak()
u1.bernapas()
u1.berbisa()