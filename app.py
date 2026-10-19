from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Use the database file in the same folder as app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "users.db")


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create the users table
def create_table():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            role TEXT
        )
    """)

    conn.commit()
    conn.close()


# Create the table when the application starts
create_table()


# Home page - show users
@app.route("/")
def index():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return render_template("index.html", users=users)


# Add user page
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]

        conn = get_db()
        conn.execute(
            "INSERT INTO users (name, role) VALUES (?, ?)",
            (name, role)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_user.html")


# Delete user
@app.route("/delete/<int:id>")
def delete_user(id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
