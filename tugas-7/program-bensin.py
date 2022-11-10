#Buat Program harga bensin ke kota tujuan
pLite = 10000
pMax = 14000
pTurbo = 17000

jTempuhPLite = 12
jTempuhPMax = 13
jTempuhPTurbo = 13.5

jakarta = 20
bekasi = 35.7
depok = 5
tangerang = 99
bogor = 120.6

#Input
namaKendaraan = input("Nama Kendaraan =  ")
jBensin = input("Jenis Bensin =  ")
KotaTujuan = input("Kota yang dituju =  ")

#Proses
if (jBensin == 'pertalite'):
    hasilPakai = eval(KotaTujuan) / jTempuhPLite
    totalHarga = hasilPakai * pLite
elif (jBensin == 'pertamax'):
    hasilPakai = eval(KotaTujuan) / jTempuhPMax
    totalHarga = hasilPakai * pMax
elif (jBensin == 'pertamax turbo'):
    hasilPakai = eval(KotaTujuan) / jTempuhPTurbo
    totalHarga = hasilPakai * pTurbo
else :
    print('ERROR')

#Rounding
hasilPakai = round(hasilPakai, 2)
totalHarga = round(totalHarga)

#Output
print("==========================================")
print("Nama Kendaraan = ",namaKendaraan)
print("Jenis Bensin = ",jBensin)
print("Kota yang dituju = ",KotaTujuan)
print("Pemakaian Bensin =",hasilPakai,"L")
print("Total Harga dari Bensin = ","Rp",totalHarga)