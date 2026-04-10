import telebot
from telebot import types

bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")

# Матни менюи асосӣ
MAIN_TEXT = """Ассалому Алейкум 🤖🤝👤

    🤖• дар бораи бот •🤖

Ин бот барои алмос ( алмаз ё ки 𝒅𝒊𝒂𝒎𝒐𝒏𝒅 ) гузаронидан ба бозии 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 аст ‼️

Ин бот метавонад алмосҳои шуморо дар муддати 5 дақиқа ба профили шумо бо 🆔 гузаронад ✅

Барои харидани алмос лутфан тугмаҳоро интихоб кунед :"""

# Функсия барои сохтани тугмаҳои менюи асосӣ
def main_menu_buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_diamond = types.InlineKeyboardButton(text="𝒅𝒊𝒂𝒎𝒐𝒏𝒅 𝒕𝒐 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 💎", callback_data="buy_diamonds")
    btn_voucher = types.InlineKeyboardButton(text="𝒗𝒐𝒖𝒄𝒉𝒆𝒓 𝒕𝒐 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 🎫", callback_data="buy_vouchers")
    markup.add(btn_diamond, btn_voucher)
    return markup

# 1. Вақте ки тугмаи "diamond to Free Fire" пахш мешавад
@bot.callback_query_handler(func=lambda call: call.data == "buy_diamonds")
def ask_id(call):
    # Паёми пурсиши ID
    msg = bot.send_message(call.message.chat.id, 
                           "Шумо дар холи хозир ( 𝒅𝒊𝒂𝒎𝒐𝒏𝒅 𝒕𝒐 𝙵𝚛𝚎𝚎 𝙵𝚒𝚛𝚎 💎 ) қарор доред ‼️\n\n"
                           "Лутфан ба бот 🆔 - и худро фиристед :")
    
    # Ботро интизор мемонем, ки паёми навбатиро (ID) гирад
    bot.register_next_step_handler(msg, process_id_step)
    bot.answer_callback_query(call.id)

# 2. Қабули ID ва намоиши он
def process_id_step(message):
    user_id_game = message.text # ID-и бозие, ки корбар фиристод
    
    # Сохтани тугмаҳо барои интихоби маҳсулот (нархномаро баъдтар илова мекунем)
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="100 💎", callback_data="pack_100")
    btn2 = types.InlineKeyboardButton(text="210 💎", callback_data="pack_210")
    markup.add(btn1, btn2)
    
    # Паёми тасдиқи ID бо нишон додани худи ID
    bot.send_message(message.chat.id, 
                     f"🆔 Қабул карда шуд ✅\n\n"
                     f"• 🆔 : {user_id_game}\n\n"
                     f"Лутфан маҳсулотро барои ба профилатон гузаронидан интихоб кунед :", 
                     reply_markup=markup)

# Оғози бот (қисми /start ва ғайра бояд бошад)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, MAIN_TEXT, reply_markup=main_menu_buttons())

bot.polling(none_stop=True)
