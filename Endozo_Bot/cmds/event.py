import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} join!')
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f"{member} 從天而降!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} remove!')
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f"{member} 掉頭不回!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('apple'):
            await msg.channel.send('iPhone')

def setup(bot):
    bot.add_cog(Event(bot))