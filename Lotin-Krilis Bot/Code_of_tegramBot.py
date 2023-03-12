from transliterate import to_cyrillic , to_latin 
import telebot
#crylist_to1_lotin_bot
TOKEN="6000977401:AAGLbSUV2TCZn7zGTuhk8a8LwVsVYTFIAkY"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):       
    answer = "Bu dastur Tursunov Oybek tomonidan tuzilgan \nAssalomu alekum Xush kelibsiz...."
    answer += "\nMatn kiriting:" 
    bot.reply_to(message,answer)
    

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    msg=message.text
    answer=lambda text:to_cyrillic(text) if text.isascii() else to_latin(text) 
    bot.reply_to(message,answer(msg))

    
bot.polling()



#text=input("Input new text:")
#if text.isascii():
#    print(to_cyrillic(text))
#else:
#    print(to_latin(text)) 