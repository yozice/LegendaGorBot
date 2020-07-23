import telebot, requests
API_TOKEN = '1348622485:AAH5EECF1ndzjQL5XDGQfTQ2kyr_r7-83HY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Серега!!!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

@bot.message_handler(content_types=['document', 'photo'])
def send_image(message):
    raw = message.photo[0].file_id
    file_info = bot.get_file(raw)
    path = '/downloads/'+raw+'.jpg'
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path, 'wb') as new_file:
        new_file.write(downloaded_file)

    #file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))

    bot.send_photo(message.chat.id, downloaded_file)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()