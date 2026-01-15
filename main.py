import os
import discord
from discord.ext import tasks
import random as r
from dotenv import load_dotenv
from mcstatus import JavaServer
import time

def print_time():
    t = time.localtime()
    t_array = [t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec]
    st_array = []

    for i in t_array:
        if len(str(i)) == 1:
            i = "0" + str(i)
        else:
            i = str(i)
        st_array.append(i)
        
    response = "[" + st_array[0] + "-" + st_array[1] + "-" + st_array[2] + " " + st_array[3] + ":" + st_array[4] + ":" + st_array[5] + "]"
    return response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    # Show login message
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    # Start recurring tasks 
    update_status.start()

@client.event
# On message events
async def on_message(message):
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    if message.author == client.user:
        return

    if message.content == "!admin":
        response = "Paging <@123172448706232321>!"
        await message.channel.send(response)
        print(print_time() + "\n" + "Admin bodrew paged.")
    
    if message.content == "!pic":
        response = f"{message.author.name}\'s [Profile Pic]({message.author.display_avatar})"
        await message.channel.send(response)
        print(print_time() + "\n" + "User picture attached to chat.")

    if message.content == "!map":
        response = "WizeCraft Map: http://map.wize-craft.com"
        await message.channel.send(response)
        print(print_time() + "\n" + "Map link posted.")
    
    if message.content == "!wiki":
        response = "WizeCraft Wiki: https://wize-craft.com"
        await message.channel.send(response)
        print(print_time() + "\n" + "Wiki link posted.")
    
    if message.content == "!rules":
        response = "WizeCraft Rules: https://discordapp.com/channels/1418350872164958241/1418363014490619905"
        await message.channel.send(response)
        print(print_time() + "\n" + "Rules message link posted.")

    if message.author.name == "Bodrew" & "minecraft server" in message.content & "Day" in message.content:
        if "coffee" in message.content:
            await message.add_reaction(discord.emoji(1))
            print(print_time() + "\n" + "Coffee reaction applied to saltedcoffwee's message")
        if "tea" in message.content:
            await message.add_reaction(discord.emoji(2))
            print(print_time() + "\n" + "Tea reaction applied to saltedcoffwee's message")

@client.event
async def on_member_join(member):
    wizecraftGuild = client.get_guild(1418350872164958241)
    newcomerRole = wizecraftGuild.get_role(1418363343378579476)
    generalChat = client.get_channel(1418371057668325497)

    response = f'Welcome <@{member.id}>! Please send your username in chat so an admin can whitelist you!'
    await generalChat.send(response)
    await member.add_roles(newcomerRole)
    print(print_time() + "\n" + "Join message posted to joiner.")

@tasks.loop(minutes=2.0)
async def update_status():
    server = JavaServer.lookup("play.wize-craft.com")
    status = server.status()
    players_online = status.players.online
    emoji = "🟢" if int(players_online) >= 1 else "🔴"

    channel_name = f"{emoji} {players_online} online"

    statusChannel = client.get_channel(1456727821815906454)
    displayedPlyrsOnline = statusChannel.name.rsplit(" ")[1]

    if int(displayedPlyrsOnline) != players_online:
        await statusChannel.edit(name=channel_name)
    else:
        print(print_time() + "\n" + "The number of players online has not changed. Not updating channel status.")

client.run(TOKEN)
