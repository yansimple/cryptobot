import time
import telebot
tgtoken = "1758380315:AAFdT2dIjqYAbea9o5GAGgNhMYbWna-25hI"
bot = telebot.TeleBot(tgtoken)
db = open("DataBaseId.txt", "r")
list_id = db.read()
list_id_splited = list_id.split(",")
print(list_id_splited)
for id in list_id_splited:
    print(id)
    Post_text = "test push"

    def send_post():
        bot.send_message(id, Post_text)
        print("was send '"+id+"'")
        time.sleep(1)
    try:
        send_post()
    except:
        print("\nUser id '"+id+"' stop use Bot\n")
        continue