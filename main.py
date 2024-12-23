import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv, find_dotenv
from graph.graph import create_workflow

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Create the workflow
app = create_workflow()

# test instruction
test_instruction = "Write a 5000-word piece on Large Language Models (LLMs), exploring their architecture, real-world applications, and the societal implications of their use. \
    Discuss the parallels between LLMs and themes of intelligence, creativity, and decision-making. \
    Finally, analyze the potential future directions of LLM development and the challenges they may face in scaling and ethical deployment."

# Run the workflow
inputs = {"initial_prompt": test_instruction,  
          "num_steps": 0,
          "llm_name": "google_gemini_1_5_flash_multithreading"}
output = app.invoke(inputs)

print(output)