def read(source):
    file = open(source, 'r')
    ganjil = 0
    genap = 0
    i = 0
    file_ini = file.readlines()
    for lists in file_ini:
        if int(file_ini[i]) % 2 == 0 :
            genap += 1
        else:
        	ganjil += 1
        	
        i +=1
        
    file.close()
    result = {"ganjil" : ganjil, 
              "genap" : genap}
    return result

source = "Chapter10_1.txt"
print("Banyaknya Bilangan Ganjil: ", read(source).get('ganjil'))
print("Banyaknya Bilangan Genap: ", read(source).get('genap'))