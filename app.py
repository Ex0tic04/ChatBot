from flask import Flask, render_template
import mysql.connector
from config_db import ht, us,pd,db

app = Flask(__name__)

daba = mysql.connector.connect(
    host=ht,
    user=us,
    passwd=pd,
    database=db
)
cursor = daba.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bot', methods=['GET', 'POST'])
def bot():
    return render_template('dialog.html')


if __name__ == '__main__':
    app.run(debug=True)