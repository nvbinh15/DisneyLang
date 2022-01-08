import discord
from log import log
import os
from keep_alive import keep_alive
from discord.ext import commands
from wn_downloader import wn_download
from cogs.quizandgrammar import Quiz
from cogs.filter import Filter
from cogs.wordnet import Professor

wn_download()

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
