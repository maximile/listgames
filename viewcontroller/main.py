from string import Template
import model.game
import webapp2

class Handler(webapp2.RequestHandler):
    def get(self):
        template_source = open("templates/main.html").read()
        template = Template(template_source)
        substitutions = {}
        
        # Create a list of game names linking to their pages
        games = model.game.get_games()
        names = [game.name for game in games]
        
        substitutions["gamelist"] = get_game_link_list()
        output = template.substitute(substitutions)
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(output)
    
def get_game_link_list():
    games = model.game.Game.all()
    
    items = []
    for game in games:
        items.append('<li><a href="%s">%s</a></li>' %
                     (game.get_url(), game.name))
    
    return "\n".join(items)

def main():
    app = webapp2.WSGIApplication([('/', Handler)], debug=True)
    app.run()

if __name__ == "__main__":
    main()