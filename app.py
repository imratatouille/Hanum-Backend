from flask import Flask, render_template, request, jsonify
import hanum_db
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/posts', methods=['GET','POST'])
def postit():
    if request.method == 'GET':
        limit = request.args.get('limit')
        limit = int(limit)
        page = request.args.get('page')
        page = int(page)
        post = hanum_db.allcheck(limit=limit, page=page)
        return jsonify({"pageCount":page,"post": post}) # db에 있는 내용을 json으로 보내는 과정에서 대괄호[]로 보내지는 현상 (수정)
            
    
    elif request.method == 'POST': # post로 db에 값 넣기 기능 구현 완료
        posts = request.get_json()
        
        if len(posts) == 0:
            return 'No post' # 비었는데도 db에 올라가는 현상을 (수정)
        else:
            author = posts['author']
            pwd = posts['password']
            content = posts['content']
            title = posts['title']
            now = datetime.now()
            now = now.isoformat()
            hanum_db.insert_db(author=author, pwd=pwd, content=content, title=title, datetime=now)
            id = hanum_db.last_id()
            return jsonify({"id":id}) # post 보낼때 null값 나오는거 수정해야됨 (수정완료)
    
        
@app.route('/posts/<postID>', methods=['GET']) # get으로 특정 postID 값 가져오기 기능 구현 완료
def god(postID):
        postID = int(postID)
        pooost = hanum_db.check(postID)
        return jsonify({"post":pooost})
        

@app.route('/posts/<postID>', methods=['DELETE']) # delete 기능 구현 완료
def delete(postID):
    postID = int(postID)
    get_pwd = request.args.get('password')
    db_pwd = hanum_db.check_pw(postID)
    if get_pwd == db_pwd:
        hanum_db.del_db(postID) # db에서 postID가 진짜로 사라졌는 체크하고 ok 보내기 (수정)
        return jsonify({"ok":True})
    else:
        return jsonify({"ok":False})

if __name__ == '__main__':
   app.run(debug = True)