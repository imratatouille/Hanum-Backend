import pymysql
from flask import jsonify

# db에 데이터 추가
def insert_db(author, pwd, content, title):
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    cursor.execute(f'INSERT INTO post_table (author, pwd, content, title) VALUES ("{author}", "{pwd}", "{content}", "{title}");')

    db.commit()
    db.close()
    
# db에 있는 post_table 내용 확인
def idcheck():
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    cursor.execute('select id from post_table ORDER BY id DESC LIMIT 1')
    res = cursor.fetchone()

    for data in res:
        data = data
        # id = wow.replace("(","").replace(")","").replace(",","").replace("'","")
        # id = int(id)
        return data

    db.commit() 
    db.close()