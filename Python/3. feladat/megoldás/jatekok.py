from jatek import *

jatekok: list[Jatek] = []

f = open('jatekok.csv', 'r', encoding='utf-8')
f.readline()
for sor in f:
    jatekok.append(Jatek(sor))
f.close()

print(f'3. feladat: {len(jatekok)} játékot értékesítettek.')

ossz = 0
for j in jatekok:
    ossz += j.ar
print(f'4. feladat: Az összes bevétel: {ossz} Ft.')

legtobbetEladott = jatekok[0]
for j in jatekok:
    if j.eladott > legtobbetEladott.eladott:
        legtobbetEladott = j
print(f'5. feladat: A legtöbbet értékesített játék: {legtobbetEladott.nev} amiből {legtobbetEladott.eladott} db-t adtak el.')

print("6. feladat: 2019 után kiadott játékok:", ", ".join([jatek.nev for jatek in jatekok if jatek.ev > 2019]))

keresettJatek = input('7. feladat: Keresett játék neve: ')
for j in jatekok:
    if j.nev == keresettJatek:
        print(f'A(z) {keresettJatek} játék {j.tipus} játék.')
        break
else:
    print(f'Nincs ilyen játék.')

with open('fps_jatekok.csv', 'w') as f:
    f.write("Játéknév;Eladott mennyiség;db Ár forintban;Kiadási év;Kategória\n")
    for jatek in jatekok:
        if jatek.tipus == 'FPS':
            f.write(';'.join([jatek.nev, str(jatek.eladott), str(jatek.ar), str(jatek.ev), jatek.tipus])+'\n')
    print(f'8. feladat: Az fps_jatekok.csv fájl elkészült.')
