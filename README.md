# Bibliosoftware

Bibliosoftware è un'applicazione da terminale sviluppata in Python per gestire l'inventario essenziale di una biblioteca.

Il progetto è stato realizzato a partire da specifiche definite in anticipo, con l'obiettivo di trasformare requisiti funzionali in un programma modulare, verificabile e semplice da utilizzare.

## Funzionalità

- aggiunta di nuovi libri e aggiornamento delle copie disponibili;
- rimozione di un libro dall'inventario;
- verifica della disponibilità;
- registrazione del prestito con decremento delle copie;
- reintegro delle copie restituite;
- visualizzazione completa dell'inventario;
- calcolo di numero di titoli, copie complessive e media delle copie;
- validazione degli input numerici e gestione degli errori con `try/except`;
- menu interattivo utilizzabile da terminale.

## Tecnologie e concetti utilizzati

- Python 3;
- funzioni e valori di ritorno;
- dizionari;
- cicli e condizioni;
- normalizzazione degli input con `strip()` e `lower()`;
- gestione delle eccezioni;
- organizzazione modulare della logica applicativa.

## Avvio

Non sono richieste librerie esterne.

1. Scaricare o clonare la repository.
2. Aprire un terminale nella cartella del progetto.
3. Eseguire:

```bash
python BiblioSoftware.py
```

Su alcuni sistemi il comando può essere:

```bash
python3 BiblioSoftware.py
```

## Struttura della repository

- `BiblioSoftware.py` - codice sorgente dell'applicazione;
- `SPECIFICHE.pdf` - requisiti funzionali di partenza;
- `LICENSE` - licenza del progetto.

## Possibili sviluppi futuri

- salvataggio permanente dell'inventario su file o database;
- separazione tra logica applicativa e interfaccia utente;
- gestione degli utenti e dello storico dei prestiti;
- test automatici;
- interfaccia grafica.

## Autore

Antonino Todaro  
[Profilo GitHub](https://github.com/Isaccocaster)
