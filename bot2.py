import discord
from discord.ext import commands
from settings import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix = '$',
    intents = intents
)


@bot.event
async def on_ready():
    print(f'Bot online: {bot.user}')


@bot.command()
async def somma(ctx, numero1: int, numero2: int):
    risultato = numero1 + numero2

    await ctx.send(f"La somma è: {risultato}")


bot.run(settings["TOKEN"])