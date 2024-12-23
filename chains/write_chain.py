import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from models.models import get_llm

# Load the write prompt template
with open(os.path.join(os.path.dirname(__file__), 'prompts', 'write.txt'), 'r') as file:
    write_template = file.read()

# Create a ChatPromptTemplate
write_prompt = ChatPromptTemplate([
    ('user', write_template)
    ])

# Create the write chain
write_chain = write_prompt | get_llm("gemini-1.5-flash", temperature=0) | StrOutputParser()

if __name__ == "__main__":
    # Test the write_chain
    test_instruction = "Write a 1500-word essay about the advancements in large language models (LLMs), covering their transformative potential, limitations, and ethical challenges in modern AI applications."

    test_plan = "Paragraph 1 - Main Point: Introduction to LLMs and their growing impact on AI applications - Word Count: 200 words"

    test_text = "Large Language Models (LLMs) have emerged as a cornerstone of modern AI, reshaping how machines process and generate human-like text across diverse domains."

    # Invoke the write_chain
    result = write_chain.invoke({
        "intructions": test_instruction,
        "plan": test_plan,
        "text": test_text,
        "STEP": "Paragraph 1"
    })
    
    # Print the result
    print("Generated Paragraph:")
    print(result)