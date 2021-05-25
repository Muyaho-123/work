from flask import Flask, render_template
app = Flask(__name__)

@app.route('/naver') # 루트(/)는 뿌리
def hello():
    return '안녕 나는 네이버야~'

@app.route('/b')
def hello2():
    return 'Hello, World! bbbbbbb'

# 웹브라우저에 http://127.0.0.1:5000/naver 
# 위와같이 접속 하면 안녕 나는 네이버야~
# 라는 글자를 나타나게 하시오

@app.route('/taxi')
def taxi():
    return render_template("taxi.html")




if __name__ == '__main__':
    app.run()
