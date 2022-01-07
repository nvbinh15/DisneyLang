from discord.ext import commands
import discord
import requests

class Insult(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def insult(self, ctx):
        response = requests.get("https://insult.mattbas.org/api/insult")
        # print(response.json)
        return await ctx.send(response.text, tts=True)