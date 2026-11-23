from unittest.mock import MagicMock, patch

@patch("your_package.demo_processor.requests.post")
def test_process_players_posts_each_player(self, mock_post):
    processor = DemoProcessor("url")

    player1 = MagicMock()
    player1.steamid = "123"
    player1.name = "alice"

    player2 = MagicMock()
    player2.steamid = "456"
    player2.name = "bob"

    processor.demo = MagicMock()
    processor.demo.parse_player_info.return_value = [
        player1,
        player2
    ]

    processor.process_players()

    self.assertEqual(mock_post.call_count, 2)



def test_process_players_returns_players(self):
    processor = DemoProcessor("url")

    players = [MagicMock(), MagicMock()]

    processor.demo = MagicMock()
    processor.demo.parse_player_info.return_value = players

    result = processor.process_players()

    self.assertEqual(result, players)



@patch("your_package.demo_processor.requests.post")
def test_process_players_builds_correct_payload(self, mock_post):
    player = MagicMock()
    player.steamid = "123"
    player.name = "Paydon"

    processor = DemoProcessor("url")

    processor.demo = MagicMock()
    processor.demo.parse_player_info.return_value = [player]

    processor.process_players()

    mock_post.assert_called_once_with(
        "http://localhost:8000/players",
        json={
            "steam_id": "123",
            "name": "Paydon",
        }
    )