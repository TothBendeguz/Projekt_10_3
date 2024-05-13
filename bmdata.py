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

def ora(ev):
    perces = ev*365*24*60
    print(f'{nev} {perces} perces')

def ora(ev):
    másodperces = ev*365*24*60*60
    print(f'{nev} {másodperces} másodperces')

nap(ev)