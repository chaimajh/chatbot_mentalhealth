# nomanapp/views.py

from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from transformers import pipeline

# Chargez votre modèle fine-tuné ici
chatbot = pipeline('text-generation', model='chaima7/Llama3.1_8b_finetuned_revised_v3')

def chatbot_view(request):
    if request.method == 'GET':
        return render(request, 'nomanapp/chatbot.html')
    elif request.method == 'POST':
        user_input = request.POST.get('user_input')  # Récupérer la saisie de l'utilisateur
        try:
            response = chatbot(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        except Exception as e:
            response = "Désolé, une erreur est survenue lors de la génération de la réponse."
        return render(request, 'nomanapp/chatbot.html', {'response': response})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
