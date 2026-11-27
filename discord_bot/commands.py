import requests

from .bot import bot
from pipeline import Pipeline, PostgresLoader
from app.models import Player, DiscordUser, Guild, GuildMember

loader = PostgresLoader()

@bot.tree.command(name="process-demo")
async def process_demo(interaction: discord.Interaction, source: str | discord.Attachment):
    user = (
        loader.db.query(DiscordUser)
        .filter(DiscordUser.discord_user_id == interaction.user.id)
        .first()
    )

    if not user:
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

    player = loader.load_player(
        Player(
            steam_id=steam_id,
            player_name=data["response"]["players"][0]["personaname"]
        )
    )

    try:
        user = loader.load_user(
            DiscordUser(
                discord_user_id=interaction.user.id,
                username=interaction.user.name,
                player_id=player.id
            ), 
            player
        )
    except Exception as e:
        await interaction.response.send_message(str(e))
        return


    nickname = interaction.user.nick
    if not nickname:
        nickname = interaction.user.display_name

    guild = (
        loader.db.query(Guild)
        .filter(Guild.guild_id == interaction.guild.id)
        .first()
    )
    if not guild:
        await interaction.response.send_message(
            "Guild not registered."
        )
        return

    guild_member = GuildMember(
        nickname=nickname,
        discord_user_id=user.id,
        guild_id=guild.id
    )
    
    member_role = interaction.user.top_role.name
    if member_role != "@everyone":
        guild_member.member_role = member_role

    loader.load_guild_member(guild_member)

    await interaction.response.send_message(
        f"successfully linked {user.username}'s steam account: {player.player_name}"
    )

