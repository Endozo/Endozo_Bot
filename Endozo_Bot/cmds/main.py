import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="About", url="https://pbs.twimg.com/media/FUFDb1MVUAEmPQy?format=jpg&name=4096x4096", description="About the bot", color=0x1adff9)
        embed.set_author(name="ミョワ", url="https://twitter.com/_MYOWA", icon_url="https://pbs.twimg.com/profile_images/1423135021171281920/2T7iqHGU_400x400.jpg")
        embed.set_thumbnail(url="https://pbs.twimg.com/media/FUFDb1MVUAEmPQy?format=jpg&name=4096x4096")
        embed.add_field(name="1", value="11", inline=False)
        embed.add_field(name="2", value="22", inline=True)
        embed.add_field(name="3", value="33", inline=True)
        embed.add_field(name="4", value="44", inline=True)
        embed.set_footer(text="15116165165")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))