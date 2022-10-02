import discord
from discord.ext import commands
from decouple import config


TOKEN = config('TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name='bug_front')
async def add_task(ctx):
    
    response = 'task adicionada'

    await ctx.send(response)

bot.run(TOKEN)