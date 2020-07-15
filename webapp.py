from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<center><h1>WELCOME TO PYTHON WEBSITE.</h1><br><h4>never give up !! great things take time !!!</h4></center>"
if(__name__) == "__main__":
    app.run()
