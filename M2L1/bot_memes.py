import discord
from discord.ext import commands
import random, os


description = '''Hola'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='---', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def meme1(ctx):
    img_name = random.choice(os.listdir('./M2L1/image'))
    with open(f'./M2L1/image/{img_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def gif(ctx):
    img_name = "https://media.tenor.com/vgQ373N5YtsAAAAM/speed-ishowspeed.gif"
    #with open(f'{img_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        #picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(img_name)    

bot.run("MTI5NDY5NzIxOTIxNTE5NjE2MA.G7RXeG.aGFIa5XYtBCTK7N8u-9HY3KcSANL3aoKvdAdTo")