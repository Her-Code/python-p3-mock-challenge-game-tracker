class Game:
    def __init__(self, title):
        self.title = title
         # Internal storage for results associated with this game
        self._results = []

    @property
    def title(self):
        # get and return the title of the game
        return self._title
    
    @title.setter
    def title(self,title):
        # set the title if not an empty string
        if isinstance (title,str) and len(title) > 0:
            self._title=title


    def results(self):
        """Return all results associated with this game."""
        return [result for result in Result.all if result.game == self]

    def players(self):
        """Return a list of unique players who have played this game."""
        return list({result.player for result in self.results()})
        

    def average_score(self, player):
        """Calculate the average score for a specific player in this game."""
        scores = [result.score for result in self.results() if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        return None

        pass

class Player:
    def __init__(self, username):
        self.username = username
        # Internal storage for results associated with this player
        self._results = [] 

    @property
    def username(self):
        # get and return the username of the player
        return self._username
    
    @username.setter
    def username(self,username):
         # Set the username if it is a string between 2 and 16 characters
        if isinstance(username,str) and 2 <= len(username) <= 16:
            self._username=username


    def results(self):
        """Return all results associated with this player."""
        return [result for result in Result.all if result._player == self]
        pass

    def games_played(self):
        """Return a list of unique games that this player has played."""
        return list({result.game for result in self.results()})
        pass

    def played_game(self, game):
        """Check if this player has played a specific game."""
        return any(result.game == game for result in self.results())

        pass

    def num_times_played(self, game):
        """Return the number of times this player has played a specific game."""
        return sum(1 for result in self.results() if result.game == game)

        pass

class Result:
    # Class variable to keep track of all result instances
    all = []

    def __init__(self, player, game, score):
        # Player associated with this result
        self._player = player
        # game associated with this result
        self._game = game
        # score associated with this result
        self._score = score
        Result.all.append(self) # Add this result to the class-level list of all results

    @property
    def player(self):
        # Return the player associated with this result
        return self._player
    
    @property
    def game(self):
        # Return the game associated with this result
        return self._game
    
    @property
    def score(self):
        # Return the score associated with this result
        return self._score
    
    @score.setter
    def score(self,value):
        # Set the score if it's an integer between 1 and 5000
        if isinstance(value,(int,len())) and  (1 <= value<= 5000):
            self._score=value
        else:
            # Raise an error if the score is invalid
            raise ValueError("Score must be an integer between 1 and 5000.")