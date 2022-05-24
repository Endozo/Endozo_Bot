import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(978648503674867712)
    await channel.send(f"{member} 從天而降!")

@bot.event
async def on_member_remove(member):
    print(f'{member} remove!')
    channel = bot.get_channel(978648525812428872)
    await channel.send(f"{member} 掉頭不回!")

@bot.command()
async def ping(ctx):

bot.run("OTc4NjE4MjgyMzMwNDM5Njkw.GtaXmA.K32HY2DdesHKkExEFMeCDFA5nRk65e_hp3Z_0o")