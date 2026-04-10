import telebot
from telebot import types

bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")

# Рӯйхати нархнома (барои осон шудани кор)
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

# Барои муваққатан нигоҳ доштани ID-и корбарон
user_data = {}

@bot.callback_query_handler(func=lambda call: call.data == "buy_diamonds")
def ask_id(call):
    msg = bot.send_message(call.message.chat.id, 
                           "Шумо дар холи хозир ( 𝒅𝒊𝒂𝒎𝒐𝒏𝒅 𝒕𝒐 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 💎 ) қарор доред ‼️\n\n"
                           "Лутфан ба бот 🆔 - и худро фиристед :")
    bot.register_next_step_handler(msg, process_id_step)
    bot.answer_callback_query(call.id)

def process_id_step(message):
    user_id_game = message.text
    user_data[message.chat.id] = {'game_id': user_id_game} # ID-ро дар хотира мегирем
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Сохтани тугмаҳо аз рӯи рӯйхати PRICES
    for key, val in PRICES.items():
        markup.add(types.InlineKeyboardButton(text=f"{val['name']} = {val['price']}", callback_data=key))
    
    bot.send_message(message.chat.id, 
                     f"🆔 Қабул карда шуд ✅\n\n"
                     f"• 🆔 : {user_id_game}\n\n"
                     f"Лутфан маҳсулотро барои ба профилатон гузаронидан интихоб кунед :", 
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pack_"))
def process_payment_step(call):
    chat_id = call.message.chat.id
    selected_pack = PRICES[call.data]
    
    # Гирифтани ID-е, ки пештар захира карда будем
    game_id = user_data.get(chat_id, {}).get('game_id', "Номаълум")
    
    result_text = f"""Маҳсулот қабул карда карда шуд ✅

• 🆔 : {game_id}
• 🛍️ : {selected_pack['name']}
• 💸 : {selected_pack['price']}

Ҳамаи рӯйхат пур карда шуд акнун ба супоридани маблағ мегузарем 🧾 :"""

    # Ин ҷо метавонед тугмаи пардохтро илова кунед
    markup = types.InlineKeyboardMarkup()
    btn_pay = types.InlineKeyboardButton(text="Пардохт кардан 💳", callback_data="pay_now")
    markup.add(btn_pay)

    bot.edit_message_text(chat_id=chat_id, 
                          message_id=call.message.message_id, 
                          text=result_text, 
                          reply_markup=markup)
    bot.answer_callback_query(call.id)

bot.polling(none_stop=True)
