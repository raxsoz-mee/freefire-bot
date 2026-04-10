import telebot
from telebot import types

bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")

# ID-и канал ё юзернейми он (бо @)
CHANNEL_ID = "@qawcaze"

def check_sub(user_id):
    try:
        # Статуси корбарро дар канал месанҷем
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status != 'left':
            return True
        else:
            return False
    except Exception:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    
    if check_sub(user_id):
        # Агар обуна бошад, паёми асосӣ меравад
        bot.send_message(user_id, "Хуш омадед! Шумо ба канал обуна ҳастед ва метавонед ботро истифода баред.")
    else:
        # Агар обуна набошад, тугмаи каналро нишон медиҳем
        markup = types.InlineKeyboardMarkup()
        btn_sub = types.InlineKeyboardButton(text="qawcaz", url=f"https://t.me/qawcaze")
        # Тугма барои санҷиши дубора (Check)
        btn_done = types.InlineKeyboardButton(text="Обуна шудам ✅", callback_data="check_subscription")
        markup.add(btn_sub)
        markup.add(btn_done)
        
        bot.send_message(user_id, 
                         "Салом! Барои ботро истифода бурдан ба канали мо обуна шавед:", 
                         reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_callback(call):
    if check_sub(call.from_user.id):
        bot.answer_callback_query(call.id, "Ташаккур барои обуна! ✅")
        bot.edit_message_text(chat_id=call.message.chat.id, 
                              message_id=call.message.message_id, 
                              text="Шумо муваффақона обуна шудед! Акнун метавонед ботро истифода баред.")
    else:
        bot.answer_callback_query(call.id, "Шумо ҳанӯз обуна нашудаед! ❌", show_alert=True)

bot.polling(none_stop=True)
