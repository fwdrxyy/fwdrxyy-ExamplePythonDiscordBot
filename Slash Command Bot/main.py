import discord
from discord.ext import commands, tasks

import asyncio

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online and ready to go!')
    change_status.start()

@tasks.loop(seconds=10)  # Change status every 10 seconds
async def change_status():
    await bot.wait_until_ready()  # Ensure the bot is ready
    while True:
        server_count = len(bot.guilds) # <---- This will count the server your bot is in if you add it as a status
        statuses = [
            discord.Game(name="Now Online via Visual Studio Code"),
            # Feel free to add more status if you'd like!
        ]
        for status in statuses:
            await bot.change_presence(activity=status, status=discord.Status.online)
            await asyncio.sleep(10)

@bot.event
async def on_ready():
    if not change_status.is_running():
        change_status.start()
        
        
# Load the Cogs if you have any
bot.load_extension('Cogs.example_commands')

bot.run("BOT_TOKEN_HERE")