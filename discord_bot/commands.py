import requests

from .bot import bot
from .pipeline import Pipeline

@bot.tree.command(name="process-demo")
async def process_demo(interaction: discord.Interaction, source: str | discord.Attachment):
    response = requests.get( f"http://localhost:8000/discord-users/discord-id/{interaction.user.id}")

    if response.status_code == 404:
        await interaction.response.send_message(
            "steam account not linked. use /link-steam <steam_id> command first."
            "use /help if you need help finding your steam ID."
        )
        return

    await interaction.response.send_message(
        "downloading demo..."
    )

    try:
        pipeline = Pipeline(source)
        await pipeline.run()

    except ValueError as e:
        await interaction.followup.send(str(e))
        return

    await interaction.followup.send("done!")

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
    player_create.raise_for_status()
    player = player_create.json()

    user_payload = {
        "discord_user_id": interaction.user.id,
        "username": interaction.user.name,
        "player_id": player["id"]
    }
    user_create = requests.post("http://localhost:8000/discord-users", json=user_payload)
    user_create.raise_for_status()
    user = user_create.json()

    nickname = interaction.user.nick
    if not nickname:
        nickname = interaction.user.display_name

    guild = requests.get(f"http://localhost:8000/guilds/guild-id/{interaction.guild.id}")
    guild.raise_for_status()
    guild_data = guild.json()
    
    member_payload = {
        "nickname": nickname,
        "discord_user_id": user["id"]
    }
    
    member_role = interaction.user.top_role.name
    if member_role != "@everyone":
        member_payload["member_role"] = member_role

    member_create = requests.post(f"http://localhost:8000/guilds/{guild_data['id']}/members", json=member_payload)
    member_create.raise_for_status()

    await interaction.response.send_message(
        f"successfully linked {user['username']}'s steam account: {player['player_name']}"
    )

