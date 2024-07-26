#from youtube_search import YoutubeSearch
from Rooz import Download
from kvsqlite.sync import Client
from telebot import types
#from time import sleep
import telebot,requests,os

db = Client('pn.hex')

bot = telebot.TeleBot('7187436465:AAHgE4TZ59zHEpXkJ1q4ov0Ic87X6xuN7y4') #‌‌ توکن ربات خود را وارد کنید


boss = types.InlineKeyboardMarkup(row_width=2)
kral = types.InlineKeyboardButton(text='Kral.. ♪ ,',url='irkral.t.me')
boss.add(kral)


#aov = types.InlineKeyboardMarkup(row_width=2)
#audio = types.InlineKeyboardButton(text='• فایل صوتی ♪',callback_data='au')
#video = types.InlineKeyboardButton(text='• ویدیو 🎞️ ',callback_data='vid')
#aov.add(audio,video)



@bot.message_handler(commands=['start'])
def start(message):
  fe = types.InlineKeyboardMarkup(row_width=2)
  dirt = types.InlineKeyboardButton(text='🧑🏻‍💻',url='irkral.t.me')
  fe.add(dirt)
  iid = message.from_user.id
  name = message.from_user.first_name
  ms = message.chat.id
  db.set(f'n_{ms}',name)
  id = message.from_user.id
#	db.set(f'id_{iid}',id)
  dmj = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})'
  db.set(f'n_{ms}',dmj)
  bot.reply_to(message,f'To The bot download from Pinterest Welcome to send your link',parse_mode='markdown',reply_markup=fe)

@bot.message_handler(func=lambda m:True)
def SaD(m):
  iid = m.from_user.id
  name = m.from_user.first_name
  ms = m.chat.id
  mm = m.text
  if m.text.startswith("https://pin.it/") or m.text.startswith('https://www.pinterest.com/pin/'):
  	do = Download(mm).DownPinterest()['video']
  	req = requests.get(do).content
  	ow = open(f'{iid}.mp4','wb')
  	ow.write(req)
  	rb = open(f'{iid}.mp4','rb')
  	bot.send_video(ms,video=rb,
  	caption='Done ✓',
  	reply_markup=boss)
  	os.remove(f'{iid}.mp4')
  else:
  	bot.reply_to(m,'Error in download :(')
		
bot.infinity_polling()	
# Coded By @MrKRAL
# Channel Opend @irkral
# نویسنده این سورس @MrKRAL میباشد 
# اوپن شده در کانال کرال تیم @irkral
