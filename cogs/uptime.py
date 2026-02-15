import discord
import time
from discord.ext import commands

print ("Uptime cog cargado")

class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def uptime(self, ctx): 
        now = time.time()
        uptime_seconds = int(now - self.bot.start_time)
        
        hours, remainder = divmod(uptime_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        await ctx.send(f"Uptime {hours}h {minutes}m {seconds}s")


async def setup(bot): 
    await bot.add_cog(Uptime(bot))