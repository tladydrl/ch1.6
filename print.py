# print() 연습
import sys
print(1)
print('hello', 'world')

x=0.2
s = 'hello world'

# sep, end 키워드 파라미터 지정하기

print(x, s, sep=',')
print(str(x) + ',' + s)

print(x, s, sep=',', end='')  # 개행을 없앰..
print('-----')
# sep end 안쓰면,,,

print(sep=' ', end = '\n')  # 디폴트

# file 파라미터를 지정할 수 있다.
print('Hello World', file=sys.stdout) # 파일로 출력,, # file=sys.stdout는 생략되있음.
# 표준출력: 콘솔로 나타남.
# 에러 : stderr , ,# stdout 은 프린트랑 같다.

print('error: hello world', file= sys.stderr)  # 에러 먼저 실행이 된다. 1출력 뒤에 실행이 되네..

#file 출력
f = open('hello.txt', 'w')
print('Hello world', file=f)
sys.stdout.write('Hello World') # 이것보다 프린트가 낫다..  #

# stdin은 키보드 입력..


















