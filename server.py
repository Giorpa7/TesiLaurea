# Importa FastAPI, il framework per creare API REST
from fastapi import FastAPI

# Importa il middleware CORS per gestire le richieste da origini diverse
from fastapi.middleware.cors import CORSMiddleware

# Importa sqlite3 per la connessione al database SQLite
import sqlite3

# Inizializza l'applicazione FastAPI
app = FastAPI()

# Configura il middleware CORS per gestire le richieste da origini diverse
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permette richieste da tutti i domini (modificabile per maggiore sicurezza)
    allow_methods=["*"],  # Permette tutti i metodi HTTP (GET, POST, PUT, DELETE, ecc.)
    allow_headers=["*"],  # Permette tutti gli header inviati dal client
)

# Specifica il nome del file del database SQLite
DB_FILE = "utenti.db"

# Funzione per creare il database e la tabella "utenti" se non esistono
def crea_database():
    conn = sqlite3.connect(DB_FILE)  # Connessione al database
    cursor = conn.cursor()
    # Crea la tabella "utenti" solo se non esiste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utenti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cognome TEXT,
            email TEXT,
            telefono TEXT,
            citta TEXT
        )
    """)
    conn.commit()  # Salva le modifiche nel database
    conn.close()  # Chiude la connessione

# Esegue la funzione per creare il database al momento dell'avvio del server
crea_database()

# Endpoint: Recupera tutti gli utenti dal database
@app.get("/utenti")
def get_utenti():
    # Connessione al database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Esegue una query per selezionare tutti i record dalla tabella "utenti"
    cursor.execute("SELECT * FROM utenti")
    rows = cursor.fetchall()  # Recupera tutti i risultati della query
    conn.close()  # Chiude la connessione al database

    # Converte i risultati della query in una lista di dizionari
    utenti = [
        {"id": row[0], "nome": row[1], "cognome": row[2], "email": row[3], "telefono": row[4], "citta": row[5]}
        for row in rows
    ]
    return utenti  # Ritorna la lista degli utenti come risposta JSON

# Endpoint: Aggiunge un nuovo utente al database
@app.post("/utenti")
def add_utente(utente: dict):
    # Connessione al database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Esegue una query per inserire un nuovo utente nella tabella
    cursor.execute("""
        INSERT INTO utenti (nome, cognome, email, telefono, citta)
        VALUES (?, ?, ?, ?, ?)
    """, (utente["nome"], utente["cognome"], utente["email"], utente["telefono"], utente["citta"]))
    conn.commit()  # Salva le modifiche nel database
    conn.close()  # Chiude la connessione al database

    return {"message": "Utente aggiunto con successo"}  # Ritorna un messaggio di conferma

# Endpoint: Filtra gli utenti per città
@app.get("/utenti/citta/{citta}")
def get_utenti_per_citta(citta: str):
    # Connessione al database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Esegue una query per selezionare gli utenti filtrati per città
    cursor.execute("SELECT * FROM utenti WHERE citta = ?", (citta,))
    rows = cursor.fetchall()  # Recupera tutti i risultati della query
    conn.close()  # Chiude la connessione al database

    # Converte i risultati della query in una lista di dizionari
    utenti = [
        {"id": row[0], "nome": row[1], "cognome": row[2], "email": row[3], "telefono": row[4], "citta": row[5]}
        for row in rows
    ]
    return utenti  # Ritorna la lista degli utenti filtrati come risposta JSON
