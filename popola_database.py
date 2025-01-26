import sqlite3  # Libreria per lavorare con SQLite
import pandas as pd  # Libreria per leggere il file Excel

# 1. Connessione al database SQLite (crea il file se non esiste)
conn = sqlite3.connect("utenti.db")  # Crea o apre il database 'utenti.db'

# 2. Creazione della tabella "utenti"
cursor = conn.cursor()  # Crea un cursore per eseguire i comandi SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Chiave primaria, incrementata automaticamente
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL,
    citta TEXT NOT NULL
)
""")
print("Tabella 'utenti' creata (se non esiste già).")

# 3. Lettura del file Excel
file_excel = "utenti_generati.xlsx"
df = pd.read_excel(file_excel)  # Legge il file Excel in un DataFrame
print("Dati letti dal file Excel.")

# 4. Inserimento dei dati nella tabella
# Usa il metodo to_sql per inserire tutti i dati dal DataFrame
df.to_sql("utenti", conn, if_exists="append", index=False)
print(f"Tabella 'utenti' popolata con {len(df)} record.")

# 5. Verifica dei dati inseriti
cursor.execute("SELECT * FROM utenti")
rows = cursor.fetchall()  # Recupera tutti i record dalla tabella
print("Dati nella tabella:")
for row in rows:
    print(row)

# 6. Chiusura della connessione
conn.commit()  # Salva le modifiche
conn.close()  # Chiude la connessione
print("Connessione al database chiusa.")
