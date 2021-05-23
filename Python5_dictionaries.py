#wörterbuch mit Dictionaries statt Listen
#verwendung von 'try' und 'except'

woerterbuch_de={"Apfel":"apple", "Birne":"pear", "Kirsche":"cherry","Melone":"melon","Marille":"apricot", "Pfirsich":"peach"}


woerterbuch_en={"apple":"Apfel", "pear":"Birne", "cherry":"Kirsche", "melon":"Melone", "apricot":"Marille", "peach":"Pfirsich"}
#dictionaries



try:
    insert=input("Wort/Word:") #eingabe des gesuchten wortes
    print(woerterbuch_de[insert],"(EN)")#falls es einen wert gibt,der zum wert der eingabe passt, wird dieser ausgegeben
    
except:
    try:
        print(woerterbuch_en[insert],"(DE)")#ausnahme, falls es einen wert gibt,der zum wert der eingabe passt, wird dieser ausgusgegeben

    except:
        print("Dieses Wort ist nicht verfügbar/Word not found")# falls kein wert passt, wird dies ausgegeben.
