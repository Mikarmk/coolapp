import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace these values with your API keys
DALLI_API_KEY = 'dalli_api_key'
CHATGPT_API_KEY = 'chatgpt_api_key'

# Function for sending a request to the DALL-E 3 API
def generate_image(prompt):
    url = 'https://api-inference.huggingface.co/models/runwayml/dalle-v2'
    headers = {'Authorization': f'Bearer {DALLI_API_KEY}'}
    data = {'inputs': prompt}
    response = requests.post(url, headers=headers, json=data)
    image_url = response.json()[0]['image']
    return image_url

# Function for sending a request to ChatGPT
def generate_text(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {'Authorization': f'Bearer {CHATGPT_API_KEY}'}
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 2048
    }
    response = requests.post(url, headers=headers, json=data)
    text = response.json()['choices'][0]['message']['content']
    return text

# Function for processing the /generate command
def generate(update: Update, context: CallbackContext) -> None:
    prompt = update.message.text[len('/generate'):]
    image_url = generate_image(prompt)
    text = generate_text(prompt)
    update.message.reply_text(f'Image: {image_url}\nText: {text}')

# Creating an instance of Updater and starting the bot
def main() -> None:
    updater = Updater(token=os.environ.get('TELEGRAM_BOT_TOKEN'), use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("generate", generate))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
