import streamlit as st
from PIL import Image
from PIL.ExifTags import TAGS
import folium
from streamlit_folium import st_folium

st.title("Projet Streamlit – Métadonnées & Cartes")

# Upload d'une image
fichier = st.file_uploader("Choisir une image (jpg, jpeg)", type=["jpg", "jpeg"])

if fichier:
    img = Image.open(fichier)
    st.image(img, caption="Image choisie", use_column_width=True)

    # Afficher les infos EXIF d'origine
    exif = img.getexif()
    if exif:
        st.subheader("Infos EXIF trouvées :")
        for id_tag in exif:
            tag = TAGS.get(id_tag, id_tag)
            donnees = exif.get(id_tag)
            if isinstance(donnees, bytes):
                donnees = donnees.decode(errors='ignore')
            st.text(f"{tag} : {donnees}")

    # Modification simulée
    st.subheader("Modification des infos (simulation) :")
    auteur = st.text_input("Auteur de la photo :", "Sofia")
    commentaire = st.text_input("Commentaire :", "Photo d’un monument algérien pour le projet")
    st.write("Nouvel auteur :", auteur)
    st.write("Nouveau commentaire :", commentaire)

    # Changer les coordonnées GPS
    st.subheader("Changer la position GPS :")
    latitude = st.number_input("Latitude", value=36.7525)   # Alger
    longitude = st.number_input("Longitude", value=3.0420)
    carte = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], tooltip="Monument Algérien").add_to(carte)
    st_folium(carte, width=700, height=500)

    # Ajouter mes voyages ou destinations de rêve
    st.subheader("Mes voyages / envies :")
    destinations = [
        {"nom": "Alger (Algérie)", "lat": 36.7525, "lon": 3.0420},
        {"nom": "Marrakech (Maroc)", "lat": 31.6295, "lon": -7.9811},
        {"nom": "Le Caire (Égypte)", "lat": 30.0444, "lon": 31.2357},
    ]
    carte2 = folium.Map(location=[30, 10], zoom_start=3)
    for dest in destinations:
        folium.Marker([dest["lat"], dest["lon"]], tooltip=dest["nom"]).add_to(carte2)
    st_folium(carte2, width=700, height=500)
