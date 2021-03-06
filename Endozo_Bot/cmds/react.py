import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def pic(self, ctx):
        random_pic = random.choice(jdata['pic'])
        picture = discord.File(random_pic)
        await ctx.send(file = picture)

    @commands.command()
    async def yes(self, ctx):
        await ctx.send("yeah baby!")

    @commands.command()
    async def birthday(self, ctx):
        await ctx.send("Happy birthday!")

def setup(bot):
    bot.add_cog(React(bot))