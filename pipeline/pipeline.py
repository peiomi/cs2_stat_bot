
class Pipeline():

    def run(self):
        demo_parser()
        process_demo()

        round_extractor()
        kill_extractor()
        grenade_extractor()

        player_stats()

        postgres_loader()

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()