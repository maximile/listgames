import webapp2
import model.game

class Handler(webapp2.RequestHandler):
    def get(self):
        template = open("templates/newgame.html").read()
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(template)
    
    def post(self):
        name = self.request.get('name')
        game = model.game.Game(name=name)
        game.put()
        self.response.out.write('Created game %s' % name)

def main():
    app = webapp2.WSGIApplication([('/newgame', Handler)], debug=True)
    app.run()

if __name__ == "__main__":
    main()

