from javascript import require, On, Once

from src.bots.bot_manager import MineflayerManager

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

manager = MineflayerManager(name='1')
bot = manager.bot

@Once(bot, 'login')
def on_login(this):
    pass

RANGE_GOAL = 1

@On(bot, 'chat')
def handleMsg(sender, message, *args):
    if sender and (sender != '1'):
        try:

            xpos, ypos, zpos = map(int, message.split(' '))

            bot.pathfinder.setGoal(pathfinder.goals.GoalNear(xpos, ypos, zpos, RANGE_GOAL))

        except ValueError:
            pass
