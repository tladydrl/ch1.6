#
# write test
#

# text 모드가 default : wt    # 텍스트 모드가 디폴트니까 wt 를 w로 생략할수 있다.
f = open('text.txt', 'w', encoding='utf-8')  # 쓰기,, wt  # 텍스트를 한자씩 받아서 인코딩하나보다..
write_size = f.write('안녕하세요\n둘리입니다.')  # 텍스트 모드.. t 는 텍스트모드/  #텍스트 하나씩 받음.
 # 리턴: 쓴 바이트 리턴한다.  \n 는 1바이트,, . 1바이트 한글: 3바이트.

print(write_size)  # 12 글자,,, 캐릭터 수만 나오네,, 바이트는 32바이트인데.
# 파이썬 utf-8 ,,

# 바이너리 모드..  : wb

f = open('test2.txt', 'wb')  #

#bytes('안녕하세요\n둘리입니다.', encoding='utf-8') #이러면 바이트 배열로 나온다.
write_size = f.write(bytes('안녕하세요\n둘리입니다.', encoding='utf-8')) #문자열을 바이트로 바꿔줌,, #1바이트로 받음..
f.close()   # 캐릭터를 바이트로 바꾼다.
print(write_size)

#
# read test
#
f = open('text.txt', 'r', encoding='utf-8') # 바이트를  # f.read()는 객체함수이다..
text = f.read()  # 텍스트를 받는다.
f.close()
print(text)

#
# copy binary file
#

f_src = open('python.png', 'rb')  # 바이트로 읽는다.
data = f_src.read()
f_src.close()

print(type(data))  # 스트링은 캐릭터로,,, 바이츠는 바이트 버퍼로,,

f_dest = open('python2.png','wb')
f_dest.write(data)
f_dest.close()

f = open('text.txt','w', encoding='utf-8')
write_size = f.write('가나다라.') #문자열을 바이트로 바꿔줌,, #1바이트로 받음..
f.close()   # 캐릭터를 바이트로 바꾼다.
print(write_size)



