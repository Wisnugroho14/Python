#Membalik Nama

def balik_Kalimat(kata):
    kata = kata.split()
    backward = ""
    for i in range(len(kata)):
        i += 1
        backward = backward + kata[-i] + " "
    return backward

print(balik_Kalimat("saya mahasiswa Nurul Fikri"))
print(balik_Kalimat("saya prodi Teknik Informatika"))
print(balik_Kalimat("Pemrograman Dasar Menyenangkan"))