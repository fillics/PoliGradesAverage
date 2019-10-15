#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sqlite3
import sys

REGEXP = r"([0-9]{8})\s+?([0-9]{6})\s+?(30 e Lode|[0-9]{2}|RIMANDATO|ASSENTE|RIPROVATO)\s+?([0-9]{6}) - (.+?)\s+\(\s*?CFU:\s*?([0-9]{1,2})\s*?\)"

db = sqlite3.connect("grades.db")
cur = db.cursor()

try:
    results = sys.stdin.read().strip().split("\n")
    for line in results:
        match = re.findall(REGEXP, line)[0]
        codice_persona = int(match[0])
        matricola = int(match[1])
        cod_insegnamento = int(match[3])
        dsc_insegnamento = match[4]
        cfu = int(match[5])
        try:
            valutazione = int(match[2])
            assente = 0
            rimandato = 0
            lode = 0
            riprovato = 0
        except ValueError:
            if (match[2] == "30 e Lode"):
                valutazione = 30
                lode = 1
                assente = 0
                rimandato = 0
                riprovato = 0
            elif (match[2] == "ASSENTE"):
                valutazione = None
                lode = 0
                assente = 1
                rimandato = 0
                riprovato = 0
            elif (match[2] == "RIMANDATO"):
                valutazione = None
                lode = 0
                assente = 0
                rimandato = 1
                riprovato = 0
            elif (match[2] == "RIPROVATO"):
                valutazione = None
                lode = 0
                assente = 0
                rimandato = 0
                riprovato = 1
        cur.execute("INSERT OR IGNORE INTO studenti (matricola) "
                    "VALUES (?)", (matricola,))
        cur.execute("UPDATE studenti SET codice_persona = ? WHERE matricola = ?",
                    (codice_persona, matricola))
        cur.execute("INSERT OR IGNORE INTO insegnamenti (id) "
                    "VALUES (?)", (cod_insegnamento,))
        cur.execute("UPDATE insegnamenti SET descrizione = ?, cfu = ? WHERE id = ?",
                    (dsc_insegnamento, cfu, cod_insegnamento))
        cur.execute("INSERT INTO esiti (studente, insegnamento, valutazione, "
                    "lode, rimandato, assente, riprovato) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (matricola, cod_insegnamento, valutazione, lode, rimandato,
                     assente, riprovato))
except:
    # Chiudiamo la connessione con il database in modo pulito prima
    # di restituire un qualunque errore
    db.close()
    raise

db.commit()
db.close()

