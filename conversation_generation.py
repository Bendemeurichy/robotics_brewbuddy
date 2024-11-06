import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained DialoGPT model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_response(input_text):
    # Encode the input text
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")

    # Generate response using the model
    response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode the response
    response_text = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    return response_text

def main():
    while True:
        input_text = input("You: ")
        if input_text.lower() in ["exit", "quit"]:
            break
        response_text = generate_response(input_text)
        print(f"Bot: {response_text}")

if __name__ == "__main__":
    main()
