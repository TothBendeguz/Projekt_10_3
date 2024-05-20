import math

a = float(input('Adja meg a téglalap "a" oldalát cm-ben: '))
b = float(input('Adja meg a téglalap "b" oldalát cm-ben: '))

d = math.sqrt(a**2 + b**2)
k = 2*(a+b)
t = a*b

print(f'\nA(z) {a} cm és {b} cm oldalú téglalap:')
print(f'\tÁtlója: {d:.2f} cm')
print(f'\tKerülete: {k:.2f} cm')
print(f'\tTerülete: {t:.2f} cm^2')