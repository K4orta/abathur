import calendar, sys

class Matchup:
    def __init__(self, tags, best_of=3):
        self.best_of = best_of
        self.tags_array = tags
        self.__end_time = None
        self.__players = []
        self.__scoreboard = {}
        self.__games = []
        self.winner = None
        self.__aliases = {}

    def sort_games(self):
        self.__games.sort(key=lambda game: game.unix_start_time())

    def has_winner(self):
        for player_name in self.__scoreboard:
            player = self.get_player(player_name)
            player['score'] = self.__scoreboard[player_name]
            if player['score'] > self.best_of / 2:
                self.winner = player


    def set_games(self, game_list, match_meta):
        self.__games = game_list

        for game in self.__games:
            game_winner = game.get_winner()
            for player in game.get_players():
                self.add_player(player)
                if not player['name'] in self.__scoreboard:
                    self.__scoreboard[player['name']] = 0
            if game_winner:
                self.__scoreboard[game_winner['name']] += 1

        for i in range(len(self.__games), self.best_of):
            self.__games.append( Game() )

        if 'aliases' in match_meta:
            self.apply_aliases(match_meta['aliases'])
        self.sort_games()
        self.number_games()
        self.has_winner()

        if len(self.__games) > 0 and len(self.__games[0].get_players()) <1:
            for i in range(2):
                tbd_player = {'name': "TBD {0}".format(i+1)}
                print(match_meta)
                if 'players' in match_meta and match_meta['players'][i] != None:
                    tbd_player['name'] = match_meta['players'][i]['name']
                    tbd_player['race'] = match_meta['players'][i]['race']
                self.add_player(tbd_player)

    def add_player(self, new_player):
        for player in self.__players:
            if player['name'] == new_player['name']:
                return None
        self.__players.append(new_player)


    def get_player(self, name):
        for player in self.__players:
            if(player['name'] is name):
                return player
        return None

    def get_players(self):
        return [{'name': self.__aliases[player['name']] if player['name'] in self.__aliases else player['name'] , 'race': player['race']} for player in self.__players]


    def apply_aliases(self, aliases):
        self.__aliases = aliases

    def number_games(self):
        for i in range(len(self.__games)):
            self.__games[i].number = i + 1

    def to_object(self):
        return {
            "tags_array": self.tags_array,
            "games": [game.to_object() for game in self.__games],
            "best_of": self.best_of,
            "winner": self.winner,
            "end_time": self.__end_time,
            "teams": self.get_players()
        }

class Game:
    def __init__(self, num=0):
        self.number = num
        self.__starts_at = None
        self.__ends_at = None
        self.__winner = None
        self.status = "ready"
        self.__players = []
        self.vod_url = None
        self.map = None

    def set_time(self, time_start, time_end):
        self.__starts_at = time_start
        self.__ends_at = time_end
        return self

    def add_player(self, name, race):
        self.__players.append({
            "name": name,
            "race": race
        })

    def get_players(self):
        return self.__players

    def get_winner(self):
        return self.__winner

    def set_winner(self, winner):
        self.__winner = winner
        self.status = "finished"

    def get_start_time(self):
        return self.__starts_at

    def unix_start_time(self):
        return calendar.timegm(self.__starts_at.utctimetuple()) if self.__starts_at != None else sys.maxint

    def to_object(self):
        return {
            "number": self.number,
            "starts_at": self.__ends_at.isoformat() if self.__ends_at != None else None,
            "ends_at": self.__ends_at.isoformat() if self.__ends_at != None else None,
            "map": self.map,
            "status": self.status,
            "winner": self.__winner
        }

class Participant:
    def __init__(self):
        pass

