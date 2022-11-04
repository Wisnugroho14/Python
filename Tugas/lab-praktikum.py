#inputan
nama  = input ("Masukkan nama anda = ")
kelas = input ("Masukkan kelas anda = ")
lab   = input ("Bagaimana kondisi lab sekarang = ")

#proses
print("===========================")
if lab =="tersedia":
  ket="Praktikum"
elif lab =="penuh":
  ket="Pindah jadwal"
else :
  ket="tidak jadi praktikum"

#output
print("===========================")
print("Nama saya adalah  = ",nama)
print("Kelas saya adalah = ",kelas)
print("Kondisi lab hari ini = ",lab)
print("Maka kamu harus = ",ket)