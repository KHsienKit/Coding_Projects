import random
import discord
import os
from discord.ext import commands
from functools import wraps
import sys
                 

#Discord Bot Settings
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!',intents = intents)

def owner():
    def predicate(ctx):
        return ctx.message.author.id == 289689571778756609
    return commands.check(predicate)

#Discord Cog Settings
@bot.event
async def on_ready():
    for file in os.listdir('B:\Programming Stuff\Python\Coding_Projects\Discord Bot\Cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'Cogs.{file[:-3]}')
    

@bot.command()
@owner()
async def reload(ctx, cog):
    '''Reloads Cog'''
    await bot.unload_extension(f'Cogs.{cog}')
    await bot.load_extension(f'Cogs.{cog}')
    await ctx.send(f'{cog} cog reloaded')


# #Exception Handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Something went wrong, try again')
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Only Lugia0000 can use this command.¯\_(ツ)_/¯')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You\'re missing arguments')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('This command does not exist')



#Wow!
@bot.command()
async def wow(ctx):
    '''wow!'''
    await ctx.send('wow!')


#Bye bye
@bot.command()
@owner()
async def bye(ctx):
    '''HK Bot goes offline'''
    await ctx.send('Bye Bye!')
    await bot.close()

#Testing Stuff

#Start Bot
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
bot.run(os.getenv('DISCORD_TOKEN'))