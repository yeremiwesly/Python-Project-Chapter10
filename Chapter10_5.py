source = "bilangan.txt"
data = open(source,"r")
for i in data:
    i = i.split('|')
    result = int(i[0])+int(i[1])
    print(result)
data.close()