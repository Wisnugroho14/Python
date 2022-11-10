#inputan
nama = input ("Masukan nama anda = ")
kelas = input ("Masukkan kelas anda = ")
nilai = int (input ("Masukkan nilai anda = "))


#proses
print ("==========================================")
if nilai < 101 and nilai > 89:
  ket="Istimewa"
elif nilai < 90 and nilai > 69:
  ket="Sangat bagus"
elif nilai < 70 and nilai > 59:
  ket="Cukup"
else :
  ket="Gagal"

#output
print("Nama saya adalah = ",nama)
print("Kelas saya adalah = ",kelas)
print("Nilai saya adalah = ",nilai)
print("Keterangan nilai saya adalah = ",ket)
print ("==========================================")
