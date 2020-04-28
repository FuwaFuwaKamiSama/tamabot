'''Main file to run bot program'''
import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import arcade_racer as ar
import anime_search as anis

load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix="!")

@bot.command(name = "mtcourse", description = "Generate a random Maximum Tune 5 course")
async def mtcourse(ctx):
    course = ar.wangan_course()
    await ctx.send("The course you should play is: \n" + course)

@bot.command(name = "id8course", description = "Generate a random Initial D 8 course")
async def id8course(ctx):
    course = ar.id8_course()
    await ctx.send("The course you should play is: \n" + course)

@bot.command(name = "bestcar", description = "Purely subjective")
async def bestcar(ctx):
    await ctx.send(ar.best_car())

@bot.command(name = "plushie", description = "Extra huggable")
async def plushie(ctx):
    picLink = anis.musashi_plush()
    await ctx.send(picLink)

@bot.command(pass_context = True, name = "tamamosearch", description = "Get a random picture of Tamamo no Mae")
async def tamamosearch(ctx):
    picLink = anis.tamamo_search()
    await ctx.send(file = discord.File(picLink))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(token)
