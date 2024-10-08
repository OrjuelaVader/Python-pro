# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='%', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def userinfo(ctx: commands.Context, user: discord.User):
    # In the command signature above, you can see that the `user`
    # parameter is typehinted to `discord.User`. This means that
    # during command invocation we will attempt to convert
    # the value passed as `user` to a `discord.User` instance.
    # The documentation notes what can be converted, in the case of `discord.User`
    # you pass an ID, mention or username (discrim optional)
    # E.g. 80088516616269824, @Danny or Danny#0007

    # NOTE: typehinting acts as a converter within the `commands` framework only.
    # In standard Python, it is use for documentation and IDE assistance purposes.

    # If the conversion is successful, we will have a `discord.User` instance
    # and can do the following:
    user_id = user.id
    username = user.name
    avatar = user.display_avatar.url
    await ctx.send(f'User found: {user_id} -- {username}\n{avatar}')


bot.run('MTI5MjE2ODIyOTk3NjAxNDg3OA.GnbsM0.hryW72paLKYcvakGZZUOO3ZBnXERRdf_XwO-m8')