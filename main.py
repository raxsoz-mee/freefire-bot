import telebot
from telebot import types
import time

# --- ТАНЗИМОТ ---
TOKEN = '8664780965:AAG2Wp--1GF_K3yZiWt8Ll_0gSV-6Y4tr0E'
ADMIN_ID = 6895966276 
CHANNEL_ID = '@qawcaze'
MY_CARD = '9762000199713891'

bot = telebot.TeleBot(TOKEN)
user_data = {}

# Танҳо Алмосҳо
DIAMOND_PRICES = {
    "105 💎": "9.70", "210 💎": "19.30", "326 💎": "28.90",
    "431 💎": "38.50", "546 💎": "48.20", "1113 💎": "97.20",
    "2398 💎": "195.80", "6160 💎": "494.30"
}

# Танҳо Ваучерҳо
VOUCHER_PRICES = {
    "Ваучер лайт": "6.00",
    "Неделя": "17.00",
    "Месяц": "93.00",
    "Прокачка 1270 💎": "55.00"
}

# Танҳо Эво-пропуск
EVO_PRICES = {
    "Эво-пропуск 3-д": "10.00", 
    "Эво-пропуск 7-д": "18.00", 
    "Эво-пропуск 30-д": "42.00"
}

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    user_data[uid] = {'first_name': message.from_user.first_name, 'username': message.from_user.username}
    if check_sub(uid):
        # МАТНИ НАВИ ШУМО
        text = (
            "Ассалому Алейкум 🤝\n\n"
            "• Ин бот 🗿 барои алмос 💎 донат кардан ба бозии Free Fire кор бурд шудааст ✅\n\n"
            "• Бот 🗿 метавонад бо 🆔 дар муддати 5️⃣ дақиқа алмосҳоятонро гузаронад 〽️\n\n"
            "• Лутфан бо кадом маҳсулот ба бози донат кунед ⁉️"
        )
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("💎 МАҲСУЛОТҲО 💎", callback_data="ask_id_diamonds"),
            types.InlineKeyboardButton("ВАУЧЕРҲО 🧾", callback_data="ask_id_vouchers"),
            types.InlineKeyboardButton("КОМБОҲО 📊", callback_data="ask_id_combo"),
            types.InlineKeyboardButton("ЭВО-ПРОПУССК 〽️", callback_data="ask_id_evo")
        )
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📢 Обуна шудан", url="https://t.me/qawcaze"))
        markup.add(types.InlineKeyboardButton("✅ Тафтиш", callback_data="verify"))
        bot.send_message(message.chat.id, "Аввал ба канал обуна шавед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    uid = call.from_user.id
    if uid not in user_data: user_data[uid] = {'first_name': call.from_user.first_name, 'username': call.from_user.username}
    
    if call.data == "verify":
        if check_sub(uid):
            bot.delete_message(call.message.chat.id, call.message.id); start(call.message)
        else:
            bot.answer_callback_query(call.id, "❌ Обуна нашудаед!", show_alert=True)
    
    elif call.data == "back_to_main":
        bot.delete_message(call.message.chat.id, call.message.id); start(call.message)

    elif call.data in ["ask_id_diamonds", "ask_id_vouchers", "ask_id_combo", "ask_id_evo"]:
        if call.data == "ask_id_diamonds": user_data[uid]['target'] = 'diamonds'
        elif call.data == "ask_id_vouchers": user_data[uid]['target'] = 'vouchers'
        elif call.data == "ask_id_combo": user_data[uid]['target'] = 'combo'
        else: user_data[uid]['target'] = 'evo'
        
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        bot.edit_message_text("Лутфан 🆔-атонро фиристед ‼️✅", call.message.chat.id, call.message.id, reply_markup=markup)

    elif call.data.startswith(("select_", "voucher_", "evo_", "combo_")):
        if call.data.startswith("select_"):
            product = call.data.replace("select_", "")
            amount = DIAMOND_PRICES.get(product, "0.00")
        elif call.data.startswith("voucher_"):
            product = call.data.replace("voucher_", "")
            amount = VOUCHER_PRICES.get(product, "0.00")
        elif call.data.startswith("evo_"):
            product = call.data.replace("evo_", "")
            amount = EVO_PRICES.get(product, "0.00")
        else:
            c_val = call.data.split("_")[1]
            combos = {"10": "2-то ваучер на лайт", "30": "2-то ваучер на неделю", "40": "Пропуск-прокачка"}
            product = combos.get(c_val, "Комбо")
            amount = f"{c_val}.00"

        user_data[uid].update({'product': product, 'price': amount})
        game_id = user_data[uid].get('id_game', '???')
        
        pay_msg = (f"🛍️ Маҳсулот қабул карда шуд ✅\n\n• 🛍️ : {product}\n• 🆔 : {game_id}\n• Нарх : {amount} сомонӣ\n\nЛутфан Душанбе City - ро интихоб кунед ✅")
        pay_url = f"http://pay.expresspay.tj/?A={MY_CARD}&s={amount}&c=&f1=133"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💳 Душанбе City", url=pay_url))
        markup.add(types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        bot.edit_message_text(pay_msg, call.message.chat.id, call.message.id, reply_markup=markup)
        bot.send_message(call.message.chat.id, "Пас аз пардохт, лутфан чекро (скриншот) ба ҳамин ҷо фиристед ‼️📊🧾")

    elif call.data.startswith("adm_"):
        action, cust_id = call.data.split("_")[1], call.data.split("_")[2]
        msg = "Маҳсулоти шумо барқарор гардид ✅" if action == "yes" else "❌ Рад шуд! Иштибоҳ кардед."
        bot.send_message(cust_id, msg)
        bot.edit_message_caption("Иҷро шуд!", call.message.chat.id, call.message.id)

@bot.message_handler(func=lambda m: m.text.isdigit())
def handle_id(message):
    uid = message.from_user.id
    if check_sub(uid):
        if len(message.text) < 8 or len(message.text) > 14:
            bot.reply_to(message, "🆔 хато! Бояд 8-14 рақам бошад.")
            return
        if uid not in user_data: user_data[uid] = {}
        user_data[uid]['id_game'] = message.text
        target = user_data[uid].get('target', 'diamonds')
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        if target == 'combo':
            markup.add(types.InlineKeyboardButton("10 см 🛍️", callback_data="combo_10"),
                       types.InlineKeyboardButton("30 см 🛍️", callback_data="combo_30"),
                       types.InlineKeyboardButton("40 см 🛍️", callback_data="combo_40"))
        elif target == 'evo':
            for n, p in EVO_PRICES.items():
                markup.add(types.InlineKeyboardButton(f"{n} — {p} см", callback_data=f"evo_{n}"))
        elif target == 'vouchers':
            for n, p in VOUCHER_PRICES.items():
                markup.add(types.InlineKeyboardButton(f"{n} — {p} см", callback_data=f"voucher_{n}"))
        else:
            for n, p in DIAMOND_PRICES.items():
                markup.add(types.InlineKeyboardButton(f"{n} — {p} см", callback_data=f"select_{n}"))
        
        markup.add(types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        bot.send_message(message.chat.id, f"🆔: {message.text} ✅\nИнтихоб кунед:", reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def handle_receipt(message):
    uid = message.from_user.id
    if uid in user_data and 'product' in user_data[uid]:
        bot.reply_to(message, "Чек қабул шуд! Интизор шавед...")
        caption = (f"Харидор: {user_data[uid].get('first_name')}\n🛍️ Маҳсулот: {user_data[uid]['product']}\n🆔 FF: {user_data[uid]['id_game']}\n🧾 Нарх: {user_data[uid]['price']} см")
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("✅ ҚАБУЛ", callback_data=f"adm_yes_{uid}"), types.InlineKeyboardButton("❌ РАД", callback_data=f"adm_no_{uid}"))
        bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption, reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()
