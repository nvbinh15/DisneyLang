import random
import asyncio
import requests
import json
import language_tool_python
from discord.ext import commands
import discord

async def grammarpolice(message):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.correct(message.content)
    reply_text = "Correct sentence should be: " + matches
    if matches != message.content:
        await message.channel.send(reply_text, reference=message)
        await message.add_reaction("🚩")
    else:
        print("correct already")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

class Quiz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def check(self, ctx, *, message):
        if message.author.bot:
            return
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.correct(message)
        reply_text = "Correct sentence should be: " + matches
        if matches != message:
            await ctx.send(reply_text)
        else:
            await ctx.send("Correct already!")


    @commands.command()
    async def quiz(self, ctx):
        await ctx.send('Answer True or False:')
        response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
        jprint(response.json())
        result = response.json()['results']
        print(result)
        question = result[0]['question']
        question = question.replace("&quot;", "'")
        question = question.replace("&#039;", "'")
        answer = result[0]['correct_answer']
        print(question)
        await ctx.send(question)

        try:
            guess = await self.bot.wait_for('message', timeout=20.0)
        except asyncio.TimeoutError:
            return await ctx.send('Sorry, you took too long it was {}.'.format(answer))

        if guess.content.lower() == answer.lower():
            await ctx.send('You are right!')
        else:
            await ctx.send('Oops. It is actually {}.'.format(answer))

