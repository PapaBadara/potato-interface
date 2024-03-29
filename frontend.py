import streamlit as st
from PIL import Image
import requests
import numpy as np

# Fonction pour faire la prédiction
def predict(image):
    # Préparer les données pour la requête POST
    files = {"file" :  image}

    # Envoyer la requête à l'API FastAPI
    req = requests.post("http://localhost:8000/predict", files=files)

    # Extraire les résultats de la réponse JSON
    resultat = req.json()
    
    return resultat

# Titre de l'application
st.title("Classification d'Images de Pommes de Terre")

# Champ de téléchargement de fichier pour l'image
upload = st.file_uploader("Chargez votre image de pomme de terre",
                           type=['png', 'jpeg', 'jpg'])

# Si une image est téléchargée
if upload:
    # Faire la prédiction
    resultat = predict(upload.getvalue())
    
    # Afficher l'image téléchargée
    st.image(Image.open(upload), caption='Image de Pomme de Terre', use_column_width=True)
    
    # Afficher les résultats de la prédiction
    st.write(f"Classe prédite : {resultat['class']}")
    st.write(f"Confiance : {resultat['confidence']:.2f}")
