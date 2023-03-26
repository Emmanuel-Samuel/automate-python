# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 18/03/2023
# REVISED DATE: 18/03/2023
# PURPOSE: Create a crypto trading bot

# import our functions from the classes
from function import BOT
from threading import Thread

# creates 2 simultaneous trading bots
first_bot = BOT("BTCUSDT", 0.001, 5, 1, 1)
second_bot = BOT("ETHUSDT", 0.01, 5, 1, 1)
third_bot = BOT("MATICUSDT", 0.01, 5, 1, 1)

# function for running bot 1
def bot_1():
    first_bot.run()

# function for running bot 2
def bot_2():
    second_bot.run()

# function for running bot 3
def bot_3():
    third_bot.run()

# create Thread, store as tbot
tbot_1 = Thread(target=bot_1)
tbot_2 = Thread(target=bot_2)
tbot_3 = Thread(target=bot_3)

# start
tbot_1.start()
tbot_2.start()
tbot_3.start()
