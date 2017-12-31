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
    print(bot.user.name)
    print(bot.user.id)


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!!")
    print("user {} has pinged".format(ctx.message.author))


# @bot.command(pass_context=True)
# async def info(ctx, user: discord.Member):
#
#     if user is None:
#         user = ctx.message.author
#
#     await bot.say("The users name is: {}".format(user.name))
#     await bot.say("The users ID is: {}".format(user.id))
#     await bot.say("The users status is: {}".format(user.status))
#     await bot.say("The users highest role is: {}".format(user.top_role))
#     await bot.say("The user joined at: {}".format(user.joined_at))
#
#
#

# @bot.on_message
# async def urcute(self, message : discord.Message):
#     if message


@bot.command(pass_context=True)
async def channel(ctx):
    await bot.say("We are in {}".format(ctx.message.channel.name))
    print("Channel name")



bot.run(TOKEN)
