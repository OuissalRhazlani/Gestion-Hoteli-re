CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS chambres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL,
    type TEXT,
    prix REAL
);

CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER,
    id_chambre INTEGER,
    date_debut TEXT,
    date_fin TEXT,
    FOREIGN KEY (id_client) REFERENCES clients(id),
    FOREIGN KEY (id_chambre) REFERENCES chambres(id)
);
