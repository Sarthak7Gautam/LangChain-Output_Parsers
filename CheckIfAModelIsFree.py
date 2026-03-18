from huggingface_hub import InferenceClient

client = InferenceClient()
client.text_generation(model="mistralai/Mistral-7B-Instruct-v0.1", prompt="Hello")

## If it throws error not free 