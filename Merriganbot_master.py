# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

TOKEN = 'NDM5NDk4OTc0NDg3OTA0MjU2.DcUs6w.KBOU--o7DtDHLnm87a5MqtRbwSw'

client = discord.Client()

@client.event
async def on_message(message):
    #we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    lowercase_suicidal_words = ['suicide', 'kill me', 'want to die', 'kill myself']
    if any([w in message.content.lower() for w in lowercase_suicidal_words]):
        msg = "Remember, you matter and that suicide is not a joke. People will miss you if you are gone."
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
