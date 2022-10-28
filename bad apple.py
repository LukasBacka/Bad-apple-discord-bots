import asyncio
import time

import discord
from discord.ext import commands

file = open(f"C:/Users/lukas/OneDrive/Plocha/frames/frames.txt", "r", encoding='utf8')
l = file.readlines()
file.close()
framecounter = 1
r = []
dict = {}
count = 0
for i in range(len(l)):
    try:
        int(l[i])
        pass
    except:
        r.append(l[i])
    if len(r) >= 37:
        dict[int(l[count])] = r
        r = []
        count += 38


def image(frame):
    global dict
    l1 = dict[int(frame)]
    em = ""
    for i in l1:
        em = em + i
    return "```" + em + "```"

client1 = commands.Bot(command_prefix = '!', intents= discord.Intents.default())
client2 = commands.Bot(command_prefix = 'owo', intents= discord.Intents.default())
client3 = commands.Bot(command_prefix = 'owo', intents= discord.Intents.default())
client4 = commands.Bot(command_prefix = 'owo', intents= discord.Intents.default())
client5 = commands.Bot(command_prefix = 'owo', intents= discord.Intents.default())

clients = []
clients.append(client1)
clients.append(client2)
clients.append(client3)
clients.append(client4)
clients.append(client5)

TOKENmain = "" #TOKENS of your bots
TOKEN2 = ""
TOKEN3 = ""
TOKEN4 = ""
TOKEN5 = ""


@client1.command()
async def frame(ctx, frame):
    await ctx.send(image(frame))


@client1.command()
async def start(ctx):
    framecounter = 1

    clients = []
    clients.append(client1)
    clients.append(client2)
    clients.append(client3)
    clients.append(client4)
    clients.append(client5)
    channels = []
    for i in range(5):
        channels.append(clients[i].get_channel()) # here should be id of your channel
    try:
        await ctx.author.voice.channel.connect()
    except discord.errors.ClientException:
        pass
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client1.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio(f"frames/badapple.mp3") #here take your own path to the badapple.mp3
    voice_client.play(audio_source)
    start_time = time.time()
    curclient = 1
    for i in range(2171):
        if curclient >= 5:
            curclient = 1
        if start_time + framecounter * 0.1 <= time.time():
            delay = (((time.time() - start_time) / 0.1) - framecounter) * 0.1
            print(f"delay of {delay} seconds")
            channel = channels[curclient]
            framecounter += 1
            if delay >= 0.3:
                framecounter += 1
            clients[curclient].loop.create_task(channel.send(image(framecounter)))
        else:
            print(f"delay of {(((time.time() - start_time) / 0.1) - framecounter) * 0.1} seconds")
            await asyncio.sleep(abs((((time.time() - start_time) / 0.1) - framecounter) * 0.1))
            channel = channels[curclient]
            clients[curclient].loop.create_task(channel.send(image(framecounter)))
        curclient += 1
        framecounter += 1


loop = asyncio.new_event_loop()
loop.create_task(client1.start(TOKENmain))
loop.create_task(client2.start(TOKEN2))
loop.create_task(client3.start(TOKEN3))
loop.create_task(client4.start(TOKEN4))
loop.create_task(client5.start(TOKEN5))

loop.run_forever()
