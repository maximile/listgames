from google.appengine.ext import db
import re

VALID_NAME = re.compile("[a-z0-9]{3,100}$")

class Game(db.Model):
    """A single list game.
    
    """    
    date = db.DateTimeProperty(auto_now_add=True)
    
    def get_url(self):
        return "/%s" % self.get_name()
    
    def get_name(self):
        return self.key().name()

def get_games():
    return db.GqlQuery("SELECT * FROM Game")    

def validate_name(name):
    """Check the game name for length and invalid characters.

    """
    if not VALID_NAME.match(name):
        raise ValueError("Game name must match: %s" % VALID_NAME.pattern)
