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
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
