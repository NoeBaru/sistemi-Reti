"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 006 pag.55 es.6
text: Scrivi un programma in Python che, assegnata una parola a una variabile stringa, stampi solo i caratteri con indice dispari
(per esempio della parola "ciao" visualizzerà solo "io").
"""

def main():
    stringa = "ciao"
    lung = len(stringa)
    for i in range(lung):
        if i % 2 == 1:
            print(stringa[i], end="")

if __name__=="__main__": 
    main()