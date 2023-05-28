import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
botPrefix = '!'
bot = commands.Bot(command_prefix=botPrefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Hello! I am {bot.user}')

@bot.command()
async def random(ctx, min_val=1, max_val=None):
    if max_val is None:
        max_val = min_val
        min_val = 1

    try:
        min_val = int(min_val)
        max_val = int(max_val)
        random_number = random.randint(min_val, max_val)
        await ctx.send(f"Рандомное число от {min_val} до {max_val}: {random_number}")
    except ValueError:
        await ctx.send("Неверный ввод. Пожалуйста введите еще раз правильно")
        
bot.run('token')
