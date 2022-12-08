def biodata(nama, alamat, tanggal, umur, tinggi_badan):
    bb_ideal = str((int(tinggi_badan) - 100) - ((int(tinggi_badan)- 100) * 0.10))
    print('Nama              : '+ nama)
    print('Alamat            : '+ alamat)
    print('Tanggal Lahir     : '+ tanggal)
    print('Umur              : '+ umur)
    print('Tinggi Badan      : '+ tinggi_badan)
    print('Berat Badan Ideal : '+ bb_ideal)

biodata("Wisnu Nugroho","Kp. Kelapa Dua RT005 RW009 Tugu Cimanggis Depok","14 Januari 2004","18","182")