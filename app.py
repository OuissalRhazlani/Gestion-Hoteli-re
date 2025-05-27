import streamlit as st
import sqlite3
from datetime import datetime
import os
# Connexion à la base
def get_conn():
    return sqlite3.connect("hotel.db")

# Création des tables (au cas où)
def init_db():
    conn = get_conn()
    c = conn.cursor()
    print("Current Working Directory:", os.getcwd())
    conn.commit()
    conn.close()

# Lister les clients
def get_clients():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM clients")
    data = c.fetchall()
    conn.close()
    return data

# Lister les réservations
def get_reservations():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM reservations")
    data = c.fetchall()
    conn.close()
    return data

# Chambres disponibles
def get_chambres_dispo(debut, fin):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM chambres WHERE id NOT IN (
            SELECT id_chambre FROM reservations
            WHERE date_debut < ? AND date_fin > ?
        )
    """, (fin, debut))
    data = c.fetchall()
    conn.close()
    return data

# Ajouter client
def ajouter_client(nom, prenom, email):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO clients (nom, prenom, email) VALUES (?, ?, ?)", (nom, prenom, email))
    conn.commit()
    conn.close()

# Ajouter réservation
def ajouter_reservation(id_client, id_chambre, debut, fin):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO reservations (id_client, id_chambre, date_debut, date_fin) VALUES (?, ?, ?, ?)",
              (id_client, id_chambre, debut, fin))
    conn.commit()
    conn.close()

# Interface principale
st.title("Application de Gestion Hôtelière")
init_db()

menu = st.sidebar.radio("Menu", ["Liste des clients", "Liste des réservations", "Chambres disponibles", "Ajouter client", "Ajouter réservation"])

if menu == "Liste des clients":
    st.subheader("Clients")
    for client in get_clients():
        st.write(client)

elif menu == "Liste des réservations":
    st.subheader("Réservations")
    for res in get_reservations():
        st.write(res)

elif menu == "Chambres disponibles":
    st.subheader("Chambres disponibles")
    date_debut = st.date_input("Date début")
    date_fin = st.date_input("Date fin")
    if st.button("Chercher"):
        dispo = get_chambres_dispo(str(date_debut), str(date_fin))
        for chambre in dispo:
            st.write(chambre)

elif menu == "Ajouter client":
    st.subheader("Nouveau client")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    email = st.text_input("Email")
    if st.button("Ajouter client"):
        ajouter_client(nom, prenom, email)
        st.success("Client ajouté")

elif menu == "Ajouter réservation":
    st.subheader("Nouvelle réservation")
    clients = get_clients()
    chambres = get_chambres_dispo("1900-01-01", "2100-01-01")
    id_client = st.selectbox("Client", [f"{c[0]} - {c[1]} {c[2]}" for c in clients])
    id_chambre = st.selectbox("Chambre", [f"{c[0]} - {c[1]}" for c in chambres])
    date_debut = st.date_input("Date début")
    date_fin = st.date_input("Date fin")
    if st.button("Réserver"):
        ajouter_reservation(int(id_client.split(" - ")[0]), int(id_chambre.split(" - ")[0]), str(date_debut), str(date_fin))
        st.success("Réservation enregistrée")
