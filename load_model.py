from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "chaima7/Llama3.1_8b_finetuned_revised_v3"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Modèle et tokenizer chargés avec succès!")
