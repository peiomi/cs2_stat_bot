from demoparser2 import DemoParser 
import requests
import bz2
import shutil

class DemoProcessor():
    def __init__(self, demo_url: str):
        self.demo_url = demo_url
        self.demo = None

    def process_demo(self):
        response = requests.get(self.demo_url)
        with open("match.dem.bz2", "wb") as f:
            f.write(response.content)

        with bz2.open("match.dem.bz2", "rb") as source:
            with open("match.dem", "wb") as dest:
                shutil.copyfileobj(source, dest)


        self.demo = DemoParser("match.dem")

        return self.demo

    def process_players(self):
        if self.demo is None:
            raise ValueError("process_demo() must be called first")

        players = self.demo.parse_player_info()

        for player in players:
            payload = {
                "steam_id": player.steamid,
                "name": player.name
            }

            response = requests.post("http://localhost:8000/players", json=payload)
        
        return players

    
        

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

"""
map name: header = demo.parse_header() > map_name = header["map_name"]
"""