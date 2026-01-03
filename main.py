import os
import discord
from discord.ext import tasks
import random as r
from dotenv import load_dotenv
from mcstatus import JavaServer
import time

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

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    update_status.start()

@client.event
async def on_message(message):
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    if message.author == client.user:
        return

    if message.content == "!admin":
        response = "Paging <@123172448706232321>!"
        await message.channel.send(response)
        print("Admin bodrew paged.")
    
    if message.content == "!pic":
        response = f"{message.author.name}\'s Profile Pic: {message.author.display_avatar}"
        await message.channel.send(response)
        print("User picture attached to chat.")

    if message.content == "!map":
        response = "[WizeCraft Map](http://map.wize-craft.com)"
        await message.channel.send(response)
        print("Map link posted.")
    
    if message.content == "!wiki":
        response = "[WizeCraft Wiki](https://wize-craft.com)"
        await message.channel.send(response)
        print("Wiki link posted.")
    
    if message.content == "!rules":
        response = "[WizeCraft Rules](https://discordapp.com/channels/1418350872164958241/1418363014490619905)"
        await message.channel.send(response)
        print("Rules message link posted.")

    if message.content == "!fetch":
        await update_status()

@client.event
async def on_member_join(member):
    wizecraftGuild = client.get_guild(1418350872164958241)
    newcomerRole = wizecraftGuild.get_role(1418363343378579476)
    generalChat = client.get_channel(1418371057668325497)

    response = f'Welcome <@{member.id}>! Please send your username in chat so an admin can whitelist you!'
    await generalChat.send(response)
    await member.add_roles(newcomerRole)
    print("Join message posted to joiner.")

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
        print("The number of players online has not changed. Not updating channel status.")

client.run(TOKEN)