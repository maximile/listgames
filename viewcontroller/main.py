from string import Template
import model.game
import util.numberwords
import webapp2
from google.appengine.api import users

class Handler(webapp2.RequestHandler):
    def get(self):
        template_source = open("templates/main.html").read()
        template = Template(template_source)
        substitutions = {}

        # Number of games on the site
        games = model.game.get_games()
        game_count = len(games)
        game_count_string = util.numberwords.int_to_words(game_count)
        game_count_string = game_count_string.capitalize()
        substitutions["game_count"] = game_count_string

        # Create a list of game names linking to their pages
        substitutions["gamelist"] = get_game_link_list()
        output = template.substitute(substitutions)
        
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.out.write(output)
    
def get_game_link_list():
    games = model.game.Game.all()
    
    items = []
    for game in games:
        items.append('<li><a href="%s">%s</a></li>' %
                     (game.get_url(), game.get_name()))
    
    return "\n".join(items)

def main():
    app = webapp2.WSGIApplication([('/', Handler)], debug=True)
    app.run()

if __name__ == "__main__":
    main()
