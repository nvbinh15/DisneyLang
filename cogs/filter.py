from discord.ext import commands
import discord
import requests

class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot == message.author:
            return
        filtered = self._profanity_filter(message.content)
        if filtered == message.content:
            return
        await message.delete()
        await message.channel.send(f'Hey you, watch your language')
        await message.channel.send(f'{message.author.mention} said: "{filtered}"')

    def _profanity_filter(self, msg):
        filtered = requests.get("https://www.purgomalum.com/service/json", params={"text": msg}).json()["result"]
        i = 0
        result = ""
        while i < len(msg):
            if (filtered[i] != "*" or (filtered[i] == "*" and msg[i] == "*")):
                result += filtered[i]
            else:
                result += "\*"
                # i+=1
                # while filtered[i] == "*":
                #   print(msg[i])
                #   result += "w"
                #   i+=1
            i += 1
        return result
