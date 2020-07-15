from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<center><h1>WELCOME TO PYTHON WEBSITE.<br>never give up !! great things take time !!!</h1></center>"
if(__name__) == "__main__":
    app.run()
