import telebot
from telebot import types
import datetime
import time
from flask import Flask
from threading import Thread

# --- ВЕБ-СЕРВЕР БАРОИ RENDER (БАРОИ ХОМӮШ НАШУДАН) ---
app = Flask('')
@app.route('/')
def home(): return "Бот фаъол аст!"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# --- ТАНЗИМОТ ---
TOKEN = '8664780965:AAG2Wp--1GF_K3yZiWt8Ll_0gSV-6Y4tr0E'
ADMIN_ID = 6895966276 
CHANNEL_ID = '@qawcaze'
MY_CARD = '9762000199713891'

bot = telebot.TeleBot(TOKEN)
user_data = {}

PRICES = {
    "105 💎": "9.70", "210 💎": "19.30", "326 💎": "28.90",
    "431 💎": "38.50", "546 💎": "48.20", "1113 💎": "97.20",
    "2398 💎": "195.80", "6160 💎": "494.30", "Ваучер лайт": "6.00",
    "Неделя": "17.00", "Месяц": "93.00", "Прокачка 1270 💎": "55.00",
    "Эво-пропуск 3-д": "10.00", "Эво-пропуск 7-д": "18.00", "Эво-пропуск 30-д": "42.00"
}

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except: return False

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    if check_sub(uid):
        text = ("Ассалому Алейкум  🤝\n\n• Ин бот 🗿 барои алмос 💎 донат кардан ба бозии Free Fire кор бурд шудааст ✅\n\n"
                "• Бот 🗿 метавонад бо 🆔 дар муддати 5️⃣ дақиқа алмосҳоятонро гузаронад 〽️\n\n• Лутфан бо кадом маҳсулот ба бози донат кунед ⁉️")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💎 МАҲСУЛОТҲО 💎", callback_data="ask_id_diamonds"))
        markup.add(types.InlineKeyboardButton("КОМБОХО 📊", callback_data="ask_id_combo"))
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📢 Обуна шудан", url="https://t.me/qawcaze"))
        markup.add(types.InlineKeyboardButton("✅ Тафтиш", callback_data="verify"))
        bot.send_message(message.chat.id, "Аввал ба канал обуна шавед:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    uid = call.from_user.id
    if call.data == "verify":
        if check_sub(uid):
            bot.delete_message(call.message.chat.id, call.message.id)
            start(call.message)
        else:
            bot.answer_callback_query(call.id, "❌ Обуна нашудаед!", show_alert=True)

    elif call.data == "back_to_main":
        bot.delete_message(call.message.chat.id, call.message.id)
        start(call.message)

    elif call.data == "ask_id_diamonds":
        user_data[uid] = {'target': 'diamonds', 'first_name': call.from_user.first_name, 'username': call.from_user.username}
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        bot.send_message(call.message.chat.id, "Лутфан 🆔-атонро фиристед ‼️✅", reply_markup=markup)

    elif call.data == "ask_id_combo":
        user_data[uid] = {'target': 'combo', 'first_name': call.from_user.first_name, 'username': call.from_user.username}
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        bot.send_message(call.message.chat.id, "Лутфан 🆔-атонро фиристед ‼️✅", reply_markup=markup)

    elif call.data.startswith("combo_"):
        c_type = call.data.split("_")[1]
        game_id = user_data[uid].get('id_game', '???')
        
        if c_type == "10":
            amount = "10.00"
            display_p = "Шумо 2-то ваучер на лайт бурд кардед 🤯"
            final_msg = f"Комбо 10сма\n\n🛍️ Маҳсулот қабул шуд ✅\n\n• 🛍️ : {display_p}\n• 🆔 : {game_id}\n\nМаблағи супориш: 10.00 сомонӣ\n\nБаъд аз пулро супоридан чекашро партоед ‼️📊🧾"
        elif c_type == "30":
            amount = "30.00"
            display_p = "Шумо 2-то ваучер на неделю бурд кардед 🤝"
            final_msg = f"Комбо 30сма\n\n🛍️ Маҳсулот қабул шуд ✅\n\n• 🛍️ : {display_p}\n• 🆔 : {game_id}\n\nМаблағи супориш: 30.00 сомонӣ\n\nБаъд аз пулро супоридан чекашро партоед ‼️📊🧾"
        elif c_type == "40":
            amount = "40.00"
            display_p = "Шумо хамаи пропуск-прокачкаро бурд кардед 🤷🏻"
            final_msg = f"Комбо 40сма\n\n🛍️ Маҳсулот қабул шуд ✅\n\n• 🛍️ : {display_p}\n• 🆔 : {game_id}\n\nМаблағи супориш: 40.00 сомонӣ\n\nБаъд аз пулро супоридан чекашро партоед ‼️📊🧾"

        user_data[uid].update({'product': display_p, 'price': amount})
        pay_url = f"http://pay.expresspay.tj/?A={MY_CARD}&s={amount}&c=&f1=133"
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("💳 Душанбе City", url=pay_url), 
                                                 types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        bot.edit_message_text(final_msg, call.message.chat.id, call.message.id, reply_markup=markup)

    elif call.data.startswith("select_"):
        product = call.data.split("_")[1]
        amount = PRICES.get(product, "0.00")
        user_data[uid].update({'product': product, 'price': amount})
        pay_url = f"http://pay.expresspay.tj/?A={MY_CARD}&s={amount}&c=&f1=133"
        final_msg = (f"🛍️ Маҳсулот қабул карда шуд ✅\n\n• 🛍️ : {product}\n• 🆔 : {user_data[uid].get('id_game', '???')}\n\n"
                     f"Нарх: {amount} сомонӣ\n\nБаъд аз пулро супоридан чекашро партоед ‼️📊🧾")
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("💳 Душанбе City", url=pay_url), 
                                                 types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        bot.edit_message_text(final_msg, call.message.chat.id, call.message.id, reply_markup=markup)

    elif call.data.startswith("adm_"):
        action, cust_id = call.data.split("_")[1], call.data.split("_")[2]
        if action == "yes":
            bot.send_message(cust_id, "Маҳсулоти шумо барқарор гардид барои дидани отзив @qawcaze 🥷✅")
            bot.edit_message_caption("✅ Қабул шуд!", call.message.chat.id, call.message.id)
        else:
            bot.send_message(cust_id, "Шумо иштибоҳ кардед боз кӯшиш кунед ‼️")
            bot.edit_message_caption("❌ Рад шуд!", call.message.chat.id, call.message.id)

@bot.message_handler(func=lambda m: m.text.isdigit())
def handle_id(message):
    uid = message.from_user.id
    if check_sub(uid):
        game_id = message.text
        # САНҶИШИ 🆔 (8-14 рақам)
        if len(game_id) < 8 or len(game_id) > 14:
            bot.reply_to(message, "Шумо 🆔 хато додаед ‼️\n🆔 бояд аз 8 то 14 рақам бошад ✅")
            return 

        target = user_data.get(uid, {}).get('target', 'diamonds')
        user_data[uid].update({'id_game': game_id})

        markup = types.InlineKeyboardMarkup(row_width=1)
        if target == 'combo':
            markup.add(types.InlineKeyboardButton("10 сомона 🛍️", callback_data="combo_10"),
                       types.InlineKeyboardButton("30 сомона 🛍️", callback_data="combo_30"),
                       types.InlineKeyboardButton("40 сомона 🛍️", callback_data="combo_40"),
                       types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        else:
            for name, price in PRICES.items():
                markup.add(types.InlineKeyboardButton(f"{name} — {price} 🇹🇯", callback_data=f"select_{name}"))
            markup.add(types.InlineKeyboardButton("⬅️ БА КАФО", callback_data="back_to_main"))
        
        bot.send_message(message.chat.id, f"🆔: {game_id} ✅\n\nЛутфан интихоб кунед 👇", reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def handle_receipt(message):
    uid = message.from_user.id
    if uid in user_data and 'product' in user_data[uid]:
        bot.reply_to(message, "Чек Кабул карда шуд ✅\nЛутфан интизор шавед то админ бинад 🥷🤳")
        caption = (f"💸 харидор: {user_data[uid].get('first_name')}\n🆔-тг: @{user_data[uid].get('username')}\n"
                   f"🛍️ маҳсулот: {user_data[uid]['product']}\n🆔-FF: {user_data[uid]['id_game']}\n"
                   f"🧾 нарх: {user_data[uid]['price']} см\n💳 Душанбе City ({MY_CARD})")
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("✅ ҚАБУЛ", callback_data=f"adm_yes_{uid}"),
                                                 types.InlineKeyboardButton("❌ РАД", callback_data=f"adm_no_{uid}"))
        bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption, reply_markup=markup)

if __name__ == "__main__":
    keep_alive()
    while True:
        try: bot.polling(none_stop=True, interval=0, timeout=20)
        except: time.sleep(10)
