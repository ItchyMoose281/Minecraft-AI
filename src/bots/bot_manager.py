from javascript import require, Once

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')


class MineflayerManager():
  def __init__(self, host='localhost', port=25565):
    self.host = host
    self.port = port
    self.botlist = {}

  def initialize_bots(self, number_of_bots=1, **kwargs):
    for i in range(number_of_bots):
      BOT_USERNAME = f'{i + 1}'

      bot_instance = mineflayer.createBot({
        'host': self.host,
        'port': self.port,
        'username': BOT_USERNAME,
        'hideErrors': False
      })


      # Listens for this specific bot's login event
      @Once(bot_instance, 'login')
      def on_login(this):
        # 'this' is the JS bot wrapper. By now, .chat() is fully loaded.
        this.loadPlugin(pathfinder.pathfinder)
        this.chat(f"Hello, I am {this.username}!")
        print(f'bot {BOT_USERNAME} logged in')

      self.botlist[BOT_USERNAME] = bot_instance

  def setMovements(self, **kwargs):
    movements = {}
    for bot_name, bot_instance in self.botlist.items():
      movements[bot_name] = pathfinder.Movements(bot_instance)
      for key, value in kwargs.items():
        setattr(movements[bot_name], key, value)
    bot_instance.pathfinder.setMovements(movements[bot_name])
    print(f"Set bot {bot_name}'s movements")