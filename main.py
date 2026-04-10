import telebot
import os
from telebot import types

# Токенро аз Railway мегирад
TOKEN = os.getenv('8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y')
bot = telebot.TeleBot(TOKEN)

# Юзернейми канали шумо
CHANNEL_USERNAME = "@qawcaze"

def check_sub(user_id):
    try:
        # Методи get_chat_member барои санҷиши обуна
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        # Агар корбар дар канал бошад, статусаш 'left' нест
        if member.status != 'left':
            return True
        return False
    except Exception as e:
        print(f"Хатогӣ: {e}")
        return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_sub(user_id):
        bot.send_message(message.chat.id, "Хуш омадед! Шумо аллакай ба канал обуна ҳастед ва метавонед ботро истифода баред.")
    else:
        # Сохтани тугма барои обуна шудан
        markup = types.InlineKeyboardMarkup()
        btn_sub = types.InlineKeyboardButton(text="Обуна шудан ба канал", url=f"https://t.me")
        # Тугмаи "Санҷиш" пас аз обуна шудан
        btn_check = types.InlineKeyboardButton(text="Санҷиши обуна", callback_data="check_subscription")
        markup.add(btn_sub)
        markup.add(btn_check)
        
        bot.send_message(
            message.chat.id, 
            "Барои истифодаи бот, лутфан ба канали мо обуна шавед:", 
            reply_markup=markup
        )

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def callback_check(call):
    if check_sub(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Ташаккур барои обуна! Акнун бот барои шумо дастрас аст.")
    else:
        bot.answer_callback_query(call.id, "Шумо ҳоло ҳам обуна нашудаед!", show_alert=True)

if __name__ == "__main__":
    bot.infinity_polling()
