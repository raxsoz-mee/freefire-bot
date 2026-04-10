import telebot
from telebot import types

# ТОКЕН ВА КАНАЛ
bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")
CHANNEL_ID = "@qawcaze"
ADMIN_USERNAME = "@qawcaz"  # Юзернейми админ барои хабардор кардан
ADMIN_ID = 6895966276 # Ин ҷо ID-и худро гузор (рақам), то бот ба ту расмҳоро фиристад

# НАРХНОМА (PRICES)
PRICES = {
    "pack_105": {"name": "105 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 9.5},
    "pack_210": {"name": "210 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 19},
    "pack_326": {"name": "326 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 28.5},
    "pack_431": {"name": "431 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 38},
    "pack_546": {"name": "546 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 47.5},
    "pack_651": {"name": "651 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 57},
    "pack_756": {"name": "756 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 66.5},
    "pack_872": {"name": "872 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 76},
    "pack_977": {"name": "977 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 85.5},
    "pack_1113": {"name": "1113 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 95},
    "pack_1544": {"name": "1544 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 135},
    "pack_2398": {"name": "2398 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 190},
    "pack_3511": {"name": "3511 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 285},
    "pack_4796": {"name": "4796 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 380},
    "pack_6160": {"name": "6160 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 475},
    "pack_7273": {"name": "7273 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 570},
    "pack_8558": {"name": "8558 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 665},
    "pack_9671": {"name": "9671 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 760},
    "pack_10956": {"name": "10 956 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 855},
    "pack_12320": {"name": "12 320 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 950},
}

user_data = {}

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status != 'left'
    except:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_sub(user_id):
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton(text="𝒅𝒊𝒂𝒎𝒐𝒏𝒅 𝒕𝒐 𝙵𝚛𝚎е 𝙵𝚒𝚛𝚎 💎", callback_data="buy_diamonds"),
            types.InlineKeyboardButton(text="𝒗𝒐𝒖𝒄𝒉𝒆𝒓 𝒕𝒐 𝙵𝚛ее 𝙵𝚒𝚛𝚎 🎫", callback_data="buy_vouchers")
        )
        bot.send_message(user_id, "Ассалому Алейкум 🤖🤝👤\n\nБарои харидани алмос тугмаҳоро интихоб кунед :", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="qawcaz", url="https://t.me/qawcaze"),
                   types.InlineKeyboardButton(text="Обуна шудам ✅", callback_data="check_subscription"))
        bot.send_message(user_id, "Салом! Барои ботро истифода бурдан ба канали мо обуна шавед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "buy_diamonds")
def ask_id(call):
    msg = bot.send_message(call.message.chat.id, "Лутфан ба бот 🆔 - и худро фиристед :")
    bot.register_next_step_handler(msg, process_id_step)

def process_id_step(message):
    u_id = message.text
    if not u_id or not u_id.isdigit():
        bot.send_message(message.chat.id, "🆔 бояд танҳо рақам бошад!")
        return
    user_data[message.chat.id] = {'game_id': u_id}
    markup = types.InlineKeyboardMarkup(row_width=1)
    for k, v in PRICES.items():
        markup.add(types.InlineKeyboardButton(text=f"{v['name']} = {v['price']} 🇹🇯", callback_data=k))
    bot.send_message(message.chat.id, f"🆔: {u_id}\nМаҳсулотро интихоб кунед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pack_"))
def process_diamond_selection(call):
    chat_id = call.message.chat.id
    selected = PRICES[call.data]
    user_data[chat_id]['price'] = selected['price']
    user_data[chat_id]['pack_name'] = selected['name']
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="𝙳𝚞𝚜𝚑𝚊𝚗𝚋𝚎 𝙲𝚒𝚝𝚢 💳", callback_data="pay_dc"),
        types.InlineKeyboardButton(text="𝙽𝚘𝚝 𝙲𝚘𝚛𝚍 🤷🏻", callback_data="pay_not_card"),
        types.InlineKeyboardButton(text="БА ҚАФО 🔃", callback_data="buy_diamonds")
    )
    text = f"Маҳсулот қабул шуд ✅\n\n🆔: {user_data[chat_id]['game_id']}\n🛍️: {selected['name']}\n💸: {selected['price']} 🇹🇯\n\nБа супоридани маблағ мегузарем 🧾:"
    bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["pay_dc", "pay_not_card"])
def payment_method(call):
    chat_id = call.message.chat.id
    price = user_data[chat_id]['price']
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    if call.data == "pay_dc":
        link = f"http://pay.expresspay.tj/?A=9762000199713891&s={price}&c=2249&f1=133"
        markup.add(types.InlineKeyboardButton(text="𝙳𝚞𝚜𝚑𝚊𝚗𝚋𝚎 𝙲𝚒𝚝𝚢 💳", url=link))
        text = "Шумо 𝙳𝚞𝚜𝚑𝚊н𝚋𝚎 𝙲𝚒𝚝𝚢 ро интихоб кардед. Ба барнома гузашта пардохт кунед ✅"
    else:
        text = f"Шумо бо корти мо дастраси надоштаед ‼️\n\n💳: 9762000199713891\n💸: {price} 🇹🇯"

    markup.add(types.InlineKeyboardButton(text="𝑚𝑜𝑛𝑒𝑦 𝑖𝑠 𝑡𝑜 𝑎𝑑𝑚𝑖𝑛 𝑐𝑜𝑟𝑑 🧑‍💻", callback_data="request_receipt"))
    markup.add(types.InlineKeyboardButton(text="БА ҚАФО 🔃", callback_data="buy_diamonds"))
    bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "request_receipt")
def request_receipt(call):
    msg = bot.send_message(call.message.chat.id, "Маблағ қабул карда шуд ✅\n\nЛутфан расми чеки маблағро ба бот фиристед ✅")
    bot.register_next_step_handler(msg, handle_receipt)

def handle_receipt(message):
    chat_id = message.chat.id
    if message.content_type == 'photo':
        # Ба корбар ҷавоб додан
        bot.send_message(chat_id, "Расми чек қабул карда ✅\n\n⏳.....интизори админ.....⏳")
        
        # Маълумоти фармоиш
        game_id = user_data.get(chat_id, {}).get('game_id', "Номаълум")
        pack = user_data.get(chat_id, {}).get('pack_name', "Номаълум")
        price = user_data.get(chat_id, {}).get('price', "Номаълум")
        user_name = f"@{message.from_user.username}" if message.from_user.username else "Бе юзернейм"

        caption = f"🔔 Фармоиши нав!\n👤 Корбар: {user_name}\n🆔 Геймер: {game_id}\n🛍️ Маҳсулот: {pack}\n💸 Маблағ: {price} 🇹🇯"
        
        # Фиристодани чек ба админ
        bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption)
        bot.send_message(ADMIN_ID, f"Барои тамос: {user_name}")
    else:
        msg = bot.send_message(chat_id, "Лутфан танҳо расм (чек) фиристед!")
        bot.register_next_step_handler(msg, handle_receipt)

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_callback(call):
    if check_sub(call.from_user.id):
        start(call.message)
    else:
        bot.answer_callback_query(call.id, "Шумо ҳанӯз обуна нашудаед!", show_alert=True)

if __name__ == "__main__":
    bot.polling(none_stop=True)
