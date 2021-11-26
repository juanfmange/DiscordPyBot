import discord
from discord.ext import commands
import music

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

cogs = [music]

client = commands.Bot(command_prefix='-', intents = intents )



for i in range(len(cogs)):
    cogs[i].setup(client)


client.run('')
