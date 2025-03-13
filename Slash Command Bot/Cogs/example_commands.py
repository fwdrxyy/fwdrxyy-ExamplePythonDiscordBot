import discord
from discord.ext import commands

class example_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Simple ping command
    @discord.slash_command(name="ping", description="Sends the bot's latency.")    
    async def ping(self, ctx):
        await ctx.respond(f"Pong! Latency is {self.bot.latency * 1000:.2f}ms")