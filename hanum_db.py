import pymysql

db = pymysql.connect(host="127.0.0.1", 
                     user="root", 
                     password="shivainu070309!", 
                     charset="utf8")

cursor = db.cursor()

cursor.execute('USE hanum_db;')
cursor.execute('INSERT INTO posts (title, author) VALUES ("4시8분", "난관에부딪힘..");')

db.commit()
db.close()