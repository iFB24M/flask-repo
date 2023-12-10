from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://example.com", "http://localhost:5173"]}})



@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()