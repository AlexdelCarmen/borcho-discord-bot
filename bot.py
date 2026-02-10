import discord
import os
from discord import Embed
import time
import json

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
STATS_FILE = "stats.json"
COOLDOWN = 10 #segundos
VERSION = "0.3.0"


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

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event 
async def on_ready(): 
    print(f'Conectado como {client.user}')
    

data = load_stats()

@client.event 
async def on_message(message): 

    if message.author.bot:
        return
    
    if message.content == "!ping": 
        user_id = message.author.id
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
        channel = client.get_channel(CHANNEL_ID)
        if channel: 
            await channel.send("Hola desde BorchoBot 😎")
            stats = data["stats"]
            msg = (
                f"📊 BorchoBot Stats\n"
                f"Pings: {stats['pings']}\n"
                f"Videos: {stats['videos']}\n"
                f"Bans: {stats['bans']}\n"
                f"Streams: {stats['streams']}"
            )
            await channel.send(msg)
            
    if message.content == "!help":
        channel = client.get_channel(CHANNEL_ID)
        if channel: 
            embed = Embed(
                title=f"🤖 BorchoBot v{VERSION}",
                description="Menu de ayuda",
                color=0x00ffcc
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
client.run(TOKEN)