#inputan
nama = input ("Masukan nama anda = ")
kelas = input ("Masukkan kelas anda = ")
nilai = int (input ("Masukkan nilai anda = "))


#proses
print ("==========================================")
if nilai >=90:
  ket="Istimewa"
elif nilai >=70:
  ket="Sangat bagus"
elif nilai >=60:
  ket="Cukup"
elif nilai <60:
  ket="Gagal"

#output
print("Nama saya adalah = ",nama)
print("Kelas saya adalah = ",kelas)
print("Nilai saya adalah = ",nilai)
print("Keterangan nilai saya adalah = ",ket)
print ("==========================================")