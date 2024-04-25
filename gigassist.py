import telebot
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Инициализация GigaChat
chat = GigaChat(credentials='OWYzYzU1MzEtNGZhZi00ZDQxLWI2ODMtM2QxY2EyYTY5ZWEzOjhmOGNjMTAwLWUwOGUtNDgzZC1iZWFhLTcyMGE5YjY2YzAwZg==', verify_ssl_certs=False, scope="GIGACHAT_API_CORP")

TOKEN = '6801652454:AAHzgRPClNH2iIzNs6ljSt7jn5mnRD-F1PQ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Обработка входящего сообщения от пользователя
    user_input = message.text
    messages = [
        SystemMessage(
            content="Обработка входящего сообщения от пользователя."
        ),
        HumanMessage(content=user_input)
    ]
    res = chat.invoke(messages)
    bot.reply_to(message, res.content)

bot.polling()
