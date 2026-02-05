import discord
import os
from discord import Embed
import time

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event 
async def on_ready(): 
    print(f'Conectado como {client.user}')
    
    
@client.event 
async def on_message(message): 
    

    if message.author.bot:
        return
    
    if message.content == "!ping": 
        channel = client.get_channel(CHANNEL_ID)
        if channel: 
            await channel.send("Hola desde BorchoBot 😎")
        start = time.time()
        
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
        
        await channel.send(embed=embed)
        
client.run(TOKEN)