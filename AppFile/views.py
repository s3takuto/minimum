from AppFile import app
import defs

@app.route("/")
def index1():
    return "index1"

@app.route("/2")
def index2():
    return defs.func()