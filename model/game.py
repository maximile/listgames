from google.appengine.ext import db
import re

VALID_NAME = re.compile("[a-z0-9]{3,100}$")

def _validate_name(name):
    """Check the game name for length and invalid characters.
    
    """
    if not VALID_NAME.match(name):
        raise ValueError("Game name must match: %s" % VALID_NAME.pattern)

class Game(db.Model):
    """A single list game.
    
    """    
    name = db.StringProperty(required=True, validator=_validate_name)
    date = db.DateTimeProperty(auto_now_add=True)
    
    def get_url(self):
        return "/%s" % self.name

def get_games():
    return db.GqlQuery("SELECT * FROM Game")    

