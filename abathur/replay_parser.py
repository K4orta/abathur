import sc2reader, sys, calendar, resources, re

def parse_matchup(directory, tags, meta_options):
    replays = sc2reader.load_replays(directory, depth=0)
    best_of = meta_options['best_of'] if 'best_of' in meta_options else 3
    games = []
    match = resources.Matchup(list(tags), best_of)
    count = 0
    for replay in replays:
        games.append(parse_game(replay))
        count += 1

    match.set_games(games)
    match.sortGames()
    match.number_games()
    # print(match.to_object())
    # print("==============")
    return match

def parse_game(replay):
    game = resources.Game()
    game.set_time(replay.start_time, replay.end_time)
    game.set_winner({
        "name": replay.winner.players[0].name,
        "race": replay.winner.players[0].pick_race.encode('ascii','ignore'),
    })
    for player in replay.players:
        game.add_player(player.name, player.pick_race.encode('ascii','ignore'))

    game.map = replay.map_name
    return game


if(__name__ == "__main__"):
    parse_matchup(sys.argv[1])
