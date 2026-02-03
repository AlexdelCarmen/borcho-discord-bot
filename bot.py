import discord
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event 
async def on_ready(): 
    print(f'Conectado como {client.user}')
    
    
@client.event 
async def on_message(message): 
    if message.author == client.user: 
        return
    if message.content == "!ping": 
        await message.channel.send("Pong 🏓")
        
client.run(TOKEN)