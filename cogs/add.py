from discord.ext import commands
import discord

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def add(self, ctx, left: int, right: int):
        return await ctx.send(left + right)
