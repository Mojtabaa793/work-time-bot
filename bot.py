import telebot
from datetime import datetime

# توکن ربات خود را اینجا قرار دهید
token = 7713603481:AAGdIa9LY8qq0m3WDHJC-nWmKisq6EaXCig
bot = telebot.TeleBot(token)

# دیکشنری برای ذخیره زمان‌های ورود و خروج کاربران
time_logs = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "سلام! من ربات ثبت ساعت کاری هستم. برای ثبت ورود /in و برای ثبت خروج /out را ارسال کنید.")

@bot.message_handler(commands=['in'])
def clock_in(message):
    user_id = message.chat.id
    time_logs[user_id] = {'in': datetime.now()}
    bot.send_message(user_id, "ورود شما ثبت شد.")

@bot.message_handler(commands=['out'])
def clock_out(message):
    user_id = message.chat.id
    if user_id in time_logs and 'in' in time_logs[user_id]:
        time_logs[user_id]['out'] = datetime.now()
        bot.send_message(user_id, "خروج شما ثبت شد.")
    else:
        bot.send_message(user_id, "ابتدا باید ورود خود را ثبت کنید.")

bot.polling()
