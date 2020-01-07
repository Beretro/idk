import discord
from discord.ext import commands
from discord.utils import get
import webbrowser
bot = commands.Bot("/")
client = discord.Client()
channel_address = 621039466752114730
bot_channel_address = 621051821821263883
pinned_channel_address = 633362598364184607
@client.event
async def on_ready():
    print("The bot is ready!")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hi" or message.content == "Hi max" or message.content == "Hi Max":
        channel = client.get_channel(channel_address)
        await channel.send("Hello")
    if "69" in message.content:
        channel = client.get_channel(channel_address)
        await channel.send("Nice")
    if "im" in message.content or "i'm" in message.content or "i am" in message.content or "Im" in message.content or "I'm" in message.content or "I am" in message.content:
        channel = client.get_channel(channel_address)
        await channel.send("And I am Max")
    ("""if message.content == "Uh oh" or message.content == "uh oh":
        channel = client.get_channel(channel_address)
        await webbrowser.open("https://www.google.com/search?q=uh+oh+stinky&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiP14mrotnmAhVgWhUIHd8yDoYQ_AUoAXoECAsQAw")
        await channel.send("Stinky")""")
    if message.content == "Max bot#9555" or message.content == "Max bot":
        channel = client.get_channel(channel_address)
        await channel.send("Hello?")
    if message.content == "No I'm Max" or message.content == "No Im Max":
        channel = client.get_channel(channel_address)
        await channel.send("Yeah me too")
    if message.content == "How u doing?" or message.content == "How are you doing?":
        channel = client.get_channel(channel_address)
        await channel.send("All good man")
    if message.content == "Ur gay" or message.content == "ur gay":
        channel = client.get_channel(channel_address)
        await channel.send(":(")
    if message.content == "Yeah me too" or message.content == "yeah me too" or message.content == "yea me too" or message.content == "Yea me too":
        channel = client.get_channel(channel_address)
        await channel.send("Yeah me too")
    else:
        channel1 = client.get_channel(pinned_channel_address)
        
        print (message.content)
        return (message.content)
        


@client.event
async def on_reaction_add(reaction, user):
        emoji = '\N{PUSHPIN}'
        if reaction.emoji == (emoji):
            channel = client.get_channel(pinned_channel_address)
            reaction_embed = discord.Embed()
            ("""reaction_embed.set_author()""")
            value1 = reaction.message.author
            reaction_embed.add_field(name = value1,value = reaction.message.content, inline = False)
            await channel.send(embed = reaction_embed)
            
            ("""reaction.message.author,reaction.message.content""")






client.run(token)
