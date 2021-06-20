import pymysql

def dpcon():
    return pymysql.connect(host='yha05223.mysql.pythonanywhere-services.com',
                   user='yha05223', password='haha1234',
                   db='yha05223$mydb', charset='utf8')
def insert_user(userid, pw, name, phone):
    try:
        db = dpcon()
        c = db.cursor()
        setdata = (userid, pw, name, phone)
        c.execute("INSERT INTO user_tb (id, pw, name, phone)VALUES (%s, %s, %s, %s )", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
            db.close()


def get_idpw(userid, pw):
    ret = ()
    try:
        db = pymysql.connect(host='127.0.0.1',
                   user='root', password='1234',
                   db='appdb', charset='utf8')

        c = db.cursor()
        setdata = (userid, pw)
        c.execute("SELECT * FROM user_tb WHERE id = %s AND pw = %s", setdata)
        ret = c.fetchone()
        #print(ret)
    except Exception as e:
        print('db error:', e)
    finally:
            db.close()
    return ret

