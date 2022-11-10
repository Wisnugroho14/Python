#Buat Program untuk pemesanan makanan
#Input
namaPembeli = input("Masukkan Nama Pembeli = ")
noHp = input("Masukkan No.Hp Pembeli = ")
pesanMenu = input("Pesan Menu Apa = ")
#Proses Pesan Menu

if pesanMenu == 'makanan':
    print("Nasi Goreng = Rp 15.000")
    print("Mie Goreng = Rp 12.000")
    print("Ayam Geprek = Rp 18.000")
elif pesanMenu == 'minuman':
    print("Aneka Jus = Rp 15.000")
    print("Soft Drink = Rp 10.000")
    print("Sweet Ice Tea = Rp 5.000")
pesanan = input('Masukkan Pesanan = ')
jumlahpesanan = int(input("Masukkan Jumlah Pesanan? "))

#Proses
#----------Makanan------------
if pesanan == 'nasi goreng':
    harga = 15000 * jumlahpesanan
elif pesanan == 'mie goreng':
    harga = 12000 * jumlahpesanan
elif pesanan == 'ayam geprek':
    harga = 18000 * jumlahpesanan
#----------Minuman------------
if pesanan == 'aneka jus':
    harga = 15000 * jumlahpesanan
elif pesanan == 'soft drink':
    harga = 10000 * jumlahpesanan
elif pesanan == 'sweet ice tea':
    harga = 5000 * jumlahpesanan

#Output
print("==========================================")
print("Nama Pembeli =",namaPembeli)
print("No Hp Pembeli =",noHp)
print("Menu yang di Pesan =",pesanan)
print("Jumlah pesanan =",jumlahpesanan)
print("Harga yang harus di bayarkan =",harga)