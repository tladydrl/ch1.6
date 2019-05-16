# 다양한 파일 입출력 함수

f = open('text.txt', 'w', encoding='utf-8')
f.write('안녕하세요\n둘리입니다.')
f.close()

f = open('text.txt', 'r+t', encoding='utf-8') # 바이너리 로 열면,, 바이너리로 '고'를 바꿔야됨.
text = f.read()
print(text)
#f.close() # 닫고열면 처음포지션.

pos = f.tell() # 파일 포지션은 바이트 단위로 나온다.
print(pos)  # 마지막 바이트의 다음번째이다...

# position을 이동시키고 다시 읽기..
f.seek(17)  # 맨 앞에서 몇 바이트 뒤로 이동/,, 한글이면 3바이트,, 잘 이동시켜야 한다. 잘리지 않게..
# 여기가 둘 자시작이다.
f.write('고')
f.seek(0)

#text = f.read()
print('aa')
text = f.read()
print('----' + text + '----')  # 두번째는 안나온다.. #개행까지 읽어버렸다.
f.close()

# a 는 파일 끝에 붙이나 보다.. 필요하면 찾아보자..

# 라인단위로 읽기
line_num = 0
f2 = open('fileio2.py', 'rt', encoding='utf-8') #롸잇 텍스트 ,, 엔코딩
while True:
    line = f2.readline()  # 한 라인씩..
    if line == '':  # 빈 문자열이면 끝나는것이다.
        f2.close() #클로즈 했네..
        break
    line_num += 1
    print("{0}: {1}".format(line_num, line), end='') # 개행까지 나오니까,, 개행으ㅏㄹ 없애기
#f2.close()

with open('fileio2.py', 'rt', encoding='utf-8') as f4:  # 위드오픈 하면 블록하면,, 끝나고
    for line_num, line in enumerate(f4.readlines()):
        print("{0}: {1}".format(line_num, line), end='')

print('\n', f4.closed) # closed 는 함수가 아니라 객체의 변수값이네..

#f3.close()

#for line


  # 여기는 개행이 있다.
 #아무것도 없다.

 # 파이썬 파일 하나를 모듈..
 # 모듈을 모아서 패키지라 하고,..
 # 변수 정의,, 함수정의, 클래스 정의/..,.
 # 심볼테이블 글로벌테이블,,
 # 임포트 해서 호출할 수 있다.
 # ~.py 파일이다.
 # 다른파일에서 쓰고싶으면,, import ~.py 하면 ,, 똑같이 더해졌다  하면됨,, ~.py 실행되고 이거 실행..

 # def f():
    #--- ---- ---

#f()..
# f 함수 변경되면 다 고쳐야 되는데,,
# ~.py 에만 f 정의해놓으면,, ~.py 파일만 바꿔서 나머지에서는 import 하면 자동으로 다 된다.
# f.py 라면,, f.f() 하면,.. 유지보수 편하게..



