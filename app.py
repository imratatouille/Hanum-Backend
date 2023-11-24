from flask import Flask, render_template, request, jsonify
import hanum_db

app = Flask(__name__)

id = 0
title = ""
author = ""

post = [
    {
            "id" : id,
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
            i =+ 1
            return jsonify({"id": i})
        
if __name__ == '__main__':
   app.run(debug = True)