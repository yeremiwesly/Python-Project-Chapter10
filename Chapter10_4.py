myfile = open('Chapter10_2-DataMHS.txt', 'r')
list_data = myfile.readlines()
i = 0
BuatList = []
for data in list_data:
    data_mhs = str(list_data[i])
    data_mhs = data_mhs.split('|')
    BuatList.append(data_mhs)
    i += 1

find = input('Masukkan NIM yang mau dicari : ')

Input = False
x = 0
for lists in BuatList:
    if find in BuatList[x]:
    	y = 0
    	for lists in BuatList:
    		if find == BuatList[y][0]:
    			print(' Data Mahasiswa' )		
    			print(' NIM	: '+ BuatList[y][0])
    			print(' Nama	: '+ BuatList[y][1])
    			print(' Alamat	: '+ BuatList[y][2])
    			Input = True
    			break
    		else:
    			y += 1
    	x += 1
    if Input == False :
    	print('Data mahasiswa tidak ditemukan')