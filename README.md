# CS2 Stat Bot

A Discord bot and ETL pipeline for parsing Counter-Strike 2 demo files, generating player performance metrics, and producing data visualizations for match reviewing.

> **Project status:** I am in the planning stages. Everything in this README.md are currently just ideas. 

## Overview 

CS2 stat bot will extract data from a given CS2 demo file and transform raw game events into player and match insights. 

Users will be able to upload and reference match demo files through Discord commands. The system will parse demo data, process player stats, store results in a relational database, and generate visual reports that can be viewed directly within Discord.

## Features

### Demo Parsing

- Parse CS2 `.dem` files
- Extract player stats and match events:
    - Kills/Deaths/Assists
    - Headshot %
    - ADR
    - Util usage
    - KAST
    - Clutches
    - MVP's
    - Trades
    - Opening duels

### ETL Pipeline

- Extract raw event data from match demos
- Transform game events into analytics-ready datasets
- Load processed data into PostgreSQL
- Maintain historical match and player records

### Discord Bot

- Upload and process match demos
- Retrieve stats on demand
- Compare player performance across matches 
- Generate visual reports through slash commands

### Data Visualization

- Dashboard of match/player stats
- Heat maps of where players die the most & get the most kills
- Heat maps of where molly/HE nades are thrown and how much damage is done 
- Heat maps of flashes and their blind time


## Tech Stack

- Python
- FastAPI
- discord.py
- PostgreSQL
- Alembic
- Jupyter Notebook
- Matplotlib
- Docker


## Example Commands

```bash
/process-demo match.dem
```

```bash
/player-stats steam_id
```

```bash
/nade-damage match_id
```

```bash
/flashes match_id
```

## Database Schema

Entities:

- Players
- Matches
- Rounds
- Match Events
- Player Stats
- Performance Reports

## Future Enhancments (the ambitious ideas that are taking a backseat)

- Discord server specific leaderboards
- Automated demo retrieval
- Cloud-based processing 
- Faceit integration

