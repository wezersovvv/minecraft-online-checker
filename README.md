# minecraft-online-checker
Discord bot for track online users at your minecraft server

First, change the parameters in the file main.py, namely:


embed.add_field(name="Server Name", value=f"Test server")

embed = create_embed("text", "server name", REPLACE WITH YOUR DISCORD ID, "ip", "port", online)

online = get_online("ip", "port")

await edit_message(CHANNEL ID, MESSAGE ID, embed)

client.run("YOUR TOKEN HERE")


After editing the file, launch the bot, go to the channel specified in the config and send the command !send 1, then edit MESSAGE ID and restart the bot.
The bot will update the information every 3 minutes.


The bot was created using the mcsrvstat API.