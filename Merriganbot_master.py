# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

with open('/home/pi/Desktop/MerriganBot/TOKEN.txt', 'r') as tokenfile:
    TOKEN = tokenfile.readline()
    tokenfile.close()

client = discord.Client()

@client.event
async def on_message(message):
    #we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    lowercase_suicidal_words = ['suicide', 'kill me', 'want to die', 'kill myself']
    lowercase_homocidal_words = ['die', 'murder', 'assassinate']
    
    if any([w in message.content.lower() for w in lowercase_suicidal_words]):
        msg = "Remember, you are important and suicide is not a joke. People will miss you if you are gone."
        await client.send_message(message.channel, msg)

    if any([w in message.content.lower() for w in lowercase_homocidal_words]):
        msg = "Don't wish for someone to die!"
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = "Listening to your every complaint"))

client.run(TOKEN)
