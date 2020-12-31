def inputMhs(source,nim,nama,almt):
    tambah = open(source, "a")
    tambah.write("{} | {} | {} \n".format(nim,nama,almt))
    tambah.close()
def viewMhs(source):
    liat = open(source, 'r')
    for i in liat:
        print(i)
    liat.close()
    
source = "Chapter10_2-DataMHS.txt"    
again = "y"
while again == "y":
    nim    = input("Masukkan NIM            :")
    nama   = input("Masukkan Nama Mhs       :")
    alamat = input("Masukkan Alamat         :")
    inputMhs(source,nim,nama,alamat)
    again  = input("Ulangi input lagi (y/n) :")

if again != "y":
    print("Data Mahasiswa")
    viewMhs(source)