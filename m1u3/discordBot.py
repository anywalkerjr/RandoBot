import discord
import random
from setting import settings
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

def magicBall():
    answer = random.choice(['Focus an ask again', 'Yes', 'No', 'No doubt about it', "Chances aren't good", "Can't say now"])
    return answer

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$magicBall'): #после $magicBall вопрос
        await message.channel.send("The Ball says: " + magicBall())
    elif message.content.startswith('$randomNumber'):
        await message.channel.send("Random number: " + str(random.randint(0,100)))
    else:
        await message.channel.send(message.content)

client.run(settings["TOKEN"])