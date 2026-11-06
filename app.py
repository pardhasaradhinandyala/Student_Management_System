
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "student-management-secret"

DATABASE = "students.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    search = request.args.get("search", "").strip()

    conn = get_db()

    if search:
        students = conn.execute("""
            SELECT * FROM students
            WHERE name LIKE ? OR email LIKE ? OR course LIKE ?
            ORDER BY id DESC
        """, (f"%{search}%", f"%{search}%", f"%{search}%")).fetchall()
    else:
        students = conn.execute(
            "SELECT * FROM students ORDER BY id DESC"
        ).fetchall()

    conn.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"].strip()
    email = request.form["email"].strip()
    course = request.form["course"].strip()

    if not name or not email or not course:
        flash("Please fill in all fields.")
        return redirect(url_for("index"))

    conn = get_db()
    conn.execute(
        "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
        (name, email, course)
    )
    conn.commit()
    conn.close()

    flash("Student added successfully!")
    return redirect(url_for("index"))


@app.route("/edit/<int:id>", methods=["POST"])
def edit_student(id):
    name = request.form["name"].strip()
    email = request.form["email"].strip()
    course = request.form["course"].strip()

    if not name or not email or not course:
        flash("All fields are required.")
        return redirect(url_for("index"))

    conn = get_db()
    conn.execute("""
        UPDATE students
        SET name = ?, email = ?, course = ?
        WHERE id = ?
    """, (name, email, course, id))

    conn.commit()
    conn.close()

    flash("Student updated successfully!")
    return redirect(url_for("index"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete_student(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    flash("Student deleted successfully!")
    return redirect(url_for("index"))


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
