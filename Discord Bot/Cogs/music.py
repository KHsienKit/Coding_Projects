import discord
from discord.ext import commands
from functools import wraps
from youtube_dl import YoutubeDL
import asyncio
import time

#YoutubeDL Options
ytdl_opts = {
    'format':'best audio/best',
    'noplaylist':'True'
}

ytdl = YoutubeDL(ytdl_opts)

#FFmpeg Options
ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}

music_queue = []
title_music_queue = []


class music(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    def search_yt(self, song):
        song_info = ytdl.extract_info('ytsearch:%s'%song, download = False)['entries'][0]
        return {'source': song_info['formats'][0]['url'], 'title': song_info['title']}

    def search_yt_url(self, url):
        url_info = ytdl.extract_info(url, download= False)
        return {'source': url_info['formats'][0]['url'], 'title': url_info['title']}

    #Music Play Function
    @commands.command()
    async def play(self, ctx, *args):
        '''Play music of your choice. Type in url or name'''
        song = ' '.join(args)
        if song[:8] != 'https://':
            source = self.search_yt(song)
            music_queue.append(source['source'])
            title_music_queue.append(source['title'])
        elif song[:8] == 'https://':
            source = self.search_yt_url(song)
            music_queue.append(source['source'])
            title_music_queue.append(source['title'])
        else:
            await ctx.send('Play what motherfucker')
        try:
            title = source['title']
            voice_channel = ctx.author.voice.channel
            await voice_channel.connect()
        except AttributeError:
            await ctx.send('You\'re not in a voice channel m8')
        except discord.ClientException:
            pass
        while ctx.voice_client.is_playing():
            pass
        else:
            ctx.voice_client.play(discord.FFmpegPCMAudio(music_queue[0],  **ffmpeg_options))
            await ctx.send(f"Now playing {source['title']}")
            music_queue.pop(0)
    

    
    #Music Queue Function
    # @commands.command()
    # async def queue(self, ctx):
    #     for title in title_music_queue:
    #         titles = ' \n'.join(title)
    #     await ctx.send(titles)
    

    #Music Pause Function
    @commands.command()
    async def pause(self, ctx):
        '''Pauses Music'''
        if ctx.voice_client.is_playing():
            ctx.voice_client.pause()
        else:
            await ctx.send('Nigga I ain\'t playing anything right now')
    
    @pause.error
    async def pause_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Nigga I ain\'t in any voice channels')


    #Music Resume Function
    @commands.command()
    async def resume(self, ctx):
        '''Resumes Music'''
        if ctx.voice_client.is_paused():
            ctx.voice_client.resume()
        else:
            await ctx.send('Wtf do you want me to pause. Nothing is playing rn')
    
    @resume.error
    async def resume_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Nigga I ain\'t in any voice channels')


    #Skip Function

    # def skip(self, ctx):

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
            ctx.voice_client.stop()
            self.skip(ctx)
        else:
            ctx.send('Skip what nigga')
    

    #Music Stop Function
    @commands.command()
    async def stop(self, ctx):
        '''Stop music and bot leaves'''
        try:
            await ctx.voice_client.disconnect()
        except AttributeError:
            await ctx.send('I\'m not in any voice channel m8')

    
    

async def setup(bot):
    await bot.add_cog(music(bot))