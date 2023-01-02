
from polja import *


def izbor():
    print("")
    print("Izaberite jednu od opcija: ")
    print("")
    print("1. Vi igrate prvi")
    print("2. Racunar igra prvi")
    
    while True:
        iz = input(">>> ")
        if iz not in ("1","2"):
            print("Izabrali ste pogresnu opciju. ")
        else:
            break
    if iz == 1:
        igra(sva_polja)
    elif iz == 2:
        igra2(sva_polja)

if __name__ == '__main__':
    izbor()

