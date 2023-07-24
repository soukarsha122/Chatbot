import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                          {"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)
