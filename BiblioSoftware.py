#Dizionario con libri in biblioteca
biblioteca = {}
#FUNZIONE AGGIUNTA LIBRO
def aggiungi_libro(biblioteca):
    add_book = input("Che libro vuoi aggiungere? ").strip().lower()
    if add_book in biblioteca: 
      try:
        add_book1 = int(input("Quante copie "))
        if add_book1 > 0:
          biblioteca[add_book] += add_book1
          print("Quantita aggiornata")
        else:
          print("Numero di copie non valido")  
      except ValueError:
        print("Inserisci un numero di copie valido")
    if add_book not in biblioteca:
      try:
        add_book2 = int(input("Quante copie volete aggiungere di questo nuovo libro? "))
        if add_book2 > 0:
          biblioteca[add_book] = add_book2
          print("Libro aggiunto")
        else:
          print("Numero copie non valido")
      except ValueError:
        print("Quantita non valida")      
#FUNZIONE RIMUOVI LIBRO
def rimuovi_libro(biblioteca):
    rem_book = input("Che libro vuoi rimuovere? ").strip().lower()
    if rem_book in biblioteca:
        del biblioteca[rem_book]
        print("Libro rimosso correttamente")
    else:
        print("ERRORE TITOLO NON VALIDO")
#FUNZIONE VERIFICA DISPONIBILITA
def verifica_disponibilita(biblioteca):
    check_book = input("DI quale libro vuoi controllare la disponibilità? ").strip().lower()
    if check_book in biblioteca and biblioteca[check_book] >= 1:
        return True
    else:
        return False
#FUNZIONE PREESTITO
def prendi_in_prestito(biblioteca):
    rent_book = input("Quale libro vuoi prendere in prestito? ").strip().lower()
    if rent_book in biblioteca and biblioteca[rent_book] >= 1:
        biblioteca[rent_book] -= 1
        print(f"Il libro {rent_book} è stato correttamente decrementato ")
    else:
        print("ERRORE NELLA RICHIESTA")
#FUNZIONE MEDIA LIBRI
def statistiche_biblioteca(biblioteca):
    tot_book = 0
    cop_book = 0
    for libro in biblioteca:
        tot_book += 1
        cop_book += biblioteca[libro]
    if tot_book == 0:
        print("Nessun libro per fare la media")
        media = 0
    else:     
        media = cop_book / tot_book
    return {"totale_libri" : tot_book,
            "copie_totali" : cop_book,
            "media_totale" : media
    }
#FUNZIONE NUMERO LIBRI E COPIE
def visualizza_libri(biblioteca):
    if biblioteca:
        for libro in biblioteca:
            print(f"Il libro {libro} ha {biblioteca[libro]} copie ")
    else:
        print("Non ci sono libri in bibloteca ")
#FUNZIONE AGGIUNGI COPIA A LIBRO ESISTENTE
def restaurare_libro(biblioteca):
    adds = input("Di quale libro vuoi aggiungere piu copie? ").strip().lower()
    if adds in biblioteca:
      try:
        addsplus = int(input("Quante copie? "))
        if addsplus > 0:
          biblioteca[adds] += addsplus
          print("Quantita aggiornata")
        else:
          print("Numero copie non valido")  
      except ValueError:
        print("Numero copie non valido")                
    else:
        print("Errore libro inesistente ")           
while True:
        scelta = input("Salve, quale comando vuole usare:\n" \
        "1) Aggiungere un libro \n" \
        "2) Rimuovere un libro \n" \
        "3) Verifica disponibilità \n" \
        "4) Prendere in prestito \n" \
        "5) Statistiche biblioteca \n" \
        "6) Visualizza tutti i libri \n" \
        "7) Restaura libro\n"
        "PER USCIRE DAL PROGRAMMA DIGITARE esci \n")
        #AGGIUNGI LIBRO
        if scelta == "1":
              aggiungi_libro(biblioteca)    
        #RIMUOVI LIBRO          
        elif scelta == "2":
              rimuovi_libro(biblioteca)
        #CONTROLLA DISPONIBILITA            
        elif scelta == "3":
             TF = verifica_disponibilita(biblioteca)
             print(TF)
        #PRESTITO LIBRO            
        elif scelta == "4":
              prendi_in_prestito(biblioteca)
        #MEDIA LIBRI            
        elif scelta == "5":
              media = statistiche_biblioteca(biblioteca)
              print(media)
        #NUMERO LIBRO E COPIE      
        elif scelta == "6":
            visualizza_libri(biblioteca)
        #AGGIUGI COPIE A LIBRO ESISTENTE          
        elif scelta == "7":
             restaurare_libro(biblioteca)
        #CHIUDI PROGRAMMA                  
        elif scelta == "esci":
              print("Grazie e arrivederci")
              break
        #SCELTA NON VALIDA
        else:
              print("SCELTA NON VALIDA SI PREGA DI INSERIRE UN COMANDO VALIDO")              