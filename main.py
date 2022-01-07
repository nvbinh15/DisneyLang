import discord
from log import log
import os
import random
import asyncio
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$task'):
            await message.channel.send('Answer True or False to turn off annoying sound:')
            response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
            jprint(response.json())
            result = response.json()['results']
            print(result)
            question = result[0]['question']
            question = question.replace("&quot;", "'")
            answer = result[0]['correct_answer']
            print(question)
            await message.channel.send(question)

            def is_correct(m):
                return m.author == message.author

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=10.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if guess.content.lower() == answer.lower():
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))

client = MyClient()


log()    
client.run(os.environ['TOKEN'])