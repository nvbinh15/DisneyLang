import discord
from log import log
import os

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


log()    
client.run(os.environ['TOKEN'])