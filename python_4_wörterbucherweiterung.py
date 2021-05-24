#wörterbucherweiterung
#Hinzufügen,Löschen, Abfragen, Beenden
#

woerterbuch_de=["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]

woerterbuch_en=["apple", "pear", "cherry", "melon", "apricot", "peach"]

program=True

while program==True:
    selection=input("Welche operation soll ausgeführt werden? (H)inzufügen, (L)öschen, (A)bfragen, (B)eenden:")
    
    
    if selection== "H":
        neues_wort_de=input("Deutsches Wort:")
        woerterbuch_de.append(neues_wort_de)
        neues_wort_en=input("English word:")
        woerterbuch_en.append(neues_wort_en)
        print("Wort erfolgreich hinzugefügt/word is now available")

    elif selection =="L":
        print ("Welches Wort soll gelöscht werden?/Wich word should be deleted?",woerterbuch_de, woerterbuch_en)
        delete=(input("Welches Wort soll gelöscht werden?:"))
        le=(len(woerterbuch_de))
        index=0
        while index<le:
            if woerterbuch_de[index].lower() == delete.lower():      
                index_en=woerterbuch_en[index] 
                woerterbuch_de.remove(woerterbuch_de[index])
                woerterbuch_en.remove(index_en)
                print("Wort erfolgreich entfernt.")
                break
        
            elif woerterbuch_en[index].lower() == delete.lower():   
                index_de=woerterbuch_de[index] 
                woerterbuch_en.remove(woerterbuch_en[index])
                woerterbuch_de.remove(index_de)
                print("Wort erfolgreich entfernt.")
                break
            index=index+1
        if index==le:
            print("Wort nicht gefunden")
        
        
        
    elif selection=="A":
        search=(input("Welches Wort soll übersetzt werden?/ Which word should be translated?"))
        le=len(woerterbuch_de)
        index=0

        while index<le:
            if woerterbuch_de[index].lower()==search.lower():
                print(woerterbuch_en[index],"(EN)")
                break

            elif woerterbuch_en[index].lower()==search.lower():
                print(woerterbuch_de[index],"(DE)")
                break
            index=index+1
  

        if index==le: 
            print("Es konnte kein Wort gefunden werden./No word could be found.")
                
        
         
    elif selection=="B":
        print("Programm beendet")
        program==False
        break
        



