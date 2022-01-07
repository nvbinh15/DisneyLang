import discord
from log import log
import os
from keep_alive import keep_alive
from discord.ext import commands

from cogs.voice import Voice
from cogs.add import Add
from cogs.wordnet import Professor

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} {bot.user.id}")

bot.add_cog(Add(bot))
bot.add_cog(Voice(bot))
bot.add_cog(Professor(bot))

keep_alive()
log()    
bot.run(os.environ['TOKEN'])
