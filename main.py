from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Hello, World!"})

@app.route("/about")
def about():
    return jsonify({"owner": "Ihor Kolomiiets", "message": "OKay"})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
