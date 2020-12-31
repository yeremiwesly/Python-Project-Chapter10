myfile = open('teks_asli.txt', 'w')
teks = input('Masukkan Teks Asli              : ')
n = input('Jumlah huruf yang ingin digeser : ')
teks_asli = teks +'\nNilai n = '+ str(n)
myfile.write(teks_asli)

#decyphering procces
teks = list(teks)
h = 0
teks_baru = []
for huruf in teks :
    alphabet = teks[h]
    if alphabet != ' ':
        asci = ord(str(alphabet))
        asci = int(asci) + int(n)
        if asci > 90 :
            asci_angka = asci - 90 + 64
        else:
            asci_angka = asci
        asci_baru = chr(asci_angka)
        teks_baru.append(asci_baru)
    else :
        asci_baru = ' '
        teks_baru.append(asci_baru)
    h += 1

#ouput
newfile = open('teks_sandi.txt', 'w')
newfile.write(''.join(teks_baru))