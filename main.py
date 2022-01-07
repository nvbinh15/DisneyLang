import discord
from log import log
import os
from keep_alive import keep_alive
from discord.ext import commands

from cogs.triviaquiz import Quiz
from cogs.filter import Filter
from cogs.wordnet import Professor

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} {bot.user.id}")

bot.add_cog(Filter(bot))
bot.add_cog(Professor(bot))
bot.add_cog(Quiz(bot))

keep_alive()
log()    
bot.run(os.environ['TOKEN'])
