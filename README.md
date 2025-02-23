For starting to use this project, you have to fill this fields:

'''
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

cats_channal_ip = 'CHANNEL_WITH_CATS'
dogs_channal_ip = 'CHANNEL_WITH_DOGS'

password_for_panel = 'CHOOSE_THE_PASSWORD'
'''

It's a telegram bot with admin panel.

In this case, two channels are connected to the bot, in which it sends interesting 
photos and facts about cats and dogs every hour (the information is 
obtained from API keys that are publicly available).
