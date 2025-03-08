import discord
import os
import random
import asyncio
from discord.ext import tasks
from datetime import datetime, time

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Replace with your actual Discord channel ID
CHANNEL_ID = 123456789012345678  # Replace with the actual channel ID
SPECIFIC_USER_ID = 490346827334287360

# List of messages to send
messages = [
    "Good morning, my love! ☀️ I hope you have the most amazing day! ❤️",
    "Rise and shine, beautiful! Today is another chance to be amazing. 😘",
    "Waking up knowing you’re in my life makes every day special. 💖",
    "You are the sunshine that brightens my day. 🌞 I love you!",
    "Morning, my love! Remember that you are loved and cherished always. ❤️"
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    send_morning_message.start()  # Start the scheduled task
    

@tasks.loop(time=time(17, 0, 0)) 
async def send_morning_message():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        message = random.choice(messages)
        await channel.send(message)
    else:
        print("Channel not found. Please check the channel ID.")


client.run(os.getenv('TOKEN'))

