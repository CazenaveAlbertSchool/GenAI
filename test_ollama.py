import ollama

# Teste la connexion à Ollama
try:
    response = ollama.chat(
        model='mistral',
        messages=[{'role': 'user', 'content': 'Bonjour, comment ça va ?'}]
    )
    print("Réponse du modèle :")
    print(response['message']['content'])
except Exception as e:
    print(f"Erreur : {e}")
