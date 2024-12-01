# Text Generation Comparison Using Gemini API and Local Model

This project demonstrates how to use Google's Generative AI (Gemini) API alongside a local transformer model (DistilGPT-2) to generate text responses based on a given prompt. The project includes functionality for comparing the outputs from the Gemini API and the local model.

## Requirements

- Python 3.7 or higher
- `google-generativeai`
- `pydantic`
- `transformers`
- `torch`

## Installation

###  Clone the repository:


git clone https://github.com/your-repo/text-generation-comparison.git
cd text-generation-comparison

##  Set up the Gemini API key:
Replace the placeholder API key in the script with your actual Gemini API key:
### genai.configure(api_key="YOUR_GEMINI_API_KEY")


# How It Works
## 1. Gemini API:
The Gemini API is used to generate a text response based on a given prompt. It uses Google's Generative AI models (such as gemini-1.5-flash) to produce the output.

## 2. Local Model (DistilGPT-2):
The DistilGPT-2 model is loaded locally using Hugging Face's transformers library. It generates text responses based on the same prompt as the Gemini API.

 ## 3. Comparison:
Once both models generate a response, the script compares the output from the Gemini API and the local model by printing their text responses.

## Conclusion
This project allows you to compare the text generation capabilities of an external (Gemini API) and a local model (DistilGPT-2). By running this script, you can observe how both models handle the same prompt and analyze the differences in their generated responses.

