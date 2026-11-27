import requests
from .bot import bot
from pipeline import PostgresLoader
from app.models import Guild

loader = PostgresLoader()

@bot.event
async def on_guild_join(guild: discord.Guild):
    loader.load_guild(
        Guild(
            guild_id=guild.id,
            name=guild.name
        )
    )