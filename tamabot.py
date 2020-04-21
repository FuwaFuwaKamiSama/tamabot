'''Main file to run bot program'''

import discord
import os
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()
token = os.getenv("BOT_TOKEN")
client = Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)
