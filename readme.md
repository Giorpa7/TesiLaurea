## **Project Work: Sistema per la Conformità al GDPR**

### **Descrizione**
Questo progetto è stato sviluppato come Project Work del corso di laurea in Informatica per le Aziende Digitali presso l'Università Telematica Pegaso. L'obiettivo principale è implementare un sistema informatico conforme ai principi del GDPR, con funzionalità di gestione e trattamento dei dati personali.

---

### **Funzionalità**
- Generazione di dati casuali e salvataggio in formato Excel.
- Popolazione di un database SQLite con i dati generati.
- Interazione con il database tramite API REST (FastAPI):
  - Recupero di tutti gli utenti.
  - Filtraggio degli utenti per città.
  - Aggiunta di nuovi utenti.
- Testing automatico della generazione di dati.
- Struttura modulare per un'estensibilità futura.

---

### **Struttura del Progetto**
- **genera_dati.py**: Genera un file Excel con dati utente casuali.
- **popola_database.py**: Popola il database SQLite con i dati generati.
- **popola_database_verifica.py**: Verifica i dati inseriti nel database.
- **server.py**: Fornisce API REST per interagire con il database.
- **genera_dati_test.py**: Contiene test automatici per verificare il corretto funzionamento del file `genera_dati.py`.

---

### **Requisiti**
Assicurati di avere i seguenti requisiti:
- **Python 3.10 o superiore**
- Librerie Python necessarie:
  - `faker`
  - `pandas`
  - `fastapi`
  - `uvicorn`

---

### **Esecuzione**
1. **Generazione dati: crea un file Excel contenente dati utente casuali**
   ```bash
   python genera_dati.py
   ```
2. **Popolazione database: inserisce i dati generati nel database SQLite**
   ```bash
   python popola_database.py
   ```
3. **Esecuzione dei test: verifica automatizzata della generazione dei dati**
   ```bash
   python -m unittest genera_dati_test.py
   ```
4. **Verifica dei dati: Consente di ispezionare manualmente i dati salvati nel database**
   ```bash
   python popola_database_verifica.py
   ```
5. **Avvio del server FastAPI: Esegue il server per interagire con il sistema tramite API REST**
   ```bash
   uvicorn server:app --reload
   ```
   
---

### **API Documentazione**
FastAPI fornisce una documentazione interattiva per testare gli endpoint:
- [Swagger UI](http://127.0.0.1:8000/docs)


### **Autore**
- **[Giorgio Pati]**
- Email: [giorgiopati1999@gmail.com]
- Università Telematica Pegaso
