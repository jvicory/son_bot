# created by Short-round
# Work with Python 3.6
import discord, os

s3 = os.environ['TOKEN']


client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Hi'):
        msg = 'Fuck you, Dad! I do what I want!'
        await client.send_message(message.channel, msg)
    if message.content.startswith('!ice') or message.content.startswith('!Ice'):
        img = "https://imgur.com/OrJuwTH"
        await client.send_message(message.channel, img)       

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
