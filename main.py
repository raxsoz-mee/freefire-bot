import telebot
from telebot import types

bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")
CHANNEL_ID = "@qawcaze"

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status != 'left'
    except Exception:
        return False

# Паёми асосии бот, ки шумо хостед
MAIN_TEXT = """Ассалому Алейкум 🤖🤝👤

    🤖• дар бораи бот •🤖

Ин бот барои алмос ( алмаз ё ки 𝒅𝒊𝒂𝒎𝒐𝒏𝒅 ) гузаронидан ба бозии 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 аст ‼️

Ин бот метавонад алмосҳои шуморо дар муддати 5 дақиқа ба профили шумо бо 🆔 гузаронад ✅

Барои харидани алмос лутфан тугмаҳоро интихоб кунед :"""

# Функсия барои сохтани тугмаҳои алмос
def main_menu_buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_diamond = types.InlineKeyboardButton(text="𝒅𝒊𝒂𝒎𝒐𝒏𝒅 𝒕𝒐 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 💎", callback_data="buy_diamonds")
    btn_voucher = types.InlineKeyboardButton(text="𝒗𝒐𝒖𝒄𝒉𝒆𝒓 𝒕𝒐 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 🎫", callback_data="buy_vouchers")
    markup.add(btn_diamond, btn_voucher)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    
    if check_sub(user_id):
        bot.send_message(user_id, MAIN_TEXT, reply_markup=main_menu_buttons())
    else:
        markup = types.InlineKeyboardMarkup()
        btn_sub = types.InlineKeyboardButton(text="qawcaz", url="https://t.me/qawcaze")
        btn_done = types.InlineKeyboardButton(text="Обуна шудам ✅", callback_data="check_subscription")
        markup.add(btn_sub)
        markup.add(btn_done)
        
        bot.send_message(user_id, "Салом! Барои ботро истифода бурдан ба канали мо обуна шавед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_callback(call):
    user_id = call.from_user.id
    if check_sub(user_id):
        # Аввал паёми санҷиширо нест мекунем
        bot.delete_message(call.message.chat.id, call.message.message_id)
        # Паёми асосиро мефиристем
        bot.send_message(user_id, MAIN_TEXT, reply_markup=main_menu_buttons())
    else:
        bot.answer_callback_query(call.id, "Шумо ҳанӯз обуна нашудаед! ❌", show_alert=True)

# Барои он ки ҳангоми пахши тугмаҳо бот ҳоло чизе нагӯяд
@bot.callback_query_handler(func=lambda call: call.data in ["buy_diamonds", "buy_vouchers"])
def ignore_buttons(call):
    bot.answer_callback_query(call.id) # Танҳо "загрузка"-ро аз болои экран дур мекунад

bot.polling(none_stop=True)
