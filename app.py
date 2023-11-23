from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/posts')
def response():
    return{
       "posts" : [
           {
               "id" : 11,
               "title" : "게시글제목",
               "author" : "게시글작성자이름"
           }
       ]
   }


if __name__ == '__main__':
   app.run(debug = True)