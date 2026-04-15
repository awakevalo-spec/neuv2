import os
import discord
from discord.ext import tasks, commands

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1489930989890175040

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("@everyone")

    send_ping.start()

@tasks.loop(hours=1)
async def send_ping():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("@everyone")

if TOKEN is None:
    print("❌ Kein TOKEN gefunden! Check Render Environment Variables.")
else:
    bot.run(TOKEN)