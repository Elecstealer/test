import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="1234", db="study1_db", charset="utf8")
cur = db.cursor()

sql = "SELECT * from board"
cur.execute(sql)

sql2 = "INSERT INTO board (num, title, writer, views, context) VALUES ('5', 'test1', 'ME', '6', '하이!')"
cur.execute(sql2)
db.commit()
db.close()

data_list = cur.fetchall()
