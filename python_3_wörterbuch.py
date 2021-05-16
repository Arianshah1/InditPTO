#woertherbuch
#einen Begriff eingeben dann die dazugehörige übersetzung ausgeben + die dazugehörige sprache
#wenn der Begriff nicht existiert, dies anzeigen 


# 2 Wortlisten kreieren

woerterbuch_de=["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]

woerterbuch_en=["apple", "pear", "cherry", "melon", "apricot", "peach"]

l=len(woerterbuch_de) #x anzahl elemente in woerterbuch_de
index=0

#wort eingabe als search bezeichnet
search=(input("Welches Wort soll übersetzt werden?/ Which word should be translated?"))


#wenn 'search' einem wort aus woerterbuch_de entspricht, dann wird das dazugehörige wort aus dem woerterbuch_en ausgeben.

while index<l:
    if woerterbuch_de[index].lower()==search.lower():
        print(woerterbuch_en[index],"(EN)")
        break


#wenn 'search' einem wort aus  woerterbuch_en entspricht, dann wird das dazugehörige wort aus dem woerterbuch_de ausgeben.
        
    
    elif woerterbuch_en[index].lower()==search.lower():
        print(woerterbuch_de[index],"(DE)")
        break
    index=index+1
  
#wenn 'search' keinem wort aus beiden listen entspricht, wird ausgegeben dass keine Übersetzung existiert.
    if index==l: 
        print("Es konnte kein Wort gefunden werden./No word could be found.")
        break
    
        
    
     
    
    


    
