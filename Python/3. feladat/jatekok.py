from jatek import *

jatekok: list[Jatek] = []

f = open('jatekok.csv', 'r', encoding='utf-8')
f.readline()
for sor in f:
    jatekok.append(Jatek(sor))
f.close()

print(f'3. feladat: {len(jatekok)} játékot értékesítettek.')

legtobbetEladott = jatekok[0]
for j in jatekok:
    if j.eladott > legtobbetEladott.eladott:
        legtobbetEladott = j
print(f'4. feladat: A legtöbbet értékesített játék: {legtobbetEladott.nev}')

for j in jatekok:
    if j.ar >= 7500:
        print(f'5. feladat: A játékok, amelyek ára 7500-nál nagyobb: {j.nev}')