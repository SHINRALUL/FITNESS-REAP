import discord
import random
import asyncio
import os

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)

    code = random.randint(100000, 999999)

    await channel.send(
        "🔥 **DAILY FITNESS VERIFICATION** 🔥\n\n"
        f"Today’s code: **{code}**\n\n"
        "Write this number down and show it clearly in your photo or video.\n"
        "No code = no credit."
    )

    await client.close()

client.run(TOKEN)
