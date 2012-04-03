import webapp2
import model.game

class Handler(webapp2.RequestHandler):
    def get(self):
        template = open("templates/newgame.html").read()
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template)
    
    def post(self):
        name = self.request.get('name')
        model.game.validate_name(name)
        if model.game.Game.get_by_key_name(name):
            raise ValueError("There's already a game called '%s'" % name)
        game = model.game.Game(key_name=name)
        game.put()
        self.response.out.write('Created game %s' % game.get_name())

def main():
    app = webapp2.WSGIApplication([('/newgame', Handler)], debug=True)
    app.run()

if __name__ == "__main__":
    main()

