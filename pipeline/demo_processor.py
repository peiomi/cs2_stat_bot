from demoparser2 import DemoParser 
import requests
import bz2
import shutil
import discord
from pathlib import Path

class DemoProcessor():
    def __init__(self, source: str | discord.Attachment):
        self.source = source
        self.demo = None
        self.demo_name = ""

    async def process_demo(self):
        if isinstance(self.source, str):
            response = requests.get(self.source)
            response.raise_for_status()

            compressed_name = Path(self.source).name
            with open(compressed_name, "wb") as f:
                f.write(response.content)

            self.demo_name = compressed_name.removesuffix(".bz2")

            with bz2.open(compressed_name, "rb") as source:
                with open(self.demo_name, "wb") as dest:
                    shutil.copyfileobj(source, dest)

        elif isinstance(self.source, discord.Attachment):
            if self.source.filename.endswith(".dem"):
                self.demo_name = self.source.filename

                await self.source.save(self.demo_name)

            elif self.source.filename.endswith(".dem.bz2"):
                compressed_name = self.source.filename

                await self.source.save(compressed_name)

                self.demo_name = compressed_name.removesuffix(".bz2")

                with bz2.open(compressed_name, "rb") as source:
                    with open(self.demo_name, "wb") as dest:
                        shutil.copyfileobj(source, dest)

            else:
                raise ValueError("File must be .dem or .dem.bz2")

        self.demo = DemoParser(self.demo_name)

        return self.demo

    def process_players(self):
        if self.demo is None:
            raise ValueError("process_demo() must be called first")

        players = self.demo.parse_player_info()
        
        return players

    def process_map(self):
        if self.demo is None:
            raise ValueError("process_demo() must be called first")

        header = self.demo.parse_header()
        map_name = header["map_name"]

        return map_name

    
        
# just for experimenting w demoparser2
if __name__ == "__main__":
    demo = Demo("003853913717792047283_0996826481.dem")
    kills = demo.parse_event("player_death")
    print(
        kills[
            [
                "attacker_name",
                "user_name",
                "assister_name",
                "weapon",
                "headshot",
                "tick"
            ]
        ].head()
    )
