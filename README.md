# BLOOM-Chat-Demo

A project exploring the conversational capabilities of the **BLOOM** language model. This repository demonstrates how to build an interactive AI chatbot using Hugging Face's BLOOM model, focusing on natural language processing (NLP) and dynamic dialogue generation.

---

## Features

- **Interactive Chatbot**: Engage in real-time conversations with the BLOOM language model.
- **Customizable Prompts**: Modify system instructions to experiment with tone, style, and behavior.
- **Dynamic Response Generation**: Generate human-like responses using parameters like temperature, top-k, and top-p for flexibility.
- **Efficient Input Management**: Handles conversation history for context-aware dialogue.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/BLOOM-Chat-Demo.git
   cd BLOOM-Chat-Demo
   ```

2. **Set Up a Python Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install transformers torch
   ```

4. **Run the Chatbot**:
   ```bash
   python bloom_chatbot.py
   ```

---

## Usage

1. **Run the Chatbot**:
   Start the chatbot by running:
   ```bash
   python bloom_chatbot.py
   ```

2. **Interact with BLOOM**:
   Type your input into the terminal, and the chatbot will respond. Example interaction:
   ```
   You: Hello!
   BLOOM: Hi there! How can I assist you today?
   ```

3. **Customize Behavior**:
   Modify the `system_instruction` variable in the script to adjust the chatbot’s tone and style:
   ```python
   system_instruction = (
       "You are a conversational AI assistant. "
       "Engage in friendly and helpful conversations with users."
   )
   ```

---

## Model Details

This project uses the **BLOOM-560m** model from Hugging Face, a multilingual large language model capable of generating coherent text. Larger versions of BLOOM (e.g., BLOOM-7b1 or BLOOM-176b) can also be integrated for enhanced performance.

For more information about BLOOM, visit the [Hugging Face BLOOM model page](https://huggingface.co/bigscience/bloom).

---

## Roadmap

Future enhancements for this project include:
- Adding a web-based interface (e.g., Flask or Streamlit).
- Expanding support for larger BLOOM variants.
- Fine-tuning BLOOM for specific conversational tasks.

---

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers): For providing the BLOOM model and tools.
- [BigScience Initiative](https://bigscience.huggingface.co/): For developing BLOOM.







