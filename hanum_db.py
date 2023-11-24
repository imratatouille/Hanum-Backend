import pymysql

# db에 데이터 추가
# db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
# cursor = db.cursor()

# cursor.execute('USE hanum_db;')
# cursor.execute('INSERT INTO post_table (author, pwd, content, title) VALUES ("권기현", "1234", "db 새로 설정중", "하 시발좆같은 backend");')

# db.commit()
# db.close()
    
# db에 있는 post_table 내용 확인
def idcheck():
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    cursor.execute('select id from post_table')
    res = cursor.fetchall()

    for data in res:
        wow = str(data)
        id = wow.replace("(","").replace(")","").replace(",","")
        print(id)

    db.commit() 
    db.close()