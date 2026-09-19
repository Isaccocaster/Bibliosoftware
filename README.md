# 📚 BiblioSoftware

Software CLI in Python per la gestione dei libri di una biblioteca, sviluppato seguendo una specifica funzionale dettagliata.

**🌐 Language:** [Italiano](#italiano) | [English](#english)

---

## Italiano

### Descrizione

BiblioSoftware è un programma da terminale per gestire il catalogo di una biblioteca. Permette di aggiungere e rimuovere libri, verificarne la disponibilità, registrare prestiti, reintegrare copie e consultare statistiche sul catalogo. I libri sono salvati in un dizionario `{titolo: copie}`. L'utente interagisce tramite un menu testuale in un ciclo continuo, finché non digita il comando `esci`.

### Specifica del progetto

Il progetto è stato sviluppato a partire da una specifica funzionale, assegnata come esercizio nell'ambito del corso Python di [Gloria Longo](https://www.pythonaccelerator.it/). Il testo completo è disponibile nel file [Specifiche Progetto 1.pdf](Specifiche%20Progetto%201.pdf). Le funzioni richieste:

| Funzione | Opzione menu | Descrizione |
|---|---|---|
| `aggiungi_libro` | 1 | Aggiunge un nuovo libro, oppure incrementa le copie se il libro esiste già |
| `rimuovi_libro` | 2 | Rimuove un libro dal catalogo; se non esiste stampa un errore |
| `verifica_disponibilita` | 3 | Restituisce `True` se c'è almeno una copia, `False` se il libro non esiste o è esaurito |
| `prendi_in_prestito` | 4 | Decrementa di 1 le copie; se il libro non esiste o è esaurito stampa un errore |
| `statistiche_biblioteca` | 5 | Restituisce un dizionario con numero di titoli, copie totali e media copie per titolo |
| `visualizza_libri` | 6 | Mostra tutti i libri con le copie disponibili, o un messaggio se il catalogo è vuoto |
| `restaurare_libro` | 7 | Aggiunge copie a un libro esistente; se non esiste stampa un errore |

### Flusso del programma

```mermaid
flowchart TD
    A[Avvio programma] --> B["Menu principale<br/>ciclo while True"]
    B --> C{"Comando inserito"}
    C -- "1 - 7" --> D["Esegue la funzione<br/>corrispondente"]
    C -- esci --> E[Fine programma]
    C -- non valido --> F["Messaggio di errore"]
    D --> B
    F --> B
```

### Esempio di utilizzo

Sessione di prova con due libri:

| Comando | Input | Output |
|---|---|---|
| 6 | — | `Non ci sono libri in bibloteca` |
| 1 | `Il Nome della Rosa`, `3` | `Libro aggiunto` |
| 1 | `1984`, `2` | `Libro aggiunto` |
| 1 | `1984`, `abc` | `Inserisci un numero di copie valido` |
| 3 | `  IL NOME DELLA ROSA ` | `True` |
| 4 | `1984` (due volte) | `Il libro 1984 è stato correttamente decrementato` |
| 4 | `1984` (copie finite) | `ERRORE NELLA RICHIESTA` |
| 3 | `1984` | `False` |
| 7 | `1984`, `5` | `Quantita aggiornata` |
| 5 | — | `{'totale_libri': 2, 'copie_totali': 8, 'media_totale': 4.0}` |
| 2 | `Dune` | `ERRORE TITOLO NON VALIDO` |
| esci | — | `Grazie e arrivederci` |

### Scelte implementative

Rispetto alla specifica, il codice presenta alcune differenze:

- **Parametri delle funzioni**: la specifica indica firme come `aggiungi_libro(titolo, copie)`. Nell'implementazione ogni funzione riceve il dizionario `biblioteca` e chiede titolo e copie all'utente con `input()` al suo interno.
- **Chiave della media**: la specifica chiede che `statistiche_biblioteca()` restituisca la chiave `media_copie`, mentre il codice usa `media_totale`.

### Punti tecnici salienti

- Codice organizzato in funzioni, una per ogni operazione richiesta dalla specifica
- Titoli non sensibili a maiuscole e spazi (`.strip().lower()`): `1984`, ` 1984 ` e `IL NOME DELLA ROSA` vengono riconosciuti
- Validazione delle quantità: le copie devono essere un numero intero maggiore di zero (`try/except ValueError`)
- Gestione dei casi limite: libro inesistente, copie esaurite, catalogo vuoto (la media non genera una divisione per zero)
- Menu interattivo con ciclo continuo (`while True`) e uscita con `esci` tramite `break`

### Come eseguirlo

```bash
python BiblioSoftware.py
```

Su alcuni sistemi il comando è `python3 BiblioSoftware.py`. Nessuna dipendenza esterna richiesta: basta la libreria standard di Python.

### Struttura della repository

| File | Contenuto |
|---|---|
| `BiblioSoftware.py` | Codice sorgente del programma |
| `Specifiche Progetto 1.pdf` | Specifica funzionale di partenza |
| `LICENSE` | Licenza MIT |

### Possibili sviluppi futuri

- Salvataggio permanente del catalogo su file o database **SQLite**
- Allineamento completo alla specifica (firme delle funzioni e chiave `media_copie`)
- Separazione tra logica applicativa e interfaccia utente
- Gestione degli utenti e dello storico dei prestiti
- Suite di test automatici

### Autore

**Antonino Todaro** — [GitHub](https://github.com/Isaccocaster)

---

## English

### Description

BiblioSoftware is a command-line program for managing a library's catalog. It lets you add and remove books, check availability, record loans, restore copies and view catalog statistics. Books are stored in a `{title: copies}` dictionary. The user interacts through a text menu in a continuous loop, until they type the `esci` command.

### Project specification

This project was built from a functional specification, assigned as an exercise within [Gloria Longo](https://www.pythonaccelerator.it/)'s Python course. The full text (in Italian) is available in [Specifiche Progetto 1.pdf](Specifiche%20Progetto%201.pdf). Required functions:

| Function | Menu option | Description |
|---|---|---|
| `aggiungi_libro` | 1 | Adds a new book, or increases the copies if the book already exists |
| `rimuovi_libro` | 2 | Removes a book from the catalog; prints an error if it does not exist |
| `verifica_disponibilita` | 3 | Returns `True` if at least one copy is available, `False` if the book does not exist or is out of stock |
| `prendi_in_prestito` | 4 | Decreases copies by 1; prints an error if the book does not exist or is out of stock |
| `statistiche_biblioteca` | 5 | Returns a dictionary with number of titles, total copies and average copies per title |
| `visualizza_libri` | 6 | Lists every book with its available copies, or a message if the catalog is empty |
| `restaurare_libro` | 7 | Adds copies to an existing book; prints an error if it does not exist |

### Program flow

```mermaid
flowchart TD
    A[Program start] --> B["Main menu<br/>while True loop"]
    B --> C{"Command entered"}
    C -- "1 - 7" --> D["Runs the matching<br/>function"]
    C -- esci --> E[Program end]
    C -- invalid --> F["Error message"]
    D --> B
    F --> B
```

### Sample session

Test session with two books:

| Command | Input | Output |
|---|---|---|
| 6 | — | `Non ci sono libri in bibloteca` |
| 1 | `Il Nome della Rosa`, `3` | `Libro aggiunto` |
| 1 | `1984`, `2` | `Libro aggiunto` |
| 1 | `1984`, `abc` | `Inserisci un numero di copie valido` |
| 3 | `  IL NOME DELLA ROSA ` | `True` |
| 4 | `1984` (twice) | `Il libro 1984 è stato correttamente decrementato` |
| 4 | `1984` (no copies left) | `ERRORE NELLA RICHIESTA` |
| 3 | `1984` | `False` |
| 7 | `1984`, `5` | `Quantita aggiornata` |
| 5 | — | `{'totale_libri': 2, 'copie_totali': 8, 'media_totale': 4.0}` |
| 2 | `Dune` | `ERRORE TITOLO NON VALIDO` |
| esci | — | `Grazie e arrivederci` |

### Implementation choices

The code differs from the specification in a few ways:

- **Function parameters**: the specification lists signatures such as `aggiungi_libro(titolo, copie)`. In the implementation each function receives the `biblioteca` dictionary and asks the user for title and copies with `input()` inside the function.
- **Average key**: the specification asks `statistiche_biblioteca()` to return the key `media_copie`, while the code uses `media_totale`.

### Key technical points

- Code organized into functions, one for each operation required by the specification
- Case- and whitespace-insensitive titles (`.strip().lower()`): `1984`, ` 1984 ` and `IL NOME DELLA ROSA` are all recognized
- Quantity validation: copies must be an integer greater than zero (`try/except ValueError`)
- Edge case handling: nonexistent book, no copies left, empty catalog (the average never divides by zero)
- Interactive menu with a continuous loop (`while True`) and exit via `esci` and `break`

### How to run it

```bash
python BiblioSoftware.py
```

On some systems the command is `python3 BiblioSoftware.py`. No external dependencies required: Python standard library only.

### Repository structure

| File | Content |
|---|---|
| `BiblioSoftware.py` | Program source code |
| `Specifiche Progetto 1.pdf` | Original functional specification |
| `LICENSE` | MIT license |

### Possible future improvements

- Persistent catalog storage on file or **SQLite** database
- Full alignment with the specification (function signatures and the `media_copie` key)
- Separation between application logic and user interface
- User management and loan history
- Automated test suite

### Author

**Antonino Todaro** — [GitHub](https://github.com/Isaccocaster)
