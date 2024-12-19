import transformers 
import torch
from huggingface_hub import login
from datetime import date
import subprocess
import os
import re
login('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')
import textwrap  
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import logging
logging.getLogger("transformers").setLevel(logging.ERROR)
# functions.py
Llama = None

def generate_prompt(choice: int, place: str, activity: str = None):
  if choice == 1: # Function logic for activity recommendation
        return f"Generate a list of 5 must try activities in {place}. Make sure to include a brief description, the address of the location, and star rating. Style this list as a text document but do not write any annotations explaining the styling"
  elif choice == 2: # Function logic for food recommendation
        return f"Generate a list of 5 must try food in {place}. Make sure to include a brief description, the address of the location, and star rating. Style this list as a text document but do not write any annotations explaining the styling"
  elif choice == 3: # Function logic for custom recommendation
        return f"Generate a list of 5 must try {activity} in {place}. Make sure to include a brief description, the address of the location, and star rating. Style this list as a text document but do not write any annotations explaining the styling"
  elif choice == 4: #  Function logic for trip planner recommendation
        return f"Generate a list of must try activities, food, and more as a vacation planner in {place}.Make sure to include the address of the location and star rating. Style this list as a text document. give time blocks and an order from the start of the day to the end of the day. make sure the time blocks are realistic based on distance and group stuff together is they are closer in distance. make sure this document can fit a 9x11 document."
  else:
        return "Invalid choice, please select a valid option."
  
def start_model():
    print("Initializing the model...")
    try:
        # Create pipeline for text generation (using CPU)
        Llama = pipeline("text-generation", 
                         model="meta-llama/Llama-3.2-3B-Instruct", 
                         device=-1,truncation=True, max_length=175)
    except Exception as e:
        print(f"Error during model start up: {e}")
    
def recommended_response(choice: int):
      try:
        place=input("Which location?: ")
        print(f"\nGetting recommendations for {place}...")
        #prompt = f"Generate a list of 5 must try food in {place}. Make sure to include a breif description, the address of the location, and star rating. Style this list as a text document but do not write any annotations explaining the styling"
        prompt = generate_prompt(choice,place)
        generated_output = Llama(prompt)[0]['generated_text']
        # Slice the generated text to exclude the prompt
        generated_text = generated_output[len(prompt):]

        print("\nGenerated text:", generated_text)

      except Exception as e:
        print(f"Error during model start up: {e}")

def custom_recomendation(choice: str):
      try:
        place=input("Which location?: ")
        print(f"\nGetting {choice} recommendations for {place}...")
        #prompt = f"Generate a list of 5 must try food in {place}. Make sure to include a breif description, the address of the location, and star rating. Style this list as a text document but do not write any annotations explaining the styling"
        prompt = generate_prompt(3, place, choice)
        generated_output = Llama(prompt)[0]['generated_text']
        # Slice the generated text to exclude the prompt
        generated_text = generated_output[len(prompt):]

        print("\nGenerated text:", generated_text)

      except Exception as e:
        print(f"Error during model start up: {e}")