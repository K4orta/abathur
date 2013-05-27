import calendar, sys

class Matchup:
    def __init__(self, tags, best_of=3):
        self.best_of = best_of
        self.tags_array = tags
        self.__end_time = None
        self.__teams = []
        self.__scoreboard = {}
        self.__games = []
        self.winner = None

    def sortGames(self):
        self.__games.sort(key=lambda game: game.unix_start_time())

    def has_winner(self):
        pass

    def set_games(self, game_list):
        self.__games = game_list

        for game in self.__games:
            game_winner = game.get_winner()
            # if(game_winner):
            #     self.__scoreboard[game_winner['name']] += 1
        #
        for i in range(len(self.__games), self.best_of):
            self.__games.append( Game() )
        # print("scoreboard: {0}".format(self.__scoreboard))
        self.has_winner()

    def set_teams():
        pass

    def use_aliases(self):
        pass

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
            "teams": self.__teams
        }

class Game:
    def __init__(self, num=0):
        self.number = num
        self.__starts_at = None
        self.__ends_at = None
        self.__winner = None
        self.status = "ready"
        self.players = []
        self.vod_url = None
        self.map = None

    def set_time(self, time_start, time_end):
        self.__starts_at = time_start
        self.__ends_at = time_end
        return self

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

