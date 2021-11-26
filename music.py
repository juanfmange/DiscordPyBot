
import discord
from discord.ext import commands
import youtube_dl
import re
from urllib import parse, request


class music (commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("No estas en un canal de voz!!!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    # @commands.command()
    # async def play(self, ctx, url):
    #     ctx.voice_client.stop()
    #     FFMPEG_OPTIONS = {
    #         'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    #     YDL_OPTIONS = {'format': "bestaudio"}
    #     vc = ctx.voice_client

    #     with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
    #         info = ydl.extract_info(url, download=False)
    #         url2 = info['formats'][0]['url']
    #         source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
    #         vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Pause")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resume")

    @commands.command()
    async def youtube(self, ctx, *search):  # Toma todas las  palabras despues del comando
        user_input = " ".join(search[:]).lower() # Junta las palabras en un solo string
        query_string = parse.urlencode({'search_query': user_input})
        html_content = request.urlopen('https://www.youtube.com/results?' + query_string)
        search_results = re.findall(r"/watch\?v=(.{11})", html_content.read().decode())

        # await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
        url = str('http://www.youtube.com/watch?v=' + search_results[0])
        print(user_input)
        print(query_string)
        print(search_results)
        print(url)
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
        

def setup(client):
    client.add_cog(music(client))
