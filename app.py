from flask import Flask, render_template, request, jsonify
import hanum_db

app = Flask(__name__)

page = hanum_db.all_idcheck()

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/posts', methods=['GET','POST'])
def postit():
    if request.method == 'GET':
        post = hanum_db.check()
        return jsonify({"post": post}) # db에 있는 내용을 json으로 보내는 과정에서 대괄호[]로 보내지는 현상 수정
    elif request.method == 'POST':
        posts = request.get_json()
        if len(posts) == 0:
            return 'No post' # 비었는데도 db에 올라가는 현상을 수정해야함
        else:
            author = posts['author']
            pwd = posts['password']
            content = posts['content']
            title = posts['title']
            hanum_db.insert_db(author=author, pwd=pwd, content=content, title=title)
            id = hanum_db.idcheck()
            return jsonify({"id":id}) # post 보낼때 null값 나오는거 수정해야됨 (수정완료)
        
@app.route(f'/posts/{page}')
def mola():
    return("hi this page is")
        
if __name__ == '__main__':
   app.run(debug = True)