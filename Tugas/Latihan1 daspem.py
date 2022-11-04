#Input
namamahasiswa = input(" Nama Mahasiswa : ")
jurusan = input(" Jurusan [SI/SIA/ILKOM] : ")
nim = input(" NIM : ")

#Proses
if jurusan == "SI":
    namaprodi = "Sistem Informasi"
    harga = 2400000
elif jurusan == "SIA":
    namaprodi = "Sistem Informasi Akuntansi"
    harga = 2000000
else : 
    jurusan == "ILKOM"
    namaprodi = "Ilmu Komputer"
    harga = 2500000

#Hasil
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("         UNIVERSITAS BINA SARANA INFORMATIKA")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Nama Mahasiswa : "+str(namamahasiswa))
print("Jurusan : "+str(jurusan))
print("NIM Mahasiswa : "+str(nim))
print("Harga : ",+(harga))
uangbayar = int(input("Masukkan Uang Bayar : "))
uangkembali = uangbayar - harga
print("Uang Kembali : ",+uangkembali)