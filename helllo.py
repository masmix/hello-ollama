import ollama

response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Say Hello World',
  },
])
print(response['message']['content'])
