#codice per verificare corretto funzionamento, da eseguire su terminale esterno
import unittest  # Libreria per creare ed eseguire test automatizzati
import os # Libreria per lavorare con file e percorsi
from genera_dati import NUM_UTENTI, dati_utenti, file_excel

class TestGenerazioneDati(unittest.TestCase):
    def test_numero_utenti(self):
        # Verifica che siano stati generati il numero corretto di utenti
        self.assertEqual(len(dati_utenti), NUM_UTENTI) #self.assertEqual: Metodo per verificare che due valori siano uguali.

    def test_campi_utenti(self):
        # Verifica che ogni utente abbia i campi richiesti
        for utente in dati_utenti:
            self.assertIn("Nome", utente)
            self.assertIn("Cognome", utente)
            self.assertIn("Email", utente)
            self.assertIn("Telefono", utente)
            self.assertIn("Citta", utente)

    def test_file_excel_creato(self):
        # Verifica che il file Excel sia stato creato
        self.assertTrue(os.path.exists(file_excel))

# Questo blocco avvia l'esecuzione dei test se il file viene eseguito direttamente.
if __name__ == "__main__":
    unittest.main()  # unittest.main(): Raccoglie automaticamente tutti i metodi che iniziano con test_ e li esegue.

