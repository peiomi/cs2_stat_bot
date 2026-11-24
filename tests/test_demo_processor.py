import unittest
from unittest.mock import patch, MagicMock
from pipeline import DemoProcessor

class TestDemoProcessor(unittest.IsolatedAsyncioTestCase):
    def test_process_players_requires_process_demo(self):
        processor = DemoProcessor("fake url")

        with self.assertRaises(ValueError):
            processor.process_players()

    @patch("pipeline.demo_processor.shutil.copyfileobj")
    @patch("pipeline.demo_processor.bz2.open")
    @patch("builtins.open")
    @patch("pipeline.demo_processor.DemoParser")
    @patch("pipeline.demo_processor.requests.get")
    async def test_process_demo_sets_demo(self, mock_get, mock_demo, mock_open, mock_bz2_open, mock_copyfileobj):
        mock_get.return_value.content = b"fake data"

        processor = DemoProcessor("https://example.com/test.dem.bz2")
        await processor.process_demo()

        self.assertIsNotNone(processor.demo)
        self.assertEqual(processor.demo, mock_demo.return_value)
        self.assertEqual(
            processor.demo_name,
            "test.dem"
        )

        mock_demo.assert_called_once_with(
            "test.dem"
        )


    @patch("pipeline.demo_processor.requests.post")
    def test_process_players_posts_each_player(self, mock_post):
        processor = DemoProcessor("url")

        player1 = MagicMock()
        player1.steamid = "123"
        player1.name = "boberthy"

        player2 = MagicMock()
        player2.steamid = "124"
        player2.name = "boberton"

        processor.demo = MagicMock()
        processor.demo.parse_player_info.return_value = [player1, player2]

        processor.process_players()

        self.assertEqual(mock_post.call_count, 2)


    @patch("pipeline.demo_processor.requests.post")
    def test_process_players_builds_correct_payload(self, mock_post):
        player = MagicMock()
        player.steamid = "123"
        player.name = "bobsie"

        processor = DemoProcessor("url")

        processor.demo = MagicMock()
        processor.demo.parse_player_info.return_value = [player]

        processor.process_players()

        mock_post.assert_called_once_with(
            "http://localhost:8000/players",
            json={
                "steam_id": "123",
                "name": "bobsie",
            }
        )

    @patch("pipeline.demo_processor.requests.post")
    def test_process_map_builds_correct_payload(self, mock_post):
        processor = DemoProcessor("url")

        processor.demo = MagicMock()
        processor.demo.parse_header.return_value = {"map_name": "anoobis"}

        processor.process_map()

        mock_post.assert_called_once_with(
            "http://localhost:8000/maps",
            json={
                "name": "anoobis",
            }
        )

if __name__ == "__main__":
    unittest.main()