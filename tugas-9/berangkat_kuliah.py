def berangkat_kuliah():
  kondisiCuaca = input("Jika Cuaca Hari Ini : ")
  def status():
    if (kondisiCuaca == "hujan"):
        berangkat = "Maka berangkat naik Gocar"
    elif (kondisiCuaca == "adem"):
        berangkat = "Maka berangkat naik Motor"
    return berangkat
  print ("Jika kondisi cuaca %s" ": %s" %(kondisiCuaca,status()))
berangkat_kuliah()