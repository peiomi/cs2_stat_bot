import requests
import bz2
import shutil

from .bot import bot
from .pipeline import DemoParser

@bot.tree.command(name="process-demo")
async def process_demo(interaction: discord.Interaction, demo_url: str):
    if interaction.user.id not in database:
        await interaction.response.send_message(
            "steam account not linked. use /link-steam <steam_id> command first."
            "use /help if you need help finding your steam ID."
        )
        return
    await interaction.response.send_message(
        "downloading demo..."
    )

    demo = DemoParser(demo_url)
    demo.process_demo()
    players = demo.process_players()

    for player in players:
        payload = {
            "steam_id": player.steamid,
            "name": player.name
        }

        response = requests.post("http://localhost:8000/players", json=payload)

@bot.tree.command(name="link-steam")
async def link_steam_id(interaction: discord.Interaction, steam_id: str):
    response = requests.get(
        "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/",
        params={
            "key": STEAM_API_KEY,
            "steamids": steam_id,
        }
    )

    data = response.json()

    if not data["response"]["players"]:
        await interaction.response.send_message(
            "Invalid Steam ID."
        )
        return

    player_payload = {
        "steam_id": steam_id,
        "player_name": data["response"]["players"][0]["personaname"]
    }
    player_create = requests.post("http://localhost:8000/players", json=player_payload)
    player = player_create.json()

    user_payload = {
        "discord_id": interaction.user.id,
        "username": interaction.user.name,
        "player_id": player["id"]
    }
    user_create = requests.post("http://localhost:8000/discord-users", json=user_payload)
    

