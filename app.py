from flask import Flask, render_template, request, redirect
import mysql.connector
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ruby2302",
    database="user_data"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/healthmeta', methods=['POST'])
def healthmeta():
    username = request.form['username']
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    medicine = request.form['medicine']
    
    cursor = db.cursor()
    sql = "INSERT INTO users (username, height, weight, medicine) VALUES (%s, %s, %s, %s)"
    val = (username, height, weight, medicine)
    cursor.execute(sql, val)
    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)