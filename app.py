import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Just for now (hardcoded login)
VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower()== "true"
    app.run(debug=debug_mode)