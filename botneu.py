import os
import discord
from discord.ext import tasks

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1489930989890175040

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Eingeloggt als {client.user}")

    channel = client.get_channel(CHANNEL_ID)
    if channel:
        msg = await channel.send("@everyone")
        await msg.delete(delay=10)  # löscht nach 10 Sekunden

    send_ping.start()

@tasks.loop(hours=1)
async def send_ping():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        msg = await channel.send("@everyone")
        await msg.delete(delay=10)  # löscht nach 10 Sekunden

client.run(TOKEN)
