import discord
from discord.ext import commands

class Ping(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx): 
        embed = discord.Embed(
            title="🏓 Pong!",
            description="BorchoBot te saluda",
            color=0xBFD7EA
        )
        latency = round(self.bot.latency * 1000)
        embed.add_field(name="Latencia", value=f"{latency}ms", inline=False)
        await ctx.send(embed=embed)

async def setup(bot): 
    await bot.add_cog(Ping(bot))
    