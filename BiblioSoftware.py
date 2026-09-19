#Dizionario con libri in biblioteca
biblioteca = {}
#FUNZIONE AGGIUNTA LIBRO
def aggiungi_libro(titolo, copie):
    if titolo in biblioteca:
        biblioteca[titolo] += copie
        print("Quantita aggiornata")
    else:
        biblioteca[titolo] = copie
        print("Libro aggiunto")
#FUNZIONE RIMUOVI LIBRO
def rimuovi_libro(titolo):
    if titolo in biblioteca:
        del biblioteca[titolo]
        print("Libro rimosso correttamente")
    else:
        print("ERRORE TITOLO NON VALIDO")
#FUNZIONE VERIFICA DISPONIBILITA
def verifica_disponibilita(titolo):
    if titolo in biblioteca and biblioteca[titolo] >= 1:
        return True
    else:
        return False
#FUNZIONE PREESTITO
def prendi_in_prestito(titolo):
    if verifica_disponibilita(titolo):
        biblioteca[titolo] -= 1
        print(f"Il libro {titolo} è stato correttamente decrementato ")
    else:
        print("ERRORE NELLA RICHIESTA")
#FUNZIONE MEDIA LIBRI
def statistiche_biblioteca():
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
            "media_copie" : media
    }
#FUNZIONE NUMERO LIBRI E COPIE
def visualizza_libri():
    if biblioteca:
        for libro in biblioteca:
            print(f"Il libro {libro} ha {biblioteca[libro]} copie ")
    else:
        print("Non ci sono libri in biblioteca ")
#FUNZIONE AGGIUNGI COPIA A LIBRO ESISTENTE
def restaurare_libro(titolo, copie):
    if titolo in biblioteca:
        biblioteca[titolo] += copie
        print("Quantita aggiornata")
    else:
        print("Errore libro inesistente ")
#FUNZIONI DI SUPPORTO PER L'INPUT DEL MENU
def chiedi_titolo(messaggio):
    return input(messaggio).strip().lower()
def chiedi_copie(messaggio):
    try:
        copie = int(input(messaggio))
        if copie > 0:
            return copie
        print("Numero di copie non valido")
    except ValueError:
        print("Inserisci un numero di copie valido")
    return None
while True:
        scelta = input("Salve, quale comando vuole usare:\n" \
        "1) Aggiungere un libro \n" \
        "2) Rimuovere un libro \n" \
        "3) Verifica disponibilità \n" \
        "4) Prendere in prestito \n" \
        "5) Statistiche biblioteca \n" \
        "6) Visualizza tutti i libri \n" \
        "7) Restaura libro\n"
        "PER USCIRE DAL PROGRAMMA DIGITARE esci \n").strip().lower()
        #AGGIUNGI LIBRO
        if scelta == "1":
              titolo = chiedi_titolo("Che libro vuoi aggiungere? ")
              copie = chiedi_copie("Quante copie? ")
              if copie is not None:
                  aggiungi_libro(titolo, copie)
        #RIMUOVI LIBRO
        elif scelta == "2":
              rimuovi_libro(chiedi_titolo("Che libro vuoi rimuovere? "))
        #CONTROLLA DISPONIBILITA
        elif scelta == "3":
             TF = verifica_disponibilita(chiedi_titolo("Di quale libro vuoi controllare la disponibilità? "))
             print(TF)
        #PRESTITO LIBRO
        elif scelta == "4":
              prendi_in_prestito(chiedi_titolo("Quale libro vuoi prendere in prestito? "))
        #MEDIA LIBRI
        elif scelta == "5":
              media = statistiche_biblioteca()
              print(media)
        #NUMERO LIBRO E COPIE
        elif scelta == "6":
            visualizza_libri()
        #AGGIUGI COPIE A LIBRO ESISTENTE
        elif scelta == "7":
             titolo = chiedi_titolo("Di quale libro vuoi aggiungere piu copie? ")
             if titolo in biblioteca:
                 copie = chiedi_copie("Quante copie? ")
                 if copie is not None:
                     restaurare_libro(titolo, copie)
             else:
                 print("Errore libro inesistente ")
        #CHIUDI PROGRAMMA
        elif scelta == "esci":
              print("Grazie e arrivederci")
              break
        #SCELTA NON VALIDA
        else:
              print("SCELTA NON VALIDA SI PREGA DI INSERIRE UN COMANDO VALIDO")
