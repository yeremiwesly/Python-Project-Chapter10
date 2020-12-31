#Hasil di run

source = "Chapter10_5-Bil1+Bil2.txt"
data = open(source,"r")
for i in data:
    i = i.split('|')
    result = int(i[0])+int(i[1])
    print(result)
data.close()

#Hasil di file baru

myfile = open('Chapter10_5-Bil1+Bil2.txt', 'r')
daftar_data = myfile.readlines()
i = 0
ListBaru = []
for data in daftar_data:
    data_angka = str(daftar_data[i])
    data_angka = data_angka.split('|')
    ListBaru.append(data_angka)
    i += 1

FileBaru = open('Chapter10_5-Jawaban.txt', 'w')
y = 0
for angka in ListBaru:
    angka1 = int(ListBaru[y][0])
    angka2 = int(ListBaru[y][1])
    FileBaru.write(str(angka1+angka2)+'\n')
    y += 1