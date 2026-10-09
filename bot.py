import discord
from gen_password import gen_pass
from settings import *

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send('Ciao! Benvenuto nel bot lezione M1L3')
    elif message.content.startswith('$password'):
        await message.channel.send('Questa è la tua password generata: ' + gen_pass(20))
    elif message.content.startswith('$arrivederci'):
        await message.channel.send('\U0001f642')
    else:
        await message.channel.send('Comando non valido!!!')

client.run(settings["TOKEN"])