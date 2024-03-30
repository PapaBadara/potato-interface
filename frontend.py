import streamlit as st
from PIL import Image
import requests
import numpy as np

# Fonction pour faire la prédiction
def predict(image):
    # Préparer les données pour la requête POST
    files = {"file": image}

    # URL de l'API FastAPI hébergée sur GitHub
    api_url = "https://potato-interface.herokuapp.com/predict"

    try:
        # Envoyer la requête à l'API FastAPI
        req = requests.post(api_url, files=files)
        
        # Vérifier si la requête a réussi
        if req.status_code == 200:
            # Extraire les résultats de la réponse JSON
            resultat = req.json()
            return resultat
        else:
            # En cas d'échec de la requête, afficher un message d'erreur
            st.error(f"Erreur lors de la requête à l'API : {req.status_code}")
    except Exception as e:
        # En cas d'erreur lors de la requête, afficher un message d'erreur
        st.error(f"Erreur lors de la requête à l'API : {str(e)}")

# Titre de l'application
st.title("Classification d'Images de Pommes de Terre")

# Champ de téléchargement de fichier pour l'image
upload = st.file_uploader("Chargez votre image de pomme de terre",
                           type=['png', 'jpeg', 'jpg'])

# Si une image est téléchargée
if upload:
    # Faire la prédiction
    resultat = predict(upload.getvalue())
    
    # Si la prédiction s'est déroulée avec succès
    if resultat:
        # Afficher l'image téléchargée
        st.image(Image.open(upload), caption='Image de Pomme de Terre', use_column_width=True)
        
        # Afficher les résultats de la prédiction
        st.write(f"Classe prédite : {resultat.get('class', 'Erreur lors de la prédiction')}")
        st.write(f"Confiance : {resultat.get('confidence', 'Erreur lors de la prédiction'):.2f}")
