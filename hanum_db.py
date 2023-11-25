import pymysql

# db에 데이터 추가
def insert_db(author, pwd, content, title, datetime):
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    cursor.execute(f'INSERT INTO post_table (author, pwd, content, title, datetime) VALUES ("{author}", "{pwd}", "{content}", "{title}", "{datetime}");')

    db.commit()
    db.close()
    
# db에 있는 post_table 중에 마지막 id내용 확인
def last_id():
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    cursor.execute('select id from post_table ORDER BY id DESC LIMIT 1;')
    res = cursor.fetchone()

    for id in res:
        return id

    db.commit() 
    db.close()
    
def check(num):
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    cursor.execute(f'select * from post_table where id = {num}')
    
    columns = [column[0] for column in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    formatted_result = [{"id": row["id"], "author": row["author"], "content": row["content"], "title": row["title"]} for row in result]
    
    
    db.commit() 
    db.close()
    
    return formatted_result

def allcheck(page,limit):
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    if page == 1:
        cursor.execute(f'select * from post_table limit {limit} offset 0')
    elif page == 2:
        one_limit = limit
        limit =+ limit
        cursor.execute(f'select * from post_table limit {limit} offset {one_limit}')
    elif page == 3:
        one_limit =+ limit
        limit =+ limit
        cursor.execute(f'select * from post_table limit {limit} offset {one_limit}')
    elif page == 4:
        one_limit =+ limit
        limit =+ limit
        cursor.execute(f'select * from post_table limit {limit} offset {one_limit}')
    elif page == 5:
        one_limit =+ limit
        limit =+ limit
        cursor.execute(f'select * from post_table limit {limit} offset {one_limit}')

    columns = [column[0] for column in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    formatted_result = [{"id": row["id"], "author": row["author"], "password": row["pwd"], "content": row["content"], "title": row["title"], "uploadAt": str(row["datetime"])} for row in result]
    
    db.commit() 
    db.close()

    return formatted_result

def del_db(postID):
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()
    
    cursor.execute('USE hanum_db;')
    cursor.execute(f'delete from post_table where id = {postID}')
    
    db.commit() 
    db.close()
    
def check_pw(postID):
    db = pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")
    cursor = db.cursor()
    
    cursor.execute('USE hanum_db;')
    cursor.execute(f'select pwd from post_table where id = {postID}')
    
    pwd = cursor.fetchall()
    pwd = str(pwd)
    pwd = pwd.replace("(","").replace(")","").replace(",","").replace("'","")
    
    db.commit() 
    db.close()
    
    return pwd