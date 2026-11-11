def pipeline(sudo_code):
    demo_parser()
    process_demo()

    round_extractor()
    kill_extractor()
    grenade_extractor()

    player_stats()

    postgres_loader()
