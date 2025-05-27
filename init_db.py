import sqlite3

def init_db():
    conn = sqlite3.connect('hotel.db')  # crée le fichier hotel.db s'il n'existe pas
    c = conn.cursor()
    # Création table clients
    c.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    # Création table chambres
    c.execute('''
        CREATE TABLE IF NOT EXISTS chambres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL,
            type TEXT NOT NULL
        )
    ''')
    # Création table reservations
    c.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_client INTEGER NOT NULL,
            id_chambre INTEGER NOT NULL,
            date_debut TEXT NOT NULL,
            date_fin TEXT NOT NULL,
            FOREIGN KEY (id_client) REFERENCES clients(id),
            FOREIGN KEY (id_chambre) REFERENCES chambres(id)
        )
    ''')
    conn.commit()
    conn.close()
    print("Base et tables créées avec succès.")

if __name__ == "__main__":
    init_db()
