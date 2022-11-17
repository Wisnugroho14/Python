print("Program Membuat Kalkulator")

#Input
print('=========================' )
a = int(input("Masukkan angka pertama = "))
b = int(input("Masukkan angka kedua = "))

print('=========================')
print('Pilihan Operator')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Bagi \t [/]')
print('  4. Kali \t [*}')
print('  5. Pangkat \t [**]')
print('  *Noted : Jika Pangkat angka kedua nya dikasih angka 0')
operator = input("Masukkan pilihan operator = ")

print('=========================')

#Proses
if operator == '1':
    hasil = a + b
elif operator == '2':
    hasil = a - b
elif operator == '3':
    hasil = a / b
elif operator == '4':
    hasil = a * b
elif operator == '5':
    hasil = a **2
else:
  print('Tidak Sesuai')

#Output
print("Angka pertama = ", a)
print("Angka kedua = ", b)
print("Pilihan Operator = ", operator)
print("Hasil Operator = ", hasil)