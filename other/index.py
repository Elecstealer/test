from flask import Flask, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", passwd="1234", db="study1_db", charset="utf8")
cur = db.cursor()

@app.route('/')
def index():
    sql = "SELECT * form board"
    cur.execute(sql)

    data_list = cur.fetchall()
    return render_template('index.html', data_list=data_list)

#@app.route('/write')
#def write():
    return render_template('write.html')

if __name__ == '__main__':
    app.run()