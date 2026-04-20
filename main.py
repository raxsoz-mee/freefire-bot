import telebot
from telebot import types
from datetime import datetime
import os

bot = telebot.TeleBot("8461445139:AAEN_FwlOjymRTUi5OSeJf7VfRdD7vZT84Y")
CHANNEL_ID = "@od1naevff"
ADMIN_ID = 6895966276

# НАРХНОМАИ АЛМОС ВА ВАУЧЕР
PRICES = {
    "pack_105": {"name": "105 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 9.5},
    "pack_210": {"name": "210 𝐝𝐢𝐚𝐦𝐨𝐧𝐝 💎", "price": 19},
    "pack_326": {"name": "326 𝐝𝐢𝐚𝐦𝐨н𝐝 💎", "price": 28.5},
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
    # ВАУЧЕРҲО
    "v_month": {"name": "𝒗𝒐𝒖𝒄𝒉𝒆𝒓 𝒎𝒐𝒏𝒕𝒉 2600 💎", "price": 95},
    "v_nedelya": {"name": "𝒗𝒐𝒖𝒄𝒉𝒆𝒓 𝒏𝒆𝒅𝒆𝒍𝒚𝒐𝒖 450 💎", "price": 15.5},
    "v_layt": {"name": "𝒗𝒐𝒖𝒄𝒉𝒆𝒓 𝒍𝒂𝒚𝒕 90 💎", "price": 6},
    "v_propusk": {"name": "𝒑𝒓𝒐𝒑𝒖𝒔𝒌 𝙵𝚛ее 𝙵𝚒𝚛е 1270 💎", "price": 45},
}

user_data = {}

def save_user(user_id):
    if not os.path.exists("users.txt"):
        with open("users.txt", "w") as f: f.write("")
    with open("users.txt", "r") as f:
        users = f.read().splitlines()
    if str(user_id) not in users:
        with open("users.txt", "a") as f:
            f.write(str(user_id) + "\n")

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return
