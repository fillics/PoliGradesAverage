# poligrades-downloader
Questo è uno script scritto in Python 3 che esegue il parsing del testo presente sui Servizi Online del Politecnico di Milano e salva in un database SQLite gli esiti degli esami di tutti gli studenti.

I dati salvati nel database sono:
* Codice, descrizione e CFU dell'insegnamento
* Numero di matricola e codice persona dello studente
* Esito dell'esame

Nella tabella `studenti` del database è anche presente un campo `nome` che però dovrà essere compilato manualmente con dati ottenuti da altre fonti. Per motivi di privacy, il Politecnico di Milano non pubblica i nomi degli studenti insieme agli esiti degli esami.

## Requisiti
* Python 3
* Modulo `sqlite3`

## Utilizzo dello script
Lo script accetta come input attraverso `stdin` il testo contenente gli esiti dell'esame e inserisce i dati nel database `grades.db`. Il testo a cui si fa riferimento può essere ottenuto dalla sezione *Consultazione esito esami* dei [Servizi Online](https://www.polimi.it/servizionline/) del Politecnico. Il testo nel riquadro rosso nello scheenshot qui sotto è ciò che deve essere passato via `stdin` allo script `poligrades-downloader.py`.

![Esempio testo da selezionare](screenshot.png)

## Scopo di questo script (disclaimer)
I dati ottenuti tramite questo script possono essere usati per fini statistici. Questo script non è stato pensato per violare la privacy degli studenti e lo sviluppatore non incoraggia nessuno a farlo. Una volta ottenuti i dati, l'utente è completamente responsabile dell'utilizzo che ne fa.
