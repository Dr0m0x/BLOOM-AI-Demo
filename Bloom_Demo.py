from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load conversational model (consider DialoGPT for better results)
model_name = "bigscience/bloom-560m"  # Replace with "microsoft/DialoGPT-medium" for fine-tuned dialogue
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Move model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

# Set system instruction for structured responses
system_instruction = (
    "You are a concise assistant. "
    "Respond clearly and professionally, in no more than 2 sentences. "
    "Avoid unrelated information or rambling."
)

print("Assistant is ready! Type your question below or type 'exit' to quit.\n")

while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Combine system instruction and user input
    prompt = f"{system_instruction}\n\nUser: {user_input}\nAssistant:"

    # Tokenize prompt
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)

    # Generate response with stricter limits
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=50,          # Limit new tokens to avoid rambling
        temperature=0.5,            # Reduce randomness
        top_k=40,                   # Limit sampling diversity
        top_p=0.85,                 # Use nucleus sampling for coherence
        do_sample=True,             # Enable sampling mode
        repetition_penalty=1.5,     # Penalize repeated phrases
        eos_token_id=tokenizer.eos_token_id  # Stop at end-of-sentence
    )

    # Decode and post-process response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.split("Assistant:")[-1].strip()
    print(f"BLOOM: {response}\n")
