# Pokémon Card Chatbot avec Ollama

Ce projet est un chatbot spécialisé pour les collectionneurs de cartes Pokémon, utilisant un modèle de langage local (Mistral ou Llama3) via Ollama.

---

## 📋 Prérequis

- Un système macOS (ou Linux/Windows avec les adaptations nécessaires).
- Python 3.8 ou supérieur installé.
- Une connexion internet pour télécharger les modèles.

---

## 🛠 Installation

### 1. Installer Ollama

#### Sur macOS :
1. Télécharge l'application Ollama depuis [ollama.com](https://ollama.com/).
2. Ouvre le fichier `.dmg` et glisse Ollama dans le dossier **Applications**.
3. Lance Ollama depuis le Launchpad ou Spotlight.

#### Sur Linux :
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Telecharger un modele de langage 

ollama pull mistral


## 🚀 Lancer l'application
### 1. Lancer le serveur Ollama

Sur macOS/Linux : Le serveur se lance automatiquement avec l'application Ollama.
Sur Windows : Le serveur se lance automatiquement après l'installation.

Vérifie que le serveur est actif :
````bash
curl http://localhost:11434
````

(Tu devrais voir {"status":"OK"}.)

### 2. Lancer l'application Streamlit
Exécute la commande suivante pour démarrer l'application :
```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans ton navigateur à l'adresse http://localhost:8501
