import discord
from discord.ext import commands
from decouple import config

from trello import list_boards


TOKEN = config('TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/',intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name='bug_front', help="Adiciona bug ao board com nome igual ao do canal")
async def bug_front(ctx, task, descricao, responsavel):

    print(list_boards())
    print(task, descricao, responsavel)
    
    response = 'task adicionada'

    await ctx.send(response)

bot.run(TOKEN)