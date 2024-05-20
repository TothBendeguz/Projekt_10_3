egyenleg = 0

def egyenleg_lekérdezése():
    global egyenleg
    print(f"\nAz aktuális egyenleg: {egyenleg}\n")

def tranzakcio_tipus():
    tipus = None
    while tipus not in ["Befizetés", "Kivétel"]:
        tipus = input("\nMilyen típusú tranzakciót szeretne végrehajtani? [Befizetés/Kivétel]: \n").strip()
        if tipus not in ["Befizetés", "Kivétel"]:
            print("\nÉrvénytelen tranzakció típus, kérem válasszon Befizetés vagy Kivétel!\n")
    return tipus

def osszeg_bekeres():
    osszeg = None
    while osszeg is None or osszeg <= 0:
        osszeg_input = input("\nAdja meg a tranzakció összegét: \n")
        if osszeg_input.isdigit():
            osszeg = int(osszeg_input)
            if osszeg <= 0:
                print("\nKérem, egy pozitív egész számot adjon meg!\n")
        else:
            print("\nÉrvénytelen bemenet, kérem, egy számot adjon meg!\n")
    return osszeg

def main():
    global egyenleg
    kilep = 'N'
    while kilep != 'I':
        tipus = tranzakcio_tipus()
        osszeg = osszeg_bekeres()
        if tipus == "Befizetés":
            egyenleg += osszeg
        elif tipus == "Kivétel":
            egyenleg -= osszeg
        egyenleg_lekérdezése()
        kilep = input("\nKi szeretne lépni [I/N]? \n").strip().upper()

main()

