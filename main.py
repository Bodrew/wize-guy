import os
import discord
from discord.ext import tasks
import random as r
from dotenv import load_dotenv
from mcstatus import JavaServer
from typing import Union
import time
import logging
import aiohttp
from ampapi import (
    ActionResultError,
    AMPADSInstance,
    AMPControllerInstance,
    AMPInstance,
    AMPInstanceState,
    AMPMinecraftInstance,
    AnalyticsFilter,
    AnalyticsSummary,
    APIParams,
    Bridge,
    Players,
)

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

AMP_URL = os.getenv('AMP_URL')
AMP_USER = os.getenv('AMP_USER')
AMP_PW = os.getenv('AMP_PW')

_params = APIParams(url=AMP_URL, user=AMP_USER, password=AMP_PW)

@client.event
async def on_ready():
    # Discord Bot login
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

    # Create the whitelist application command.
'''
@discord.app_commands.Command(name="echo", description="Repeat your message back", callback="test")
async def echo(interaction: discord.Interaction, message: str) -> None:
    await interaction.response.send_message(message)
'''

# On message events
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
        print(print_time() + "\n" + "Admin bodrew paged.")
    
    if "!pic" in message.content:
        response = f"{message.author.name}\'s [Profile Pic]({message.author.display_avatar})"
        await message.channel.send(response)
        print(print_time() + "\n" + f"{message.author.name}\'s picture attached to chat.")

    if "!map" in message.content:
        response = "WizeCraft Map: https://map.wize-craft.com"
        await message.channel.send(response)
        print(print_time() + "\n" + "Map link posted.")
    
    if "!wiki" in message.content:
        response = "WizeCraft Wiki: https://wize-craft.com"
        await message.channel.send(response)
        print(print_time() + "\n" + "Wiki link posted.")
    
    if "!rules" in message.content:
        response = "WizeCraft Rules: https://discordapp.com/channels/1418350872164958241/1418363014490619905"
        await message.channel.send(response)
        print(print_time() + "\n" + "Rules message link posted.")

    if "minecraft server" in message.content.lower() and "day" in message.content.lower() and "suggesting" in message.content.lower():
        if "coffee" in message.content:
            emoji = "\u2615"
            await message.add_reaction(emoji)
            print(print_time() + "\n" + f"Coffee reaction applied to {message.author.name}'s message")
        elif "tea" in message.content:
            emoji = "\U0001F375"
            await message.add_reaction(emoji)
            print(print_time() + "\n" + f"Tea reaction applied to {message.author.name}'s message")
    
    if "!whitelist " in message.content:
        user = message.content.split(" ")[1]
        #whitelist(user)
    
    if "!bedrock" in message.content:
        response = "Bedrock players cannot be whitelisted in Java servers directly because their usernames do not exist in the Java \"database\". The workaround is to turn off the whitelist, have the bedrock player join, add them to the whitelist (because now the server knows their name), and then turn the whitelist back on. \n\nIf you're ready, join now so <@123172448706232321> can whitelist you. Otherwise, ping him later when ready!"
        await message.channel.send(response)
    
    if "!tps" in message.content:
        prompt = "spark tps"
        consoleChat = client.get_channel(1532383467181051914)
        await consoleChat.send(prompt)
        time.sleep(3)
        async for historyItem in consoleChat.history(limit=1):
            response = historyItem.content
            lines = response.split("\n")

            newLines = []
            for line in lines:
                if " ] " in line:
                    newLine = line.split(" ] ")[1]
                    newLines.append(newLine)
                else:
                    newLines.append(line)
            
            tpsMsg = ""
            for line in newLines:
                tpsMsg += line + "\n"
            await message.channel.send(tpsMsg)

@client.event
async def on_member_join(member):
    wizecraftGuild = client.get_guild(1418350872164958241)
    newcomerRole = wizecraftGuild.get_role(1418363343378579476)
    notWhitelistedRole = wizecraftGuild.get_role(1530689863555350779)
    generalChat = client.get_channel(1418371057668325497)

    await member.add_roles(newcomerRole)
    await member.add_roles(notWhitelistedRole)
    response = f'Welcome <@{member.id}>! Please send your username in chat so an admin can whitelist you!'
    await generalChat.send(response)
    print(print_time() + "\n" + f"Join message posted to {member.name}.")

@tasks.loop(minutes=2.0)
async def update_status():
    server = JavaServer.lookup("play.wize-craft.com")
    status = server.status()
    players_online = status.players.online
    emoji = "🟢" if int(players_online) >= 1 else "🟡"

    channel_name = f"{emoji} {players_online} online"

    statusChannel = client.get_channel(1456727821815906454)
    displayedPlyrsOnline = statusChannel.name.rsplit(" ")[1]

    if int(displayedPlyrsOnline) != players_online:
        await statusChannel.edit(name=channel_name)
    else:
        print(print_time() + "\n" + "The number of players online has not changed. Not updating channel status.")

client.run(TOKEN)
