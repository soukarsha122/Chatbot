import openai
import gradio
from typing_extensions import Annotated, deprecated

openai.api_key = "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"

# emotions of the system
messages = [{"role": "system",
             "content": "You are a friend philosopher and guide"}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


# make the interface
demo = gradio.Interface(fn=CustomChatGPT, inputs="text",
                        outputs="text", title="Friend Philosopher and Guide")

# generate a sharable link
demo.launch(share=True)
