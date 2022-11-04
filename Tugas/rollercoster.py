#inputan
nama   = input ("Masukkan nama anda = ")
umur   = int (input ("Masukkan umur anda = "))
tinggi = int (input ("Masukkan tinggi anda = "))

#proses
print("==========================")
if tinggi >=90:
    ket="boleh bermain"
else:
  ket="tidak boleh bermain"

#output
print("==========================")
print("Nama saya adalah ",nama)
print("Umur saya adalah ",umur)
print("Tinggi saya adalah ",tinggi)
print("Saya dinyatakan ",ket)