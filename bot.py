# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

with open('TOKEN.txt', 'r') as tokenfile:
    TOKEN = tokenfile.readline()
    tokenfile.close()

client = discord.Client()

@client.event
async def on_message(message):
    #we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    lowercase_suicidal_words = ['suicide', 'kill me', 'want to die', 'kill myself', 'toaster bath', 'toaster in bath', 'toaster in the bath']
    lowercase_homocidal_words = ['die', 'kill you']
    lowercase_slurs = ['nigga', 'nigger', 'fag', 'retard']
    
    if any([w in message.content.lower() for w in lowercase_suicidal_words]):
        msg = "Remember, you are important and suicide is not a joke. People will miss you if you are gone."
        await client.send_message(message.channel, msg)

    if any([w in message.content.lower() for w in lowercase_homocidal_words]):
        msg = "Don't wish for someone to die!"
        await client.send_message(message.channel, msg)

    if any([w in message.content.lower() for w in lowercase_slurs]):
        msg = "That is not appropriate speech for this server. Let's change out mindset"
        await client.send_message(message.channel, msg)

    if message.content.upper ().startswith('E!CHANGESTATUS'):
        if message.author.id == "369267862050832385":
            args = message.content.split(" ")
            if len (args) == 1:
                msg = '''Status changed to "Listening to your every complaint"'''
                await client.change_presence(game=discord.Game(name= "Listening to your every complaint"))
                await client.send_message(message.channel, msg)
            else:
                msg = '''Status changed to '''  '%s' % (" ".join(args[1:]))
                await client.change_presence(game=discord.Game(name='%s' % (" ".join(args[1:]))))
                await client.send_message(message.channel, msg)
        else:
            msg = 'You do not have permission to use this command.'
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = "Listening to your every complaint"))

client.run(TOKEN)
