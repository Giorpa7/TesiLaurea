# Utilizzare Python per generare casualmente dati per 10 utent+creazione file excel

from faker import Faker #importo le due librerie necessarie per il progetto
import pandas as pd

# Inizializza la libreria Faker
fake = Faker("it_IT")  # Genera dati in italiano

# Numero di utenti da generare
NUM_UTENTI = 10

# Lista per memorizzare i dati generati
dati_utenti = []

# Genera i dati casuali
for _ in range(NUM_UTENTI):
    utente = {
        "Nome": fake.first_name(),
        "Cognome": fake.last_name(),
        "Email": fake.email(),
        "Telefono": fake.phone_number(),
        "Citta": fake.city()
    }
    dati_utenti.append(utente) # Aggiunge il dizionario alla lista dati_utenti

# Crea un DataFrame con i dati
utenti_df = pd.DataFrame(dati_utenti)

# Salva i dati in un file Excel
file_excel = "utenti_generati.xlsx"
utenti_df.to_excel(file_excel, index=False) #index=False: Evita di includere l’indice (numerazione delle righe) come colonna aggiuntiva nel file Excel.

print(f"Dati generati con successo! File salvato come '{file_excel}'")
