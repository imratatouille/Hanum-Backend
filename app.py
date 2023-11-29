from flask import Flask, request, jsonify
import hanum_db
from datetime import datetime

app = Flask(__name__)

@app.route('/posts', methods=['GET', 'POST'])
def manage_posts():
    if request.method == 'GET': # request.method가 get일때 limit, page의 args값을 받고 page랑 posts를 반환
        limit = int(request.args.get('limit', 10))
        page = int(request.args.get('page', 1))
        posts = hanum_db.get_posts_page(page=page, limit=limit)
        return jsonify({"pageCount": page, "posts": posts})
    elif request.method == 'POST': # request.method가 post일때 json값을 받고 id부여하고 db에 저장
        post_data = request.get_json()
        author, pwd, content, title = post_data['author'], post_data['password'], post_data['content'], post_data['title']
        now = datetime.now().isoformat()
        if len(author) == 0:   # |
            return 'No post'   # |
        elif len(pwd) == 0:    # |
            return 'No post'   # => author, pwd, content, title의 값이 0이면 'No post'를 return
        elif len(content) == 0:# |
            return 'No post'   # |
        elif len(title) == 0:  # |
            return 'No post'   # |
        hanum_db.insert_post(author=author, pwd=pwd, content=content, title=title, datetime=now)
        post_id = hanum_db.last_post_id()
        return jsonify({"id": post_id})

@app.route('/posts/<int:postID>', methods=['GET', 'DELETE']) # get => 고유postid값 받고 return
def manage_post(postID):                                     # delete => 고유postid값 받고 pw값 비교후 삭제
    if request.method == 'GET':                              # pw가 틀리면 false 맞아서 삭제되면 true 
        post = hanum_db.get_post(postID)
        return jsonify(post)
    elif request.method == 'DELETE':
        get_pwd = request.args.get('password')
        db_pwd = hanum_db.get_post_password(postID)
        if get_pwd == db_pwd:
            result = hanum_db.delete_post(postID)
            return jsonify({"ok": result})
        else:
            return jsonify({"ok": False})

@app.route('/posts/<int:postID>/comments', methods=['POST']) # 고유 postid값 받고 comment하면 받은 postid에 comment가 달림
def add_comment(postID):
    comment_data = request.get_json()
    author, pwd, content = comment_data['author'], comment_data['password'], comment_data['content']
    post_id = hanum_db.get_post_by_id(postID)
    now = datetime.now().isoformat()
    if post_id == [{'id': postID}]:
        hanum_db.insert_comment(author=author, pwd=pwd, content=content, postid=postID, now=now)
        comment_id = hanum_db.last_comment_id()
        return jsonify({"commentId": comment_id})
    else:
        return jsonify({"commentId": False})

@app.route('/posts/<int:postID>/comments/<int:commentID>', methods=['DELETE']) # db에 있는 comment-pw랑 받은 comment-pw값이 같으면 delete
def delete_comment(postID, commentID):
    get_id = hanum_db.get_post_by_id(postID)
    get_pwd = request.args.get('password')
    db_pwd = hanum_db.get_comment_password(commentID)
    if get_id == [{'id': postID}]:
        if get_pwd == db_pwd:
            result = hanum_db.delete_comment(commentID)
            return jsonify({"ok": result})
        elif get_pwd != db_pwd:
            return jsonify({"ok": "pw_Fail"})
        else:
            return jsonify({'ok': "another_Fail"})
    else:
        return jsonify({"ok": "id_Fail"})

if __name__ == '__main__':
    app.run(debug=True)