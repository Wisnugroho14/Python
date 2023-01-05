#Program untuk menampilkan bintang bintang segitiga

#Fungsi untuk menampilkan bintang bintang segitiga
def segitiga_bintang(tinggi):
  for i in range(tinggi):
    for j in range(i + 1):
      print("*", end="")
    print()

#Fungsi untuk menampilkan segitiga terbalik 
def segitiga_terbalik(tinggi):
  for i in range(tinggi):
    for j in range(tinggi - i - 1):
      print("*", end="")
    print()

#Tinggi segitiga
tinggi = 6

#Tampilkan segitiga bintang 
segitiga_bintang(tinggi)

#Tampilkan segitiga terbalik
segitiga_terbalik(tinggi)