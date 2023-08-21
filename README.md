# Multilingual Telegram Bot ( Saral )

## Introduction

The Multilingual Telegram Bot is an intelligent chatbot that can detect the language of incoming text or voice messages and respond with both text and voice messages in the same detected language. This project utilizes the power of OpenAI's GPT-3.5 Turbo model, the Telegram Bot API, Google Text-to-Speech (gTTS) library, langdetect, and moviepy to create a dynamic and multilingual chatbot experience.

## Features

- **Language Detection**: The bot can automatically detect the language of both text and voice messages using the langdetect library.

- **Multilingual Response**: It responds to messages with text and voice messages in the same detected language.

- **GPT-3.5 Turbo Integration**: Powered by OpenAI's GPT-3.5 Turbo, the bot generates contextually relevant responses.

- **User-Friendly Interface**: Users can seamlessly communicate with the bot through the familiar Telegram messaging platform.

## Setup and Usage

1. **API Key Setup**:
   - Obtain an API key from OpenAI and a Bot Token from Telegram.
   - Configure the API keys in your script.

2. **Environment Setup**:
   - Clone this repository to your local machine.
   - Install the required Python packages using `pip install -r requirements.txt`.

3. **Run the Bot**:
   - Execute the script to start the Telegram bot: `python your_bot_script.py`.

4. **Interact with the Bot**:
   - Send text or voice messages to the bot via Telegram.

## Dependencies

- OpenAI API: For generating intelligent responses based on user input.
- Telegram Bot API: To interact with users on the Telegram platform.
- gTTS (Google Text-to-Speech): Converts text to speech for bot responses.
- langdetect: Detects the language of the incoming text or voice messages.
- moviepy: Processes audio files for voice responses.
- 
## Limitations

- Language Detection Accuracy: Language detection for voice messages might not always be accurate, depending on the content and duration of the message.

- Multilingual GPT-3.5 Turbo: The bot generates responses based on English by default, and using other languages might require model fine-tuning.

## Feedback and Contributions

Feedback, bug reports, and contributions are welcome. Feel free to open issues or submit pull requests to enhance the bot's functionality.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

Enhance your Telegram chats with the Multilingual Telegram Bot. Engage in conversations in various languages and receive responses that match your preferred language. Experience the power of AI-driven language detection and natural language understanding.

*[Powered by OpenAI](https://openai.com)*

*[Telegram Bot API](https://core.telegram.org/bots)*

*[gTTS Library](https://pypi.org/project/gTTS/)*

*[langdetect Library](https://pypi.org/project/langdetect/)*

*[moviepy Library](https://pypi.org/project/moviepy/)*

