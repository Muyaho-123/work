print("let's go game")

# if 1이면 간다 2면 안간다

my = 1
#여기를 짤라낸다
def login(my):
 
    if my == 1:
        print("true")

    else:
        print("false")



# 돈을 넣으면 2배가 뻥튀기

m = 1000
def coin(m):
    return m *2

mym = coin(1000)
print("내돈은 {0}". format(mym))

# 맞냐 틀렸냐

def ck_idpw(ret):
    #if id == 'a' and pw == '123':
    if ret != None:
        return '로그인 성공!!@'
    else: 
        return '가입 되지 않은 아이디나 패스워드.'