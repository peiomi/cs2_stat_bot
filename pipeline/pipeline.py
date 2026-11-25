import discord
from . import (
    DemoProcessor,
    RoundExtractor,
    KillExtractor,
    GrenadeExtractor,
    PlayerStatsExtractor,
    PostgresLoader
)

class Pipeline():
    def __init__(self, source: str | discord.Attachment):
        self.processor = DemoProcessor(source)
        self.rounds = RoundExtractor()
        self.kills = KillExtractor()
        self.grenades = GrenadeExtractor()
        self.player_stats = PlayerStatsExtractor()
        self.postgres = PostgresLoader()

    async def run(self):
        # real code
        processed_demo = await self.parser.process_demo()
        self.processor.process_players()
        self.processor.process_map()

        # fake TODO code 
        # tbh it looks like this is all just going in processor 
        rounds = self.rounds.extract(processed_demo)
        kill_events = self.kills.extract(processed_demo)
        grenade_events = self.grenades.extract(processed_demo)
        player_stats = self.player_stats.extract(processed_demo)

        self.postgres.load(
            rounds=rounds,
            kill_events=kill_events,
            grenade_events=grenade_events,
            player_stats=player_stats
        )

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()