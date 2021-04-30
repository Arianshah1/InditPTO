#aufgabe1
#schreiben sie ein Pythonprogramm, das
#den benutzer grüßt
#eine erste zahl entgegen nimmt
#eine zweite zahl entgegen nimmt
#summe
#differenz
#produkt
#quotient inkl. Nachkommastellen

"""str_user_name=input("Username eingeben:")
print("Hello",str_user_name)


str_zahl1=input("Eingabe erste Zahl:")
str_zahl1=float(str_zahl1)

str_zahl2=input("Eingabe zweite Zahl:")
str_zahl2=float(str_zahl2)

Summe=str_zahl1+str_zahl2
Differenz=str_zahl1-str_zahl2
Produkt=str_zahl1*str_zahl2
Quotient=str_zahl1/str_zahl2
print("Die Summe der Zahlen lautet:",Summe)
print("Die Differenz der Zahlen lautet:",Differenz)
print("Das Produkt der Zahlen lautet:",Produkt)
print("Der Quotient der Zahlen lautet:",Quotient)"""

#neue aufgabe 26.03.21
#schreiben sie ein Pythonprogramm, das
#den benutzer grüßt
#eine erste zahl entgegen nimmt
#eine zweite zahl entgegen nimmt
#Die Summe bildet
#Das Produkt bildet
#quotient kleinere zahl durch größere zahl berechnen
#die differenz der kleineren von der größeren zahl berechnen




str_user_name=input("Username eingeben:")
print("Hello",str_user_name)


str_zahl1=input("Eingabe erste Zahl:")
str_zahl1=float(str_zahl1)

str_zahl2=input("Eingabe zweite Zahl:")
str_zahl2=float(str_zahl2)

Summe=str_zahl1+str_zahl2
print("Die Summe der Zahlen lautet:",Summe)

Produkt=str_zahl1*str_zahl2
print("Das Produkt der Zahlen lautet:",Produkt)

if str_zahl2<str_zahl1:
    Quotient=str_zahl2/str_zahl1
elif str_zahl1<str_zahl2:
    Quotient=(str_zahl1/str_zahl2)

elif str_zahhl1 == str_zahl2:
    Quotient=str_zahl1/str_zahl2
    
print("Der Quotient lautet:", Quotient)

if str_zahl1>str_zahl2:
    Differenz=str_zahl1-str_zahl2
    print("Die Differenz ist", Differenz)

elif str_zahl1<str_zahl2:
    Differenz=str_zahl2-str_zahl1
    print("Die Differenz ist", Differenz)
   
else: Differenz = str_zahl1-str_zahl2
print ("Die Differenz ist", Differenz)







