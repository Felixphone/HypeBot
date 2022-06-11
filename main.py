import schedule
import time
import discord
import random
from discord.ext import commands, tasks
import webbrowser

client = commands.Bot(command_prefix = '.')

global hype_onoff
global activate

hype_onoff = 1
activate = 0
print("open")
def hype_trig():
    global hype_onoff
    global activate
    if hype_onoff == 1:
        print("Hype!")
    activate=activate+1
    current_time = time.strftime("%H:%M:%S")
    print("[" + current_time +"]    Hype activated     TrgID:" + str(activate) + "    TrgType:{Force Trigger}")
    
import json

@client.event
async def on_ready():
    print('Booting cogs...')
    await client.change_presence(status=discord.Status.online)
    print('bot ready')
    
@client.command()
async def hype_toggle(ctx):

    with open("data.json", "r") as f:
        data = json.load(f)
    trig_stat_fetch=(data["hype_onoff"])
    
    global hype_onoff
    if trig_stat_fetch == 1:
        with open("data.json") as f:
            data = json.load(f)
            data["hype_onoff"] = 0
            json.dump(data, open("data.json", "w"), indent = 4)
         

        print("Hype is off")
        await ctx.send("hype is off")


    elif trig_stat_fetch == 0:
        with open("data.json") as f:
            data = json.load(f)
            data["hype_onoff"] = 1
            json.dump(data, open("data.json", "w"), indent = 4)
            
        print("Hype is on!")
        await ctx.send("Hype is on!")




@client.command()
async def hype_toggle_query(ctx):
    with open("data.json", "r") as f:
        data = json.load(f)
    trig_stat_fetch=(data["hype_onoff"])
    
    global hype_onoff
    if trig_stat_fetch == 1:
        print("Hype is on!")
    elif trig_stat_fetch == 0:
        print("Hype is off")

@client.command()
async def rickroll_JT(ctx):
    await ctx.send("OK. RickRolling Julian...")

    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')

    
@client.command()
async def close_running_server(ctx):
    await ctx.send("<!Closing running server!>  port:0050   cache.dump / dumping   Exit code: -2 'Forced Close'")
    quit()

@client.command()
async def logout(ctc):
    await client.close()
    
client.run('OTM1OTUyODQ1ODIyMzgyMTUw.YfGIAw.qoEuamMo9MvzhM3eJzoEEt7v9Tk')
