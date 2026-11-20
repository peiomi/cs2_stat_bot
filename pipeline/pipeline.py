from . import (
    DemoParser,
    RoundExtractor,
    KillExtractor,
    GrenadeExtractor,
    PlayerStatsExtractor,
    PostgresLoader
)

class Pipeline():
    def __init__(self):
        self.parser = DemoParser()
        self.rounds = RoundExtractor()
        self.kills = KillExtractor()
        self.grenades = GrenadeExtractor()
        self.player_stats = PlayerStatsExtractor()
        self.postgres = PostgresLoader()

    def run(self):
        demo = self.parser.parse_demo("test.dem")

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