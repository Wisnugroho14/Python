#Tugas2

baris = int(input("Jumlah Baris Yang Ingin diulang: "))
for i in range (baris) :
  for j in range (i+1) :
    print ("*", end="")
  print ("")