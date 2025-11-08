import time
from sympy import symbols, sqrt, sympify

delta = "\u0394"

def calc():
    int1 = input("Inserisci primo termine della tua equazione quadratica: ").strip()
    int2 = input("Inserisci secondo termine della tua equazione quadratica: ").strip()
    int3 = input("Inserisci terzo termine della tua equazione quadratica: ").strip()

    if int1 == '' or int2 == '' or int3 == '':
        print("no input ")
        return

    try:
       
        a = sympify(int1)
        b = sympify(int2)
        c = sympify(int3)
    except:
        print("Input!!!!!!!!!!!!!!!! non valido :c")
        return

    x = symbols("x")
    delt = b**2 - 4*a*c

    if delt.is_number:
        if delt > 0:
            print(delta, ">", 0)
        elif delt == 0:
            print(delta, "==", 0)
        else:
            print(delta, "<", 0)
    else:
        print(delta, "non può essere valutato ")

  
    formularis1 = (-b + sqrt(delt)) / (2*a)
    formularis2 = (-b - sqrt(delt)) / (2*a)
    print("Le radici sono:", formularis1, formularis2)
    time.sleep(0.5)

calc()
