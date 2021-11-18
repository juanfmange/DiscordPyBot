import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='-', intents = discord.Intents.all())


for i in range(len(cogs)):
    cogs[i].setup(client)


client.run('OTEwNzMzNzA4NTE0OTg0MDQ2.YZXI3A.5Z8DR9NAhxNvj134J6HrIt4yu0o')
