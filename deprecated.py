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
'''
### ------------------------------------ ###
### DEPRECATED COMMANDS / FUNC FROM TESTING ###
''' 
    This probably isn't actually useful and may in fact be worse implemented than not.
    if message.content == "!users":
        response = f"Full list of users: {[member.name.replace("_", "\\_") for member in guild.members]}"
        await message.channel.send(response)
        print("User list printed.")

    if message.content == "!join":
        response = f'Welcome <@{message.author.id}>! Please send your username in chat so an admin can whitelist you!'
        await message.channel.send(response)
        print("Join message simulated.")

    if message.content == "!genchat":
        generalChat = client.get_channel(1418371057668325497)
        response = f"Type of `generalChat` variable is {type(generalChat)}. \n Literal: {generalChat}."
        await message.channel.send(response)
        print("General chat identification message sent.")

    ### TESTING ROLE APPLICATION ###
    if message.content == "!roleme":
        wizecraftGuild = client.get_guild(1418350872164958241)
        # Newcomer
        newcomerRole = wizecraftGuild.get_role(1418363343378579476)
        # Administrator
        adminRole = wizecraftGuild.get_role(1418363458533064775)

        if adminRole in message.author.roles:
            await message.author.add_roles(newcomerRole)
            response = f"Added role {newcomerRole.name} role to {message.author.name}."
        else:
            response = "User has insufficient permissions to use `roleme`."
        await message.channel.send(response)
        print("Roleme message sent")
    '''
### --------------------------------------- ###
