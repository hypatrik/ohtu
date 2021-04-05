from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, Or
from querybuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(5, "assists"),
    #     PlaysIn("PHI")
    # )

    # matcher = And(
    #     Not(HasAtLeast(1, "goals")),
    #     PlaysIn("NYR")
    # )

    # matcher = And(
    #     HasAtLeast(50, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("NYI"),
    #         PlaysIn("BOS")
    #     )
    # )
    query = QueryBuilder()

    matcher = (
      query  
        .playsIn("NYR")  
        .hasAtLeast(5, "goals")  
        .hasFewerThan(10, "goals")  
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
