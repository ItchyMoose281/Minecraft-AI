from javascript import require, Once, On
import random

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

def command_handler(sender, message, manager):
  if sender != manager.bot.username and "#" == message[0]:
    split_msg = message[1:].split()
    if split_msg[0] == "state":
      manager.query_state()
      manager.bot.chat(str(manager.last_state[split_msg[1]]))
    if split_msg[0] == "come":
      pos = manager.bot.players[sender].entity.position
      manager.bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, 1))


class MineflayerManager:
  def __init__(self, name=str(random.randint(0, 1000)), host='localhost', port=25565):
    self.movements = None
    self.host = host
    self.port = port

    self.bot_username = name
    self.last_state = {}

    self.bot = mineflayer.createBot({
      'host': self.host,
      'port': self.port,
      'username': self.bot_username,
      'hideErrors': False
    })

    @Once(self.bot, 'login')
    def on_login(this):
      this.loadPlugin(pathfinder.pathfinder)
      this.chat(f"Hello, I am {this.username}!")
      print(f'bot {self.bot_username} logged in')
      self.set_movements()
      self.query_state()

    @On(self.bot, 'chat')
    def on_message(sender, message, *args):
      print(message)
      command_handler(sender, message, self)

    @On(self.bot, 'whisper')
    def on_whisper(sender, message, *args):
      print(message)
      command_handler(sender, message, self)


  def set_movements(self, **kwargs):
    self.movements = pathfinder.Movements(self.bot)
    for key, value in kwargs.items():
      setattr(self.movements, key, value)
    self.bot.pathfinder.setMovements(self.movements)
    print(f"Set bot {self.bot_username}'s movements")

  def query_state(self):
    self.last_state["entities"] = self.bot.entites
    self.last_state["held_item"] = self.bot.held_item
    self.last_state["dimension"] = self.bot.game.dimension
    self.last_state["difficulty"] = self.bot.game.difficulty
    self.last_state["players"] = self.bot.players
    self.last_state["is_raining"] = self.bot.isRaining
    self.last_state["experience"] = self.bot.experience.points
    self.last_state["health"] = self.bot.health
    self.last_state["food"] = self.bot.food
    self.last_state["oxygen_level"] = self.bot.oxygenLevel
    self.last_state["time_of_day"] = self.bot.time.timeOfDay
    self.last_state["day"] = self.bot.time.day
    self.last_state["inventory"] = self.bot.inventory
    return self.last_state


