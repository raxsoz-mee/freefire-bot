import telebot
from telebot import types
from datetime import datetime

# ТОКЕН ВА МАЪЛУМОТ
bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")
CHANNEL_ID = "@qawcaze"
ADMIN_ID = 6895966276 # ID-и худро инҷо санҷ

# НАРХНОМА
PRICES = {
    "pack_105": {"name": "105 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 9.5},
    "pack_210": {"name": "210 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 19},
    "pack_326": {"name": "326 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 28.5},
    "pack_431": {"name": "431 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 38},
    "pack_546": {"name": "546 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 47.5},
    "pack_651": {"name": "651 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 57},
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
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_sub(user_id):
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text="𝒅𝒊𝒂𝒎𝒐𝒏𝒅 𝒕𝒐 𝙵𝚛ее 𝙵𝚒𝚛е 💎", callback_data="buy_diamonds"),
                   types.InlineKeyboardButton(text="𝒗𝒐𝒖𝒄𝒉𝒆𝒓 𝒕𝒐 𝙵𝚛ее 𝙵𝚒𝚛е 🎫", callback_data="buy_vouchers"))
        bot.send_message(user_id, """Ассалому Алейкум 🤖🤝👤

    🤖• дар бораи бот •🤖

Ин бот барои алмос ( алмаз ё ки 𝒅𝒊𝒂𝒎𝒐𝒏𝒅 ) гузаронидан ба бозии 𝙵𝚛ее 𝙵𝚒𝚛е аст ‼️

Ин бот метавонад алмосҳои шуморо дар муддати 5 дақиқа ба профили шумо бо 🆔 гузаронад ✅

Барои харидани алмос лутфан тугмаҳоро интихоб кунед :""", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="qawcaz", url="https://t.me/qawcaze"),
                   types.InlineKeyboardButton(text="Обуна шудам ✅", callback_data="check_sub"))
        bot.send_message(user_id, "Салом! Барои ботро истифода бурдан ба канали мо обуна шавед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_sub_btn(call):
    if check_sub(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)
    else:
        bot.answer_callback_query(call.id, "Шумо ҳанӯз обуна нашудаед! ❌", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "buy_diamonds")
def ask_id(call):
    msg = bot.send_message(call.message.chat.id, "Шумо дар ( 𝒅𝒊𝒂𝒎𝒐𝒏𝒅 𝒕𝒐 𝙵𝚛ее 𝙵𝚒𝚛е 💎 ) қарор доред ‼️\n\nЛутфан ба бот 🆔 - и худро фиристед :")
    bot.register_next_step_handler(msg, process_id_step)

def process_id_step(message):
    u_id = message.text
    if not u_id or not u_id.isdigit() or not (8 <= len(u_id) <= 14):
        msg = bot.send_message(message.chat.id, "Шумо иштибох кардед ‼️\nХарф бояд набошад ва ракам аз 8 то 14 то бошад ‼️\nЛутфан боз кушиш кунед :")
        bot.register_next_step_handler(msg, process_id_step)
        return
    user_data[message.chat.id] = {'game_id': u_id}
    markup = types.InlineKeyboardMarkup(row_width=1)
    for k, v in PRICES.items():
        markup.add(types.InlineKeyboardButton(text=f"{v['name']} = {v['price']} 🇹🇯", callback_data=k))
    bot.send_message(message.chat.id, f"🆔 Қабул карда шуд ✅\n\n• 🆔 : {u_id}\n\nЛутфан маҳсулотро интихоб кунед :", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pack_"))
def select_pack(call):
    pack = PRICES[call.data]
    user_data[call.message.chat.id].update({'pack': pack['name'], 'price': pack['price']})
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="𝙳𝚞𝚜𝚑𝚊н𝚋𝚎 𝙲𝚒𝚝𝚢 💳", callback_data="pay_dc"),
               types.InlineKeyboardButton(text="𝙽𝚘𝚝 𝙲𝚘р𝚍 🤷🏻", callback_data="pay_not_card"),
               types.InlineKeyboardButton(text="БА ҚАФО 🔃", callback_data="buy_diamonds"))
    bot.edit_message_text(f"Маҳсулот қабул карда карда шуд ✅\n\n• 🆔 : {user_data[call.message.chat.id]['game_id']}\n• 🛍️ : {pack['name']}\n• 💸 : {pack['price']} 🇹🇯\n\nАкнун ба супоридани маблағ мегузарем 🧾 :", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["pay_dc", "pay_not_card"])
def payment(call):
    price = user_data[call.message.chat.id]['price']
    markup = types.InlineKeyboardMarkup(row_width=1)
    if call.data == "pay_dc":
        markup.add(types.InlineKeyboardButton(text="𝙳𝚞𝚜𝚑𝚊н𝚋𝚎 𝙲𝚒𝚝𝚢 💳", url=f"http://pay.expresspay.tj/?A=9762000199713891&s={price}&c=_ADMIN_QAWCAZ_THEDANATERBOT_&f1=133"))
    markup.add(types.InlineKeyboardButton(text="𝑚𝑜𝑛𝑒𝑦 𝑖𝑠 𝑡𝑜 𝑎𝑑𝑚𝑖𝑛 𝑐𝑜𝑟𝑑 🧑‍💻", callback_data="request_check"))
    bot.edit_message_text(f"Лутфан {price} 🇹🇯 ба корт гузаронед:\n💳 9762000199713891\n\nБаъди супоридан тугмаи зерро пахш кунед:", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "request_check")
def request_check(call):
    msg = bot.send_message(call.message.chat.id, "Маблағ қабул карда шуд ✅\n\nЛутфан расми чеки маблағро ба бот фиристед ✅")
    bot.register_next_step_handler(msg, send_admin_panel)

def send_admin_panel(message):
    if message.content_type == 'photo':
        cid = message.chat.id
        u = message.from_user
        dt = datetime.now().strftime("%H:%M:%S")
        
        # МАЪЛУМОТ БАРОИ ТУ (БОСС)
        boss_msg = f"""Шумо махсулоти нов доред БОСС🕶

👤 КОРБАР : {u.first_name}
🗣 НОМБАР : @{u.username if u.username else "Надорад"}
🆔️ ТЕЛЕГРАМ : {u.id}
🛍 МАХСУЛОТ : {user_data[cid]['pack']}
💷 МАБЛАГ : {user_data[cid]['price']} 🇹🇯
🆔️ БОЗИ : {user_data[cid]['game_id']}
♻️ ВАКТ : {dt}

БОСС! Шумо ин махсулотро кабул мекунед ?"""

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("КАБУЛ ✅", callback_data=f"ok_{cid}"),
            types.InlineKeyboardButton("РАД ❌", callback_data=f"no_{cid}"),
            types.InlineKeyboardButton("НАВИСТАН БА МУШТАРИ 👤", url=f"tg://user?id={cid}")
        )
        bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=boss_msg, reply_markup=markup)
        bot.send_message(cid, "Расми чек қабул карда ✅\n⏳.....интизори админ.....⏳")
    else:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Танҳо расм фиристед!"), send_admin_panel)

@bot.callback_query_handler(func=lambda call: call.data.startswith(("ok_", "no_")))
def final_answer(call):
    target_id = int(call.data.split("_")[1])
    if call.data.startswith("ok_"):
        bot.send_message(target_id, "Маҳсулоти шумо бо муваффақият ба профилатон гузаронида шуд ✅\nБарои дидани расми чек @qawcaze 🧑‍💻")
        bot.answer_callback_query(call.id, "Фиристода шуд ✅")
    else:
        bot.send_message(target_id, "Шумо иштибоҳ кардед лутфан боз кӯшиш кунед ‼️\nИштибоҳ мумкин дар чек ё 🆔 аст ‼️")
        bot.answer_callback_query(call.id, "Рад шуд ❌")
    bot.edit_message_caption(caption=call.message.caption + "\n\nҶавоб дода шуд ✅", chat_id=call.message.chat.id, message_id=call.message.message_id)

bot.polling(none_stop=True)
