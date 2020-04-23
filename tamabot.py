'''Main file to run bot program'''
import discord
import os
from dotenv import load_dotenv
from discord.ext.commands import Bot
import arcade_racer as ar

load_dotenv()
token = os.getenv("BOT_TOKEN")
client = Bot(command_prefix="!")

@client.command(name = "mtcourse", description = "Generate a random Maximum Tune 5 course")
async def mtcourse():
    course = ar.wangan_course()
    await client.say("The course you should play is: \n" + course)

@client.command(name = "id8course", description = "Generate a random Initial D 8 course")
async def id8course():
    course = ar.id8_course()
    await client.say("The course you should play is: \n" + course)

@client.command(name = "bestcar", description = "Purely subjective")
async def bestcar():
    await client.say(ar.best_car())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)
