# Text Generation Comparison Using Gemini API and Local Model

This project demonstrates how to use Google's Generative AI (Gemini) API alongside a local transformer model (DistilGPT-2) to generate text responses based on a given prompt. The project includes functionality for comparing the outputs from the Gemini API and the local model.

## Requirements

- Python 3.7 or higher
- `google-generativeai`
- `pydantic`
- `transformers`
- `torch`

## Installation

### 1. Clone the repository:


git clone https://github.com/your-repo/text-generation-comparison.git
cd text-generation-comparison

## 3. Set up the Gemini API key:
Replace the placeholder API key in the script with your actual Gemini API key:
### genai.configure(api_key="YOUR_GEMINI_API_KEY")

