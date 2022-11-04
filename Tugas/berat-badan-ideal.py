#input
print ("program menghitung berat badan ideal")
tinggiBadan = input ("masukkan tinggi badan (centimeter): ")

#rumus
beratBadanideal = (int (tinggiBadan) - 100) - ((int (tinggiBadan) - 100) * 10/100)

#0utput
print ("berat badan ideal dari tinggi", tinggiBadan, "adalah : ", beratBadanideal, "Kg")

