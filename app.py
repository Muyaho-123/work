from flask import Flask, render_template, request, session, redirect
from func import ck_idpw 
import db

app = Flask(__name__)
app.secret_key = b'aaa!111/'


@app.route('/') 
def travel():
    return render_template('travel.html')

@app.route('/now')
def now():
    return render_template("now.html")

@app.route('/CA')
def CA():
    return render_template("CA.html")

@app.route('/ND')
def ND():
    return render_template("ND.html")    

@app.route('/NE')
def NE():
    return render_template("NE.html")    

@app.route('/NW')
def NW():
    return render_template("NW.html")    

@app.route('/NY')
def NY():
    return render_template("NY.html")    

@app.route('/PA')
def PA():
    return render_template("PA.html")    

@app.route('/login')
def login():
    return render_template("login.html")    


@app.route('/jo') 
def jo():
    return render_template("jo.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/join_action',methods=['GET', 'POST'])
def join_action():
    if request.method == 'GET':
        return "다시 로그인 하세요."
    else:
        userid = request.form['userid']
        pwd = request.form['pwd']
        name = request.form['name']
        phone = request.form['phone']
        print(userid, pwd, name, phone)
        
        db.insert_user(userid, pwd, name, phone)
        return '회원가입 성공.'


@app.route('/jo',methods = ['GET','POST'])
def jo():
    if request.method == 'GET':
        return render_template('jo.html')
        
    else:
        ID = request.form['ID']
        PW = request.form['PW']
        if ck_idpw(ID, PW):
            return '반갑습니다.'
        else:
            return '다시 로그인하세요.'






@app.route('/action_page',methods=['GET', 'POST'])
def action_page():
    if request.method == 'GET':
        return "나는 액션 GET페이지야"
    else:
        search = request.form['search']
        return '''당신은 '{}'로 검색을 했습니다.<br>
        결과를 보여드리겠습니다. 잠시만 기다려주세요!<br>
        리스크쫙~~~
        '''.format(search)

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
        
    else:
        userid = request.form['userid']
        pwd = request.form['pwd']
        print(userid,'pwd')
        ret = db.get_idpw(userid, pwd)
        if ret != None:
            session['user'] = ret[3] #로그인 처리함
        return ck_idpw(ret)
        if 'qu' == '123' and 'qe' == '456':
            return '안녕하세요 어서오세요'
        else:
          return '다시 로그인하세요'

if __name__ == '__main__':
    app.run()
