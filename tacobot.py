# Tacobot by Mbtj

import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Ready when you are")
    print (bot.user.name)
    print (bot.user.id)


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

bot.run("Mzk2NzA3OTYwOTI5MjU1NDI2.DSrC5w.57nAKnI2x5Ve44qYFqraodXDRQA")