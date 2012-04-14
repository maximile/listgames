from google.appengine.ext import db
import util.numberwords
import re

VALID_NAME = re.compile("[a-z0-9]{3,100}$")

class Game(db.Model):
    """A single list game.
    
    """    
    date = db.DateTimeProperty(auto_now_add=True)
    title = db.DateTimeProperty(auto_now_add=True)
    
    def get_url(self):
        return "/%s" % self.get_name()
    
    def get_name(self):
        return self.key().name()

def get_games():
    results = db.GqlQuery("SELECT * FROM Game").fetch(limit=1000)
    if len(results) == 1000:
        raise RuntimeError("Too many games!")
    return results

def validate_name(name):
    """Check the game name for length and invalid characters.

    """
    if not VALID_NAME.match(name):
        raise ValueError("Game name must match: %s" % VALID_NAME.pattern)

def validate_title(title):
    """Make sure the title has a number in it and no unwanted characters.
    
    """
    # Make sure it contains a number written in words
    for number in xrange(1, 1000):
        if util.numberwords.int_to_words(number) in title:
            break
    else:
        raise ValueError("Title must contain a number, written in words")
    
    if title == title.strip():
        raise ValueError("Title has whitespace at beginning or end")
    
    
    
