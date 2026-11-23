from . import (
    DemoProcessor,
    RoundExtractor,
    KillExtractor,
    GrenadeExtractor,
    PlayerStatsExtractor,
    PostgresLoader
)

class Pipeline():
    def __init__(self, demo_url):
        self.parser = DemoProcessor(demo_url=demo_url)
        self.rounds = RoundExtractor()
        self.kills = KillExtractor()
        self.grenades = GrenadeExtractor()
        self.player_stats = PlayerStatsExtractor()
        self.postgres = PostgresLoader()

    def run(self):
        # real code
        processed_demo = self.parser.process_demo()
        self.parser.process_players()

        # fake TODO code 
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