#input
print ("program konversi suhu dari celcius ke fahrenheit ke reamur")
celcius = input ("masukkan suhu celcius =")

#rumus
fahrenheit = int(9)/int(5) * int(celcius) + int(32)
reamur = (int(fahrenheit) - int(32)) * int(4)/int(9)

#output
print ("hasil dari celcius ke fahrenheit adalah ", fahrenheit)
print ("hasil dari celcius ke fahrenheit ke reamur adalah ", reamur)
