from flask import Flask, render_template, request, jsonify
import hanum_db

app = Flask(__name__)

title = ""
author = ""

post = [
    {
            "id" : 1,
            "title" : f"{title}",
            "author" : f"{author}"
        }
]

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/hello, world!')
def hello():
    if 1 == 1:
        return("perpect")
    else:
        return("error")

@app.route('/posts', methods=['GET','POST'])
def postit():
    if request.method == 'GET':
        return jsonify({"post": post})
    elif request.method == 'POST':
        posts = request.get_json()
        if len(posts) == 0:
            return 'No post'
        else:
            author = posts['author']
            pwd = posts['password']
            content = posts['content']
            title = posts['title']
            hanum_db.insert_db(author=author, pwd=pwd, content=content, title=title)
            id = hanum_db.idcheck()
            return jsonify({"id":id}) # post 보낼때 null값 나오는거 수정해야됨
        
if __name__ == '__main__':
   app.run(debug = True)