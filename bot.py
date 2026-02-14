import discord
import os
from discord import Embed
import time
import json
from discord.ext import commands
import asyncio


from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
STATS_FILE = "stats.json"
COOLDOWN = 10 #segundos
VERSION = "0.4.0"
DEFAULT_STATS = {
    "pings": 0,
    "commands": 0,
    "bans": 0,
    "videos": 0,
    "last_used": 0
                 }

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

async def main():
    async with bot: 
        await bot.load_extension("cogs.ping")
        await bot.start(TOKEN)

asyncio.run(main())
    

bot.run(TOKEN)

'''
    def ensure_user(stats, user_id): 
        if user_id not in stats: 
            stats[user_id] = DEFAULT_STATS.copy()

    def load_stats (): 
        try: 
            with open(STATS_FILE, "r") as f: 
                return json.load(f)
        except FileNotFoundError: 
            return {
                "stats" : {
                    "pings" : 0, 
                    "videos" : 0,
                    "bans" : 0, 
                    "streams" : 0
                }
            }

    def save_stats(data): 
        with open(STATS_FILE, "w") as f: 
            json.dump(data, f, indent=4)

    last_used = {
        
    }



    client = discord.Client(intents=intents)

    @client.event 
    async def on_ready(): 
        print(f'Conectado como {client.user}')
        

    data = load_stats()

    @client.event 
    async def on_message(message): 

        if message.author.bot:
            return
        
        user_name = message.author.display_name
        
        if message.content == "!ping": 
            user_id = str(message.author.id)
            
            ensure_user(data, user_id)
            
            if user_id not in data: 
                data[user_id] = DEFAULT_STATS.copy()
                save_stats(data)
            
            data[user_id]["commands"] += 1
            data[user_id]["pings"] += 1
            data[user_id]["last_used"] += time.time()
            data["stats"]["pings"] += 1
            save_stats(data)
            
            
            channel = client.get_channel(CHANNEL_ID)
            start = time.time()
            if channel: 
                await channel.send("Hola desde BorchoBot 😎")

            if user_id in last_used: 
                elapsed = start - last_used[user_id]

                if elapsed < COOLDOWN: 
                    wait = int(COOLDOWN - elapsed)
                    await channel.send(
                        f"⏳ Espera {wait}s antes de usar !ping otra vez."
                    )
                    return

            embed = Embed(
                title="🤖 BorchoBot",
                description="Sistema activo",
                color=0x00ffcc
            )
            
            latency = round(client.latency * 1000)
            
            embed.add_field(
                name="🏓Pong",
                value=f"Latencia: {latency} ms",
                inline=False
            )
            last_used[user_id] = start
            await channel.send(embed=embed)
        
        if message.content == "!stats": 
            user_id = str(message.author.id)
            
            ensure_user(data, user_id)
            
            if user_id not in data: 
                data[user_id] = DEFAULT_STATS.copy()
                save_stats(data)
            
            save_stats(data)
            
            
            channel = client.get_channel(CHANNEL_ID)
            if channel: 

                embed = Embed(
                    title=f"📊 Tus estadísticas",
                    description=f"Datos de uso de BorchoBot para {user_name}",
                    color=0x00ffaa
                )
                
                embed.add_field(
                    name="Pings",
                    value=f"{data[user_id]["pings"]} veces",
                    inline=False
                )
                
                embed.add_field(
                    name="Comandos",
                    value=f"{data[user_id]["commands"]} veces",
                    inline=False
                )
                
                await channel.send(embed=embed)
                
        if message.content == "!help":
            
            user_id = str(message.author.id)
            
            ensure_user(data, user_id)
            
            if user_id not in data: 
                data[user_id] = DEFAULT_STATS.copy()
                save_stats(data)
            
            data[user_id]["commands"] += 1
            data[user_id]["last_used"] += time.time()
            data["stats"]["commands"] += 1
            save_stats(data)        
            
            
            channel = client.get_channel(CHANNEL_ID)
            if channel: 
                embed = Embed(
                    title=f"🤖 BorchoBot v{VERSION}",
                    description="Menu de ayuda",
                    color=0x00faca
                )
                
                embed.add_field(
                    name="!ping",
                    value="Testea la latencia del bot",
                    inline=False
                )
                embed.add_field(
                    name="!stats",
                    value="Muestra las estadisticas de uso",
                    inline=False
                )
                embed.add_field(
                    name="!help",
                    value="Menu de ayuda",
                    inline=False
                )
                await channel.send(embed=embed)
                
        for user in data: 
            for key in DEFAULT_STATS: 
                if key not in data[user]: 
                    data[user][key] = DEFAULT_STATS[key]
    client.run(TOKEN)
'''