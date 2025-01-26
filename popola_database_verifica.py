# Codice da eseguire per verificare il corretto funzionamento del file popola_database.py
# In alternativa possiamo verificare eseguendo direttamente il file utenti.db in MYSQL

import sqlite3

# Connessione al database
conn = sqlite3.connect("utenti.db")
cursor = conn.cursor()

# Esegui una query per visualizzare i dati
cursor.execute("SELECT * FROM utenti")
rows = cursor.fetchall()

# Stampa i dati
for row in rows:
    print(row)

# Chiudi la connessione
conn.close()
print("Connessione al database chiusa.")
