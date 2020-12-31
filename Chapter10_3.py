myfile = open('Chapter10_2-DataMHS.txt', 'r')
list_data = myfile.readlines()
i = 0
BuatList = []
for data in list_data:
    data_mhs = str(list_data[i])
    data_mhs = data_mhs.split('|')
    BuatList.append(data_mhs)
    i += 1

dataMhs = {}
ket = 0
for data in BuatList:
    d = {}
    d['nim'] = BuatList[ket][0]
    d['nama'] = BuatList[ket][1]
    d['alamat'] = str.rstrip(BuatList[ket][2])
    dataMhs[str(ket+1)] = d    
    ket += 1

print('Data Mhs= ', dataMhs)