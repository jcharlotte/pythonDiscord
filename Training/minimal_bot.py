import discord                          # Import the library

client = discord.Client()               # Create an instance of a client

@client.event 
async def on_ready():                   # This will be triggered once the bot has settled and is ready
    print('We have logged in as {0.user}'.format(client))

@client.event                   
async def on_message(message):          # This will be triggered every time the bot recieves a message
    if message.author == client.user:   # Make sure to ignore message from yourself
        return

    if message.content.startswith('$hello'):        # If message recieved starst with $hello, then :
        await message.channel.send('Hello!')

client.run('ODUyODU3ODIwMTQ3MzUxNTYy.YMM7vQ.ty8pGZkteAeeWvAy9_umuoJ9_LA')                       # Calls for the bot token, check https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro
