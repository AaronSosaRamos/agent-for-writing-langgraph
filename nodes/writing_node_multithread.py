from langchain.schema import Document
from chains.write_chain import write_chain
import threading
from queue import Queue

def count_words(text):
    """
    Count the number of words in the given text.

    Args:
        text (str): The input text to count words from.

    Returns:
        int: The number of words in the text.
    """
    # Split the text into words and count them
    words = text.split()
    return len(words)

def writing_node_multithread(state):
    """Take the initial prompt and write a plan to make a long doc."""
    print("---WRITING THE DOC---")
    initial_instruction = state['initial_prompt']
    plan = state['plan']
    num_steps = int(state['num_steps'])
    num_steps += 1

    plan = plan.strip().replace('\n\n', '\n')
    planning_steps = plan.split('\n')
    text = ""
    responses = [None] * len(planning_steps)

    if len(planning_steps) > 50:
        print("Plan is too long")
        return

    def worker(idx, step, result_queue):
        """Worker function to invoke the write_chain for a given step."""
        result = write_chain.invoke({
            "intructions": initial_instruction,
            "plan": plan,
            "text": text,
            "STEP": step
        })
        result_queue.put((idx, result))

    # Create a queue to store results
    result_queue = Queue()

    # Start threads for each planning step
    threads = []
    for idx, step in enumerate(planning_steps):
        thread = threading.Thread(target=worker, args=(idx, step, result_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Collect results from the queue and order them sequentially
    while not result_queue.empty():
        idx, result = result_queue.get()
        responses[idx] = result

    # Combine responses sequentially
    final_doc = '\n\n'.join(responses)

    # Count words in the final document
    word_count = count_words(final_doc)
    print(f"Total word count: {word_count}")
    print(f""" 
          STEP 2: 
          Final doc: {final_doc}
          Word count: {word_count}
          Num. steps: {num_steps}
        """)

    return {"final_doc": final_doc, "word_count": word_count, "num_steps": num_steps}
