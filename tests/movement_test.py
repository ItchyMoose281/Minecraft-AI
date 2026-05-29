from javascript import require, On, Once

from src.bots.bot_manager import MineflayerManager

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

manager = MineflayerManager()
manager.initialize_bots()

bot = manager.botlist['1']

@Once(bot, 'login')
def on_login(this):
    manager.setMovements()

RANGE_GOAL = 1

@On(bot, 'chat')
def handleMsg(sender, message, *args):
    if sender and (sender != '1'):
        try:

            xpos, ypos, zpos = map(int, message.split(' '))

            bot.pathfinder.setGoal(pathfinder.goals.GoalNear(xpos, ypos, zpos, RANGE_GOAL))

        except ValueError:
            # This handles cases where chat messages aren't "X, Z" numbers
            print(f"Ignored chat message (not valid coordinates): {message}")
