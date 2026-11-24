import discord
import requests
import logging
from discord import app_commands

logging.basicConfig(level=logging.INFO)

class CS2StatBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        logging.info("Logged in as %s", self.user)

bot = CS2StatBot()

