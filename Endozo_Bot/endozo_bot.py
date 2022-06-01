import discord
from discord.ext import commands
import json
import random
import os

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

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])