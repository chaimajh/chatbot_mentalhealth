from transformers import AutoTokenizer

# Remplacez MODEL_NAME par le nom correct de votre modèle
MODEL_NAME = "chaima7/Llama3.1_8b_finetuned_revised_v3"

# Essayez d'abord de charger le tokenizer normalement
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
except Exception as e:
    print(f"Error loading tokenizer: {e}")
    # Si vous souhaitez essayer de charger uniquement à partir de fichiers locaux
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, local_files_only=True)
    except Exception as e:
        print(f"Error loading tokenizer from local files: {e}")
def generate_response(user_input):
    # Logique pour générer une réponse à partir de l'entrée de l'utilisateur
    # Cela pourrait impliquer l'utilisation du tokenizer et du modèle
    response = f"Réponse générée pour l'entrée : {user_input}"
    return response
