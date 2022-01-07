import discord
from log import log
import os
from discord.ext import commands

from voice import Voice
from add import Add

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} {bot.user.id}")

bot.add_cog(Add(bot))
bot.add_cog(Voice(bot))

log()    
bot.run(os.environ['TOKEN'])
