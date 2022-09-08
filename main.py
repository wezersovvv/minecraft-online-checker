import discord
from discord.ext import commands
from discord.ext import tasks
import requests
import json

client = discord.Client()

def get_online(ip, port=None):
    try:
        r = requests.get(f"https://api.mcsrvstat.us/2/{ip}:{port}")
        r = r.json()
        online = r['players']['online']
        return online
    except:
        return 0

#Убрать
@client.command()
async def send(ctx, *, text):
    await ctx.send(text)
#Убрать

async def create_embed(desc, title, user, ip, port, players, color=0x2f3136):
    author = await client.fetch_user(user)
    embed=discord.Embed(title = title, description = desc, color=color)
    embed.add_field(name="Скачать лаунчер", value=f"[Скачать](https://bulitcraft.ru/start)")
    embed.add_field(name="Игроков", value=players)
    embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.avatar_url)
    return embed

async def edit_message(channel, message, embed):
	channel = await client.fetch_channel(channel)
	message = await client.fetch_message(message)
	await message.edit(embed=embed, content=None)

@tasks.loop(minutes= 3.0)
async def change_status():
    online = get_online("ip", "port")
    embed = create_embed("Embed Text", "Server Name", 23847238462834, "n18.joinserver.ru", "25763", online)

    await edit_message(884003421072531518, 862449391109144638, embed)
    await client.change_presense(acrivity=discord.Activity(type=discord.ActivityType.watching, name = f"за {online} игроками"))

@client.event
async def on_ready():
    change_status.start()

client.run("OTk0MjQzODQ5MDcxMzY2MjM0.GZDOFK.Igp-Vh6UY-WlLN_wMhywUfANCVRtEkuUgYUA4s")


        