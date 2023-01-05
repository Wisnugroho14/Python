from Kantin import *

kantin = Kantin()

print(f'='*40)
konsumen1 = Konsumen('Wisnu', 50000)
konsumen1.pesan(kantin, {'Ayam Goreng': 2, 'Mie Goreng': 1,'Kopi': 1})

print(f'='*40)
konsumen2 = Konsumen('Khadaffi', 50000)
konsumen2.pesan(kantin, {'Ayam Goreng': 2, 'Mie Goreng': 1,'Susu': 1})

print(f'='*40)
konsumen3 = Konsumen('Saiful', 1000)
konsumen3.pesan(kantin, {'Ayam Goreng': 2, 'Mie Goreng': 1,'Teh Manis': 1})