"""Greeting Flask app."""

#from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.<a href="http://localhost:5000/hello">Go to hello</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">

          <select name="complement">
            <option value="awesome">awesome</option>
            <option value="terrific">terrrific</option>
            <option value="fantastic">fantastic</option>
            <option value="neato">neato</option>
            <option value="fantabulous">fantabulous</option>
            <option value="brilliant">brilliant</option>
            <option value="incredible">incredible</option>
            <option value="wowzae">wowza</option>
          </select>

          <input type="submit" value="Submit">

        </form>


        <form action="/diss">
            <input type="submit" value="Go to diss">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    complement = request.args.get("complement")

    #y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, complement)


@app.route("/diss")
def diss_person():
  """diss user"""

  player = request.args.get("person")
  complement = request.args.get("complement")

  return """
   <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, person! You are so NOT cool!
      </body>
    </html>
    """.format(player, complement)



if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
