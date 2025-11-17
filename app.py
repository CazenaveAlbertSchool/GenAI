import streamlit as st
import ollama
import requests

# Configuration de la page
st.set_page_config(page_title="Pokémon Card Chatbot", page_icon="🃏")
st.title("🃏 Pokémon Card Chatbot")
st.write("Posez-moi une question sur les cartes Pokémon !")

# Charger le prompt système
with open("prompts/system_prompt.txt", "r") as f:
    system_prompt = f.read()

# Fonction pour interroger le LLM local (Ollama)
def ask_llm(question, model="mistral"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    return response["message"]["content"]

# Fonction pour récupérer des données depuis l'API Pokémon (optionnel)
def fetch_pokemon_card(name):
    url = f"https://api.pokemontcg.io/v2/cards?q=name:{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"][0] if data["data"] else None
    return None

# Interface utilisateur
user_question = st.text_input("Votre question :")
if st.button("Envoyer"):
    if user_question:
        with st.spinner("Réflexion en cours..."):
            # Option 1 : Réponse basée sur le LLM seul
            answer = ask_llm(user_question)
            st.write("**Réponse :**")
            st.write(answer)

            # Option 2 : Intégration avec l'API Pokémon (exemple)
            if "valeur de la carte" in user_question.lower():
                card_name = user_question.split("valeur de la carte ")[-1].strip()
                card_data = fetch_pokemon_card(card_name)
                if card_data:
                    st.write("**Données API :**")
                    st.json(card_data)

# Instructions
st.sidebar.markdown("""
### Instructions
1. Posez une question sur une carte Pokémon.
2. Exemples :
   - "Quelle est la valeur de la carte Pikachu Illustrator ?"
   - "Quelles sont les cartes les plus rares de la série Base Set ?"
""")
