import requests
from .bot import bot

@bot.event
async def on_guild_join(guild):
    payload = {
        "guild_id": guild.id,
        "name": guild.name
    }

    response = requests.post("http://localhost:8000/guilds", json=payload)

    print(response.status_code)