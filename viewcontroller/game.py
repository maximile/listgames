from string import Template
import model.game
import webapp2

class Handler(webapp2.RequestHandler):
    def get(self, name):
        """Render the game page for the game from the name
        from the URL.
        
        """
        # Get the game object from the name from the URL
        game = model.game.Game.get_by_key_name(name)
        if not game:
            self.error(404)
            self.response.out.write("Game not found.")
            return
        
        # Load the template
        template_source = open("templates/game.html").read()
        template = Template(template_source)
        substitutions = {}
        
        # Replace $name with the game name
        substitutions["name"] = game.get_name()
        output = template.substitute(substitutions)
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(output)

def main():
    app = webapp2.WSGIApplication([('/(.*)', Handler)], debug=True)
    app.run()

if __name__ == "__main__":
    main()
