import discord
from discord.ext import commands
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f"{member} 從天而降!")

@bot.event
async def on_member_remove(member):
    print(f'{member} remove!')
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f"{member} 掉頭不回!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")

@bot.command()
async def pic(ctx):
    random_pic = random.choice(jdata['pic'])
    picture = discord.File(random_pic)
    await ctx.send(file = picture)

@bot.command()
async def yes(ctx):
    await ctx.send("yeah baby!")

bot.run(jdata['TOKEN'])