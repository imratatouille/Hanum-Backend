import pymysql

def connect_db():
    return pymysql.connect(host="127.0.0.1", user="root", password="shivainu070309!", charset="utf8")

# query문 실행 및 반환값 받는 함수
def execute_query(query, args=None, fetch_one=False):
    db = connect_db()
    cursor = db.cursor()

    cursor.execute('USE hanum_db;')
    cursor.execute(query, args)

    result = None
    if fetch_one:
        result = cursor.fetchone()
    else:
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]

    db.commit()
    db.close()

    return result

# db에 post를 insert하는 함수
def insert_post(author, pwd, content, title, datetime):
    query = f'INSERT INTO post_table (author, pwd, content, title, datetime) VALUES (%s, %s, %s, %s, %s);'
    args = (author, pwd, content, title, datetime)
    execute_query(query, args, fetch_one=True)
    
# db에 comment를 insert하는 함수
def insert_comment(author, pwd, content, postid):
    query = 'INSERT INTO comments_table (author, password, content, post_id) VALUES (%s, %s, %s, %s);'
    args = (author, pwd, content, postid)
    execute_query(query, args, fetch_one=True)

# db에서 마지막 post id값을 return 하는 함수
def last_post_id():
    query = 'SELECT id FROM post_table ORDER BY id DESC LIMIT 1;'
    result = execute_query(query, fetch_one=True)
    return result[0] if result else None

# db에서 post id값 받아오는 함수
def get_post_by_id(post_id):
    query = 'SELECT * FROM post_table WHERE id = %s;'
    args = (post_id,)
    result = execute_query(query, args)
    return result

# db에서 마지막 commnet id값을 return 하는 함수
def last_comment_id():
    query = 'SELECT comment_id FROM comments_table ORDER BY comment_id DESC LIMIT 1;'
    result = execute_query(query, fetch_one=True)
    return result[0] if result else None

# db에서 post를 limit값과 page값으로 제한해서 return하는 함수
def get_posts_page(page, limit):
    offset = (page - 1) * limit
    query = 'SELECT id, author, content, title, datetime FROM post_table LIMIT %s OFFSET %s;'
    args = (limit, offset)
    result = execute_query(query, args)
    return result

# db에서 post를 delete 하는 함수
def delete_post(post_id):
    query = 'DELETE FROM post_table WHERE id = %s;'
    args = (post_id,)
    execute_query(query, args, fetch_one=True)
    return True

# db에서 comment를 delete 하는 함수
def delete_comment(comment_id):
    query = 'DELETE FROM comments_table WHERE comment_id = %s;'
    args = (comment_id,)
    execute_query(query, args, fetch_one=True)
    return True

# db에서 post의 password값을 return 하는 함수
def get_post_password(post_id):
    query = 'SELECT pwd FROM post_table WHERE id = %s;'
    args = (post_id,)
    result = execute_query(query, args, fetch_one=True)
    return result[0] if result else None

# db에서 comment의 password값을 return 하는 함수
def get_comment_password(comment_id):
    query = 'SELECT password FROM comments_table WHERE comment_id = %s;'
    args = (comment_id,)
    result = execute_query(query, args, fetch_one=True)
    return result[0] if result else None