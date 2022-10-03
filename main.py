import discord
from discord.ext import tasks
from discord.ext import commands
import requests
import json

client = commands.Bot(command_prefix = '!')

def get_online(ip, port=None):
    try:
        r = requests.get(f"https://api.mcsrvstat.us/2/{ip}:{port}")
        r = r.json()
        online = r['players']['online']
        return online
    except:
        return 0
        



async def create_embed(desc, title, user,servers = {}, color=0x2f3136):
    author = await client.fetch_user(user)
    embed = discord.Embed(title = title, description = desc, color = color)
    
    f_text = ""
    s_text = ""
    d_text = "TechnoMagic 1.7.10"

    for i in servers:
        f_text += f"{i['ip']}{i['port']}\n"
        s_text += f"{i['players']}/{i['max_players']}\n"

    embed.add_field(name="IP и порт", value=f_text)
    embed.add_field(name="Игроков", value=s_text)
    embed.add_field(name="Сервер", value=d_text)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/592277274397769748/679129902297120829/minecraft.png')
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"by wezersovvv#9439")
    return embed

async def edit_message(channel, message, embed):
    channel = await client.fetch_channel(channel)
    message = await channel.fetch_message(message)

    await message.edit(embed=embed, content = None)

@tasks.loop(minutes=3.0)
async def change_status():
    online = get_online("ip","port")
    embed = await create_embed("Some Text", "Minecraft", 975839690471112744, servers=[{"ip": "IP", "port": "PORT", "players": get_online("ip","port"), "max_players": 2022}])
    await edit_message(1007233683754856468, 1007234131123507260, embed)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"за {online} игроками"))




@client.event
async def on_ready():
    change_status.start()
    print('Bot connected')
    
@client.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(administrator=True)
async def send(ctx, channel, message):
    channel = await client.fetch_channel(channel)
    await channel.send(message)

client.run("token")
