from app.models import Player
from app.database import SessionLocal

class PostgresLoader():
    def __init__(self):
        self.db = SessionLocal()

    def load(self):
        pass

    def load_players(self, players):
        for _, row in players.itterrows():
            player = Player(
                steam_id=row["steamid"],
                name=row["name"]
            )
            self.db.add(player)
        self.db.commit()
