import random
import discord
import os
from discord.ext import commands
from functools import wraps
import sys

sys.path.append('B:\Programming Stuff\Python\Coding_Projects\Other Projects')
import Overwatch_Tracker # type: ignore
import sqlite3
overwatch = Overwatch_Tracker
conn = sqlite3.connect('B:\Programming Stuff\Python\Coding_Projects\Discord Bot\Overwatch_Tracker.db')
c = conn.cursor()

def owner():
    def predicate(ctx):
        return ctx.message.author.id == 289689571778756609
    return commands.check(predicate)


class Discord_Overwatch_Tracker(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Overwatch Player Creation
    @commands.command()
    @owner()
    async def create_overwatch_player(self, ctx, player_name, Tank_Rank, Tank_Win, Tank_Loss, DPS_Rank, DPS_Win, DPS_Loss, Support_Rank, Support_Win, Support_Loss):
        '''Creates Overwatch player profile. Requires name, tank rank, tank win, tank loss, DPS rank, DPS win, DPS loss, support rank, support win and support loss'''
        overwatch.add_player(player_name, Tank_Rank, Tank_Win, Tank_Loss, DPS_Rank, DPS_Win, DPS_Loss, Support_Rank, Support_Win, Support_Loss)
        await ctx.send(f'{player_name} has been added to the overwatch database')


    #Overwatch Player Deletion
    @commands.command()
    @owner()
    async def delete_overwatch_player(self, ctx, player_name):
        '''Deletes Overwatch player profile'''
        overwatch.delete_player(player_name)
        await ctx.send(f'{player_name} has been deleted from Overwatch Rank Tracker')

    @delete_overwatch_player.error
    async def delete_overwatch_player_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')


    #Overwatch Profile View
    @commands.command()
    async def overwatch_check(self, ctx, player_name):
        '''View Overwatch player profile'''
        with conn:
            c.execute('SELECT * FROM Overwatch_Rank_tracker WHERE Name = :Name',{'Name':player_name})
        result = c.fetchone()
        await ctx.send(result)

    @overwatch_check.error
    async def overwatch_check_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')


    #Overwatch Update Tank Rank
    @commands.command()
    async def update_tank_rank(self, ctx, player_name, Tank_Rank):
        '''Updates tank rank for Overwatch player. Requires player name and tank rank. Use \' \' for multiple words'''
        overwatch.update_Tank_Rank(player_name, Tank_Rank)
        await ctx.send(f'Tank rank is updated for {player_name} to {Tank_Rank}')
    
    @update_tank_rank.error
    async def update_tank_rank_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You forgot to update the rank to something')


    #Overwatch Add Tank Win
    @commands.command()
    async def add_tank_win(self, ctx, player_name):
        '''Adds one tank win to the counter'''
        overwatch.add_Tank_Win(player_name)
        await ctx.send(f'Tank win has been added to {player_name}')

    @add_tank_win.error
    async def add_tank_win_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')


    #Overwatch Add Tank Loss
    @commands.command()
    async def add_tank_loss(self, ctx, player_name):
        '''Adds one tank loss to the counter'''
        overwatch.add_Tank_Loss(player_name)
        await ctx.send(f'Tank loss has been added to {player_name}')

    @add_tank_loss.error
    async def add_tank_loss_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')


    #Overwatch Update DPS Rank
    @commands.command()
    async def update_dps_rank(self, ctx, player_name, DPS_Rank):
        '''Updates DPS rank for Overwatch player. Requires player name and DPS rank. Use \' \' for multiple words'''
        overwatch.update_DPS_Rank(player_name, DPS_Rank)
        await ctx.send(f'DPS rank is updated for {player_name} to {DPS_Rank}')

    @update_dps_rank.error
    async def update_dps_rank_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You forgot to update the rank to something')


    #Overwatch Add DPS Win
    @commands.command()
    async def add_dps_win(self, ctx, player_name):
        '''Adds one DPS win to the counter'''
        overwatch.add_DPS_Win(player_name)
        await ctx.send(f'DPS Win has been added to {player_name}')

    @add_dps_win.error
    async def add_dps_win_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')


    #Overwatch Add DPS Loss
    @commands.command()
    async def add_dps_loss(self, ctx, player_name):
        '''Adds one DPS loss to the counter'''
        overwatch.add_DPS_Loss(player_name)
        await ctx.send(f'DPS loss has been added to {player_name}')

    @overwatch_check.error
    async def overwatch_check_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')


    #Overwatch Update Support Rank
    @commands.command()
    async def update_support_rank(self, ctx, player_name, Support_Rank):
        '''Updates support rank for Overwatch player. Requires player name and support rank. Use \' \' for multiple words'''
        overwatch.update_Support_Rank(player_name, Support_Rank)
        await ctx.send(f'Support rank is updated for {player_name} to {Support_Rank}')
            
    @update_support_rank.error
    async def update_support_rank_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You forgot to update the rank to something')


    #Overwatch Add Support Win
    @commands.command()
    async def add_support_win(self, ctx, player_name):
        '''Adds one support win to the counter'''
        overwatch.add_Support_Win(player_name)
        await ctx.send(f'Support Win has been added to {player_name}')

    @update_support_rank.error
    async def update_support_rank_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')


    #Overwatch Add Support Loss
    @commands.command()
    async def add_support_loss(self, ctx, player_name):
        '''Adds one support loss to the counter'''
        overwatch.add_Support_Loss(player_name)
        await ctx.send(f'Support loss has been added to {player_name}')

    @add_support_loss.error
    async def add_support_loss_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Player does not exist in database')
            

async def setup(bot):
    await bot.add_cog(Discord_Overwatch_Tracker(bot))