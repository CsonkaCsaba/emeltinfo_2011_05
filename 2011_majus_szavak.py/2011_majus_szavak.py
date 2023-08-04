szo_input = input('1. feladat: Adjon meg egy szót: ')
mgh = ['a', 'e', 'i', 'o', 'u']
van = 0
for elem in mgh:
    if elem in szo_input:
        van = 1
if van:
    print('Van benne magánhangzó.')
else:
    print('Nincs benne magánhangzó.')

#2. feladat
szavak = []
forras = open('szoveg.txt')
for sor in forras:
    szavak.append(sor.strip())
forras.close()
print('2. feladat: A leghosszabb szó:', sorted(szavak, key=lambda x: len(x), reverse = True)[0])
print('hossza:', len(sorted(szavak, key=lambda x: len(x), reverse = True)[0]), 'betű')

#3. feladat
tobb_mgh = []
szoban_mgh = 0
for szo in szavak:
    for ch in szo:
        if ch in mgh:
            szoban_mgh += 1
    if (len(szo)-szoban_mgh) < szoban_mgh:
        tobb_mgh.append(szo)
    szoban_mgh = 0
print('több magánhangzó:', end="")
for szo in tobb_mgh:
    print("", szo, end="")
print("")
print(len(tobb_mgh), '/', len(szavak), ' : ', round(len(tobb_mgh)/len(szavak)*100, 2), '%', sep="")

#4. feladat

szo_5betu = []
for szo in szavak:
    if len(szo) == 5:
        szo_5betu.append(szo)
szo_3ch_input = input('adjon meg egy 3 karakteres szórészletet: ')

print('ebből építhető:', end="")
for szo in szo_5betu:
    if szo[1:4] == szo_3ch_input:
        print("", szo, end="")
print("")

#6. feladat
kimenet = open('letra.txt', 'w')
szoreszlet3 = set()
for szo in szo_5betu:
    szoreszlet3.add(szo[1:4])

letraszavak = []
szo1_letraszavak = []
for elem in szoreszlet3:
    for szo in szo_5betu:
        if elem == szo[1:4]:
            szo1_letraszavak.append(szo)
    letraszavak.append(szo1_letraszavak)
    szo1_letraszavak = []
for elem in letraszavak:
    if len(elem) != 1:
        for szo in elem:
            print(szo, file=kimenet)
        print("", file=kimenet)
kimenet.close()
