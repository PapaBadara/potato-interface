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

        # Vérifier le statut de la réponse
        if req.status_code == 200:
            # Si la réponse est réussie, décoder la réponse en JSON
            resultat = req.json()
            return resultat
        else:
            # Si la réponse n'est pas réussie, retourner une erreur avec le code de statut
            return {"error": f"Erreur {req.status_code} lors de la requête à l'API."}
    except requests.exceptions.RequestException as e:
        # Si une erreur de requête se produit, retourner une erreur
        return {"error": f"Erreur de requête : {str(e)}"}

# Titre de l'application
st.title("Classification d'Images de Pommes de Terre")

# Champ de téléchargement de fichier pour l'image
upload = st.file_uploader("Chargez votre image de pomme de terre",
                           type=['png', 'jpeg', 'jpg'])

# Si une image est téléchargée
if upload:
    # Faire la prédiction
    resultat = predict(upload.getvalue())
    
    # Si la prédiction s'est déroulée sans erreur
    if "error" not in resultat:
        # Afficher l'image téléchargée
        st.image(Image.open(upload), caption='Image de Pomme de Terre', use_column_width=True)
        
        # Afficher les résultats de la prédiction
        st.write(f"Classe prédite : {resultat['class']}")
        st.write(f"Confiance : {resultat['confidence']:.2f}")
    else:
        # Si une erreur s'est produite lors de la prédiction, afficher un message d'erreur
        st.error(resultat["error"])
