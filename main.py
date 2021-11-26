
import discord
import datetime
from discord.ext import commands
from discord.colour import Color
import music

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

cogs = [music]

client = commands.Bot(command_prefix='!', intents=intents)

# comando Ping
@client.command()
async def ping(ctx):
    await ctx.send('pong')

# comnado Info
@client.command()
async def info(ctx):  # informacion del servidor
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Hola bandamax",
                          timestamp=datetime.datetime.utcnow(), Color=discord.Colour.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # icono del servidor con url
    embed.set_thumbnail(url='https://pbs.twimg.com/media/C_Ull_NV0AAMSZw.jpg')
    await ctx.send(embed=embed)


# Aviso de activado
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)  # nombre del server
#   print(bot.user.id)          #id del bot
    print('Running...')

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTEzMjczOTMzMjA4MzU5MDEy.YZ8GoQ.a4SDUaTOGmxPJM-LP4xdpf6XYWw")
