import discord
from discord.ext import commands
#By Tomás Ryan
#tomasryanmann@gmail.com
##########
#tammi bot code
#last edited 5/1/2018
##########
#basically a warm up to get back into coding as im rusty as fuck
##########
bot = commands.Bot(command_prefix='yotam ', description='sure no bother')

@bot.event
async def on_ready():
    print('this is')
    print(bot.user.name)
#Bot command list
@bot.command()
async def hello():
    await bot.say('h0i! im TamMiB0t! c:')
@bot.command()  
async def joke():
    await bot.say('make me')
@bot.command()    
async def endWorld():
    await bot.say("couldn't be arsed tbh")
@bot.command()    
async def say(*, something):
    await bot.say(something)
    
bot.run('MzA1MTc3MzExMzY2MzQ4ODEx.DTEsCg.XQL8D5MESGion9OtogvuW8dsyT8')

#https://discordapp.com/api/oauth2/authorize?client_id=305177311366348811&scope=bot&permissions=0
