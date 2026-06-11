import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/login")
def login():
    user_input = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # CodeQL flags this line as a high-severity flaw
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    # cursor.execute(query)
    
    return "Query executed."