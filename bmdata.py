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

nap(ev)