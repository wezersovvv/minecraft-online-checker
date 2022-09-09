# minecraft-online-checker
Discord bot for track online users at your minecraft server

First, change the parameters in the file main.py, namely:


d_text = "TechnoMagic 1.7.10"

embed.set_footer(text=f"by wezersovvv#9439")

online = get_online("ip","port")

embed = await create_embed("Some Text", "Minecraft", 975839690471112744, servers=[{"ip": "IP", "port": "PORT", "players": get_online("ip","port"), "max_players": 2022}])

await edit_message(1007233683754856468, 1007234131123507260, embed)


After editing the file, launch the bot, go to the channel specified in the config and send the command !send 1, then edit MESSAGE ID and restart the bot.
The bot will update the information every 3 minutes.


The bot was created using the mcsrvstat API.