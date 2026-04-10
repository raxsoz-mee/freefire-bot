import telebot
from telebot import types

bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")
CHANNEL_ID = "@qawcaze"

# Рӯйхати ПУРРАИ нархнома
PRICES = {
    "pack_105": {"name": "105 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "9.5 🇹🇯"},
    "pack_210": {"name": "210 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "19 🇹🇯"},
    "pack_326": {"name": "326 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "28.5 🇹🇯"},
    "pack_431": {"name": "431 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "38 🇹🇯"},
    "pack_546": {"name": "546 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "47.5 🇹🇯"},
    "pack_651": {"name": "651 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "57 🇹🇯"},
    "pack_756": {"name": "756 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "66.5 🇹🇯"},
    "pack_872": {"name": "872 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "76 🇹🇯"},
    "pack_977": {"name": "977 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "85.5 🇹🇯"},
    "pack_1113": {"name": "1113 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "95 🇹🇯"},
    "pack_1544": {"name": "1544 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "135 🇹🇯"},
    "pack_2398": {"name": "2398 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "190 🇹🇯"},
    "pack_3511": {"name": "3511 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "285 🇹🇯"},
    "pack_4796": {"name": "4796 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "380 🇹🇯"},
    "pack_6160": {"name": "6160 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "475 🇹🇯"},
    "pack_7273": {"name": "7273 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "570 🇹🇯"},
    "pack_8558": {"name": "8558 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "665 🇹🇯"},
    "pack_9671": {"name": "9671 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "760 🇹🇯"},
    "pack_10956": {"name": "10 956 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "855 🇹🇯"},
    "pack_12320": {"name": "12 320 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": "950 🇹🇯"},
}

user_data = {}

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status != 'left'
    except:
        return False

MAIN_TEXT = """Ассалому Алейкум 🤖🤝👤

    🤖• дар бораи бот •🤖

Ин бот барои алмос ( алмаз ё ки 𝒅𝒊𝒂𝒎𝒐𝒏𝒅 ) гузаронидан ба бозии 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 аст ‼️

Ин бот метавонад алмосҳои шуморо дар муддати 5 дақиқа ба профили шумо бо 🆔 гузаронад ✅

Барои харидани алмос лутфан тугмаҳоро интихоб кунед :"""

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
        btn_sub = types.InlineKeyboardButton(text="Обуна шудан 📢", url="https://t.me/qawcaze")
        btn_done = types.InlineKeyboardButton(text="Обуна шудам ✅", callback_data="check_subscription")
        markup.add(btn_sub, btn_done)
        bot.send_message(user_id, "Салом! Барои ботро истифода бурдан аввал ба канали мо обуна шавед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_callback(call):
    if check_sub(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, MAIN_TEXT, reply_markup=main_menu_buttons())
    else:
        bot.answer_callback_query(call.id, "Шумо ҳанӯз обуна нашудаед! ❌", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "buy_diamonds")
def ask_id(call):
    msg = bot.send_message(call.message.chat.id, "Лутфан ба бот 🆔 - и худро фиристед :")
    bot.register_next_step_handler(msg, process_id_step)
    bot.answer_callback_query(call.id)

def process_id_step(message):
    user_id_game = message.text
    if not user_id_game.isdigit() or not (8 <= len(user_id_game) <= 14):
        msg = bot.send_message(message.chat.id, "Шумо иштибох кардед ‼️\nХарф бояд набошад ва ракам аз 8 то 14 то бошад ‼️\nБоз кӯшиш кунед:")
        bot.register_next_step_handler(msg, process_id_step)
        return
    
    user_data[message.chat.id] = {'game_id': user_id_game}
    markup = types.InlineKeyboardMarkup(row_width=1)
    for key, val in PRICES.items():
        markup.add(types.InlineKeyboardButton(text=f"{val['name']} = {val['price']}", callback_data=key))
    bot.send_message(message.chat.id, f"🆔 Қабул шуд: {user_id_game}\nИнтихоб кунед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pack_"))
def process_payment(call):
    selected_pack = PRICES[call.data]
    game_id = user_data.get(call.message.chat.id, {}).get('game_id', "Номаълум")
    res_text = f"Маҳсулот қабул шуд ✅\n\n• 🆔 : {game_id}\n• 🛍️ : {selected_pack['name']}\n• 💸 : {selected_pack['price']}\n\nБа супоридани маблағ мегузарем 🧾"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Пардохт кардан 💳", callback_data="pay_now"))
    bot.edit_message_text(res_text, call.message.chat.id, call.message.message_id, reply_markup=markup)

bot.polling(none_stop=True)
