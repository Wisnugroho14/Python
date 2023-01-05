class Kantin:
  def __init__(self):
    self.menu_makanan = {
      'Ayam Goreng': 10000,
      'Nasi Goreng': 8000,
      'Mie Goreng': 7000,
      'Bakso': 9000,
      'Sate': 11000
    }
    self.menu_minuman = {
      'Teh Manis': 3000,
      'Kopi': 4000,
      'Susu': 5000,
      'Jus Jeruk': 6000,
      'Jus Mangga': 7000
    }
  
  def cetak_struk(self, nama, uang, pesanan):
    total_harga = 0
    for p in pesanan:
      total_harga += p['harga']
    print(f'Nama: {nama}')
    print('Pesanan:')
    for p in pesanan:
      print(f'{p["nama"]} {p["jumlah"]} x {p["harga"]} = {p["jumlah"] * p["harga"]}')
    print(f'Total harga: {total_harga}')
    print(f'Uang yang dibawa: {uang}')
    print(f'Kembalian: {uang - total_harga}')

class Konsumen:
  def __init__(self, nama, uang):
    self.nama = nama
    self.uang = uang
  
  def pesan(self, kantin, pesanan):
    items = []
    for p in pesanan:
      item = {
        'nama': p,
        'jumlah': pesanan[p],
        'harga': kantin.menu_makanan[p] if p in kantin.menu_makanan else kantin.menu_minuman[p]
      }
      items.append(item)
    
    total_harga = 0
    for item in items:
      total_harga += item['jumlah'] * item['harga']
    
    if total_harga > self.uang:
      print('Maaf, uang Anda tidak cukup.')
    else:
      kantin.cetak_struk(self.nama, self.uang, items)