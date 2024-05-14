nev = ''
while nev == '':
    nev = input("Hogy hívják önt?: >> ")
ev = ''
while ev == '':
    ev = int(input("Hány éves ön?: >> "))
    if ev <= 0:
        print('Meg sem született.')

def nap(ev):
    napos = ev*365
    print(f'{nev} {napos} napos')

def ora(ev):
    oras = ev*365*24
    print(f'{nev} {oras} órás')

def perc(ev):
    perces = ev*365*24*60
    print(f'{nev} {perces} perces')

def masodperc(ev):
    masodperces = ev*365*24*60*60
    print(f'{nev} {masodperces} másodperces')

nap(ev)