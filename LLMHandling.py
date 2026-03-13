from ollama import ChatResponse, chat, generate


def init():
    print("Warming model...")
    generate(model="wizardlm2")
    print("Model ready.")

def get_response(options):
  prompt = (
  f"Please consider the following options and choose the one that best fits the answer.\n"
  f"You will receive a list of tuples, where each tuple contains an index and an effect description.\n"
  f"Your task is to analyze the effects and determine which one is the best upgrade of the given choices.\n"
  f"Do not provide any explanation, just return the index and effect of the best option.\n"
  f"Here are the options:\n"
  f"{options}\n"
  )

  response: ChatResponse = chat(
    model="wizardlm2",
    messages=[
      {
        'role': 'system',
        'content': prompt
      },
    ]
  )

  return response['message']['content']
