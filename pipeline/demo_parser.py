from demoparser2 import DemoParser as Demo

class DemoParser():
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


        self.demo = Demo("match.dem")

        return self.demo

    def process_players(self):
        players = self.demo.parse_player_info()
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
player name/ steam id: demo.parse_player_info()
"""