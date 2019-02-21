import discord
import asyncio
import requests


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content.startswith('!food'):
            await message.channel.send("Getting food")
            msg = message.content.split(" ")
            if(len(msg) < 3):
                await message.channel.send("not enough arguments")
            else:
                data = requests.get("https://rumobile.rutgers.edu/1/rutgers-dining.txt")
                location = msg[1]
                meal = msg[2]
                data_json = data.json()
                for i in data_json:
                    if location.lower() in i['location_name'].lower():
                        for j in i['meals']:
                            if meal.lower() in  j['meal_name'].lower():
                                for k in j['genres']:
                                    for s in k['items']:
                                        await message.channel.send(s)

                




client = MyClient()
client.run('token')
