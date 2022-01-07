import discord
from log import log
import os
from discord.ext import commands

from cogs.voice import Voice
from cogs.add import Add
from cogs.insult import Insult
from cogs.filter import Filter

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} {bot.user.id}")


bot.add_cog(Add(bot))
bot.add_cog(Voice(bot))
bot.add_cog(Insult(bot))
bot.add_cog(Filter(bot))

log()    
bot.run(os.environ['TOKEN'])
