#es008 pag.40 es.3

def main():
    operatore = int(input("Inserisci il numero corrispndente all'operatore del calcolo che si vuole effettuare: "))
    n1 = int(input("Inserisci il primo numero: "))
    n2 = int(input("Inserisci il secondo numero: "))
    if operatore == 0: #somma
        risultato = n1 + n2

    elif operatore  == 1: #sottrazione
        risultato = n1 - n2

    elif operatore == 2: #moltiplicazione
        risultato = n1 * n2

    elif operatore == 3: #divisione
        risultato = n1 // n2 #con una sola / stampa la divisione in float

    print(f"L'operazione corrispondente al numero {operatore} risulta {risultato}")    

if __name__=="__main__": 
    main()