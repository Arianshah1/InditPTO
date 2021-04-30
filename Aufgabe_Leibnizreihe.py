# Pi durch leibnitz-Reihe annäherungsweise berechnen.

N=input("Eingabe Anzahl der Brüche n:")
n=float(N)
Wert=input("Eingabe gesuchter Wert:")
Wert=float(Wert)
k=(0)
Ergebnis=(0)

while k<n:
    Ergebnis=Ergebnis+(4*((-1)**k)/(2*k+1))
    k=k+1
    if Wert==k:
        print("Das Zwischenergebnis:",k,"=", Ergebnis)
    print ("Die Anzahl der Brüche:", k,"=", Ergebnis)
        