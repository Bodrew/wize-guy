import os
import discord
import random as r
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents=discord.Intents.all()
client = discord.Client(intents=intents)

#generalChat
#generalChat = client.get_channel(1418371057668325497)
#dev-test chat
#generalChat = client.get_channel(1454568341061636316)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

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

    if message.content == "!users":
        response = f"Full list of users: {[member.name.replace("_", "\\_") for member in guild.members]}"
        await message.channel.send(response)
        print("User list printed.")

    if message.content == "!pic":
        response = f"{message.author.name}\'s Profile Pic: {message.author.display_avatar}"
        await message.channel.send(response)
        print("User picture attached to chat.")

    if message.content == "!join":
        response = f'Welcome <@{message.author.id}>! Please send your username in chat so an admin can whitelist you!'
        await message.channel.send(response)
        print("Join message simulated.")

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

    if message.content == "!genchat":
        generalChat = client.get_channel(1418371057668325497)
        response = f"Type of `generalChat` variable is {type(generalChat)}. \n Literal: {generalChat}."
        await message.channel.send(response)
        print("General chat identification message sent.")

@client.event
async def on_member_join(member):
    generalChat = client.get_channel(1418371057668325497)
    response = f'Welcome <@{member.id}>! Please send your username in chat so an admin can whitelist you!'
    await generalChat.send(response)
    print("Join message posted to joiner.")

### DEPRECATED COMMANDS FROM SPINACH-BOT ###
'''
legends = ["Ash","Bangalore","Bloodhound","Catalyst","Caustic","Crypto","Fuse","Gibraltar","Horizon","Lifeline","Loba","Mad Maggie","Mirage","Newcastle","Octane","Pathfinder","Rampart","Revenant","Seer","Valkyrie","Vantage","Wattson","Wraith"]
weapons = ["Havoc Rifle","VK-47 Flatline","R-301 Carbine","Nemesis Burst AR","Alternator SMG","Prowler Burst PDW","R-99 SMG","Volt SMG","C.A.R. SMG","Devotion LMG","L-STAR EMG","M600 Spitfire","Rampage LMG","G7 Scout","Triple Take","30-30 Repeater","Charge Rifle","Longbow DMR","Sentinel","EVA-8 Auto","Mastiff Shotgun","Mozambique Shotgun","Peacekeeper","P2020","Wingman"]

if message.content == "!treat":
    response = "MEOW, MEOW, MEOOOOOW\nhttps://www.twitch.tv/videos/1700951454"
    await message.channel.send(response)

### APEX LEGENDS COMMANDS ###
if message.content == "!legend":
    legend = r.choice(legends)
    response = f"Meow! You should play **{legend}** this round!"
    await message.channel.send(response)

if message.content == "!loadout":
    w1 = r.choice(weapons)
    weapons.remove(w1)
    w2 = r.choice(weapons)

    response = f"Meow! You should use the **{w1}** and the **{w2}** this round!"
    await message.channel.send(response)
    weapons.append(w1)
### --------------------- ###
'''
### ------------------------------------ ###

client.run(TOKEN)
