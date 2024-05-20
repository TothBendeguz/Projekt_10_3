egyenleg = 0

def egyenleg_lekérdezése():
    global egyenleg
    print(f"\nAz aktuális egyenleg: {egyenleg}\n")

def tranzakcio_tipus():
    tipus = None
    while tipus not in ["Befizetés", "Kivétel"]:
        
        if tipus not in ["Befizetés", "Kivétel"]:
            print("\nÉrvénytelen tranzakció típus, kérem válasszon Befizetés vagy Kivétel!\n")
    return tipus

def osszeg_bekeres():
    osszeg = None
    while osszeg is None or osszeg <= 0:

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
            
        elif tipus == "Kivétel":
            
        
        

main()

