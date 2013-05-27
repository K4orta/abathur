import sc2reader, sys, calendar, resources, re

def parse_matchup(directory, tags, meta_options):
    replays = sc2reader.load_replays(directory, depth=0)
    best_of = meta_options['best_of'] if 'best_of' in meta_options else 3
    games = []
    regex = re.compile("^set[\d]",re.I)
    # Strip the set container tag if there is one
    if(regex.search(tags[len(tags)-1])):
        tags = tags[:len(tags)-1]
    match = resources.Matchup(list(tags), best_of)
    count = 0
    for replay in replays:
        games.append(parse_game(replay))
        count += 1

    match.set_games(games)
    match.sortGames()
    match.number_games()
    print(match.to_object())
    print("==============")
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

def parse_replay(file_path):
    replay = sc2reader.load_replay(file_path)
    print("===========")
    print("The players were: {0} and {1}".format(replay.players[0].name, replay.players[1].name))
    print("on {0}".format(replay.map_name))
    print("at {0}".format(replay.end_time))
    print("The winner was: {0}".format(replay.winner.players[0].name))
    print("===========")

if(__name__ == "__main__"):
    parse_matchup(sys.argv[1])
