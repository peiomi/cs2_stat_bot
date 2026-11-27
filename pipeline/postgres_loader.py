from app.models import Player, Map, DiscordUser, GuildMember, Guild
from app.database import SessionLocal

class PostgresLoader():
    def __init__(self):
        self.db = SessionLocal()

    def load(self):
        pass

    def load_players(self, players):
        for _, row in players.iterrows():
            existing_player = (
                self.db.query(Player)
                .filter(Player.steam_id == row["steamid"])
                .first()
            )

            if not existing_player:
                player = Player(
                    steam_id=row["steamid"],
                    name=row["name"]
                )
                self.db.add(player)
        self.db.commit()

    def load_player(self, player):
        existing_player = (
            self.db.query(Player)
            .filter(Player.steam_id == player.steam_id)
            .first()
        )

        if existing_player:
            return existing_player

        
        self.db.add(player)
        self.db.commit()
        self.db.refresh(player)

        return player


    def load_user(self, user, player):
        existing_user = (
            self.db.query(DiscordUser)
            .filter(DiscordUser.discord_user_id == user.discord_user_id)
            .first()
        )

        existing_link = (
            self.db.query(DiscordUser)
            .filter(DiscordUser.player_id == player.id)
            .first()
        )

        if existing_user:
            raise Exception("Discord user already linked to a Steam account")

        if existing_link:
            raise Exception("Steam account already linked to another Discord user")
        

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def load_guild_member(self, guild_member):
        existing_member = (
            self.db.query(GuildMember)
            .filter(
                GuildMember.guild_id == guild_member.guild_id,
                GuildMember.discord_user_id == guild_member.discord_user_id
            )
            .first()
        )

        if existing_member:
            return existing_member

        self.db.add(guild_member)
        self.db.commit()
        self.db.refresh(guild_member)

        return guild_member

    def load_map(self, map_name: str):
        existing_map = (
            self.db.query(Map)
            .filter(Map.name == map_name)
            .first()
        )

        if existing_map:
            raise Exception("Map already exists")

        cs_map = Map(
            name=map_name
        )
        self.db.add(cs_map)
        self.db.commit()
        self.db.refresh(cs_map)

        return cs_map

    def load_guild(self, guild):
        existing_guild = (
            self.db.query(Guild)
            .filter(Guild.guild_id == guild.guild_id)
            .first()
        )

        if existing_guild:
            return existing_guild

        self.db.add(guild)
        self.db.commit()
        self.db.refresh(guild)

        return guild