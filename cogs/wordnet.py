from discord.ext import commands
from nltk.corpus import wordnet
import re

# words = message.split()
# result = ''

# for word in words:

#     synset = wordnet.synsets(word)
#     if len(synset) == 0:
#         result += word + ' '
#     else:
#         result += synset[0].definition() + ' '
# print(result)

def parse_message(message):
    words = re.findall(r"[\w']+|[.,!?;]", message)
    result = ''

    for word in words:

        synset = wordnet.synsets(word)
        if len(synset) == 0:
            result += word + ' '
        else:
            result += synset[0].definition() + ' '
    return result

class Professor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        parsed = parse_message(message.content)
        if parsed == message.content:
            return
            
        await message.channel.send(parsed, reference=message)
    