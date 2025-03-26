from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv() #Load settings from .env file

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, DevSecOps World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("DEBUG", "False").lower() == "true"
    host = os.environ.get("HOST", "127.0.0.1")

    app.run(debug=debug_mode, host=host, port=port)

