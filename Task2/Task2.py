import google.generativeai as genai
import os
from pydantic import BaseModel, ValidationError
from transformers import pipeline, AutoTokenizer

# Initialize the tokenizer (choose the correct model)
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Configure Gemini API key
genai.configure(api_key="AIzaSyC3SDFNANoMrbANDQfH1gfDqH5hDyh0G-I")

# Define the Pydantic model for response validation
class GeminiResponse(BaseModel):
    text: str  # Only include text, as metadata is not available

# Function to create prompt text for analysis
def create_prompt(text: str) -> str:
    return f"Explain how artificial intelligence works in simple terms. Include the following points:\n1. Core Concepts\n2. The Process\n3. Limitations"

# Function to call Gemini API
def call_gemini_api(prompt: str) -> GeminiResponse:
    try:
        # Initialize the model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content using the Gemini model
        response = model.generate_content(prompt)
        
        # Validate the response
        validated_response = GeminiResponse(text=response.text)
        return validated_response
    except ValidationError as ve:
        raise ValueError(f"Response validation error: {ve}")
    except Exception as e:
        raise Exception(f"Error calling Gemini API: {e}")

# Load a local model (e.g., DistilGPT-2)
local_model = pipeline("text-generation", model="distilgpt2")

# Function to call the local model
def call_local_model(prompt: str) -> GeminiResponse:
    try:
        # Use a larger max_length for better response
        response = local_model(prompt, max_length=200)
        generated_text = response[0]['generated_text']
        
        # Validate the response
        validated_response = GeminiResponse(text=generated_text)
        return validated_response
    except ValidationError as ve:
        raise ValueError(f"Response validation error: {ve}")
    except Exception as e:
        raise Exception(f"Error calling local model: {e}")

# Function to compare responses from Gemini API and local model
def compare_outputs(external_response: GeminiResponse, local_response: GeminiResponse):
    print("External API Response:")
    print(external_response.json())
    
    print("\nLocal Model Response:")
    print(local_response.json())

# Example usage
if __name__ == "__main__":
    raw_text = "Explain how artificial intelligence works."
    prompt = create_prompt(raw_text)

    try:
        # Tokenize the text
        encoded_text = tokenizer.encode(raw_text, truncation=True, max_length=512)
        print(f"Encoded text: {encoded_text}")

        # Generate structured response using Gemini API
        structured_response_gemini = call_gemini_api(prompt)
        
        # Generate structured response using local model
        structured_response_local = call_local_model(prompt)
        
        # Compare outputs
        compare_outputs(structured_response_gemini, structured_response_local)
        
    except Exception as e:
        print(f"An error occurred: {e}")
