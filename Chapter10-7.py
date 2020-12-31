myfile = open('teks_hasil_sandi.txt', 'w')
teks = input('Masukkan Teks Sandi             : ')
n = input('Jumlah huruf yang telah digeser : ')
teks_sandi = teks +'\nNilai n = '+ str(n)
myfile.write(teks_sandi)

#decyphering proccess
teks = list(teks)
h = 0
teks_asli = []
for huruf in teks :
    alphabet = teks[h]
    if alphabet != ' ':
        asci = ord(str(alphabet))
        asci = int(asci) - int(n)
        if asci < 65 :
            asci_angka = 90 - (64 - asci)
        else:
            asci_angka = asci
        asci_asli = chr(asci_angka)
        teks_asli.append(asci_asli)
    else :
        asci_asli = ' '
        teks_asli.append(asci_asli)
    h += 1

#ouput
newfile = open('teks_asli_hasil_sandi', 'w')
newfile.write(''.join(teks_asli))