from flask import Flask

app = Flask (__name__)

@app.route("/")
def top():
    return"しろにんげんこつ"

app.run(host="0.0.0.0")