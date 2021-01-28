import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_pelaaja_olemassa(self):
        player = self.statistics.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")


    def test_search_pelaaja_ei_ole_olemassa(self):
        player = self.statistics.search("Foo")
        self.assertIsNone(player)

    def test_team_olemassa(self):
        players = self.statistics.team("EDM")
        self.assertEqual(len(players), 3)

    def test_team_ei_ole_olemassa(self):
        players = self.statistics.team("FOO")
        self.assertEqual(len(players), 0)

    def test_top_scoreres_top_2(self):
        players = self.statistics.top_scorers(2)
        self.assertEqual(len(players), 2)
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[0].name, "Gretzky")

