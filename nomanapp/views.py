from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# Chargez et initialisez le modèle
model_path = hf_hub_download(
    repo_id="chaima7/Llama3.1_8b_finetuned_revised_v3",
    filename="unsloth.Q8_0.gguf"
)

llm = Llama(
    model_path=model_path,  # Utiliser le chemin du modèle téléchargé
    n_ctx=2048,
    n_gpu_layers=-1
)

def chatbot_view(request):
    if request.method == 'GET':
        return render(request, 'nomanapp/chatbot.html')
    elif request.method == 'POST':
        user_input = request.POST.get('user_input')  # Récupérer la saisie de l'utilisateur
        try:
            # Créer une complétion avec le modèle
            response = llm.create_completion(
                prompt=user_input,
                max_tokens=50,  # Limiter le nombre de tokens générés
                temperature=0.7
            )["choices"][0]["text"]  # Récupérer le texte généré
        except Exception as e:
            response = "Désolé, une erreur est survenue lors de la génération de la réponse."
        return render(request, 'nomanapp/chatbot.html', {'response': response})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
