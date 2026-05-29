from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')

def initialize_bots(number_of_bots=1):

  bot_dict = {}

  for i in range(number_of_bots):
    BOT_USERNAME = f'player_{i+1:03d}'
    bot = mineflayer.createBot({ 'host': '127.0.0.1', 'port': 12345, 'username': BOT_USERNAME, 'hideErrors': False })
    bot_dict[BOT_USERNAME] = bot

  for name, bot in bot_dict.items():
    #The spawn event
    once(bot, 'login')
    bot.chat(f'{BOT_USERNAME} spawned')

# while True:
#   for name, bot in bot_dict.items():
#     @On(bot, 'chat')
#     def breakListener(sender, message, *args):
#       print(sender, message, args)
#       if sender and (sender not in bot_dict.keys()):
#         if 'break' in message:
#           pos = bot.entity.position.offset(0, -1, 0)
#           blockUnder = bot.blockAt(pos)
#           if bot.canDigBlock(blockUnder):
#             bot.chat(f"I'm breaking the '{blockUnder.name}' block underneath")
#             # The start=True parameter means to immediately invoke the function underneath
#             # If left blank, you can start it with the `start()` function later on.
#             try:
#               @AsyncTask(start=True)
#               def break_block(task):
#                 bot.dig(blockUnder)
#               bot.chat('I started digging!')
#             except Exception as e:
#               bot.chat(f"I had an error {e}")
#           else:
#             bot.chat(f"I can't break the '{blockUnder.name}' block underneath")
#         if 'stop' in message:
#           off(bot, 'chat', breakListener)