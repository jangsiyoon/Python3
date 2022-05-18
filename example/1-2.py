## 문자열 자료형
## 문자열을 만드는 방법 " ", ' ', ''' ''' 등.

## 문자열 안에 작은따옴표(') 포함 

import weakref


food = "Python's favorite food is perl"
print(food)

## 문자열 안에 큰따옴표 포함

say = '"Python is very easy." he says'
print(say)

## 백 슬래시 사용 \ (이 다음 오는건 기호의 의미가 아니라 문자라는 의미.)

example = 'jangsiyoon\'s the \"very good\"'
print(example)

## 여러 줄인 문자열을 변수에 대입하고 싶을 때

multiline = "Life is too short\nYou need python" # 가독성 안 좋음.
print(multiline)

multiline ='''
    Life is too short
    You need python3
    Happy is too short
'''
print(multiline)

## 이스케이프 코드 (프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합") 
## ex) \n \t \b 

## 문자열 곱하기 더하기, 곱하기

# 더하기
head = "Python"
tail = " is fun!"
print(head+tail)

# 곱하기
a = "Python3 "
print(a*3)

# 응용
print("="*50)
print("\t My Program")
print("="*50)

## 문자열 길이 구하기
a = "Life is too short"
b = len(a)
print(b)

## 문자열 인덱싱과 슬라이싱 

# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[13],a[-1],a[-2])

# 문자열 슬라이싱
print(a[0:4])
print(a[0:])

# 슬라이싱으로 문자열 나누기(현업에서 사용 하는 방법.)
example = "20220519Rainy"
date = example[:8]
weather = example[8:]
year = example[:4]
day = example[4:8]

print(date, weather, year, day)

# 중간에 문자 삽입 하는 방법

a = "Pthon3"
a = a[:1] + "y" + a[1:]
print(a)

## 문자열 포매팅 

print("I eat %d apples." % 3) # 숫자 대입
print("I eat %s apples." % "five") # 문자열 바로 대입

# 2개 이상의 값 넣기

number = 10
day = "three"
says = "u ate %d apples. so I was sick for %s days." % (number, day) 
print(says)

''' 문자열 포맷 코드
 %s 문자열 
 %c 문자 
 %d 정수
 %f 실수
 %o 8진수
 &x 16진수
'''

## 위에서 보았듯이 %d, %s등의 포맷 코드는 문자열 안에 어떤 값을 삽입하기 위해 사용한다. 하지만 포맷 코드를 숫자와 함께 사용하면 더 유용하게 사용할 수 있다.

# 1. 정렬과 공백
example = "%10s" %"hi"
print(example)

# 2. 예제
print("=" * 50) 
print("{0:^50}".format("My programing")) # 가운데 정렬 가능.
print("=" * 50)

# 3. 소수점 표현 하기

pi = 3.141542882222222
print("%15.4f" % pi)

## fomat 함수를 사용한 포매팅, 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다. 

print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))
print("I eat {0} apples.".format(3.14))

# 1. 2개이상의 값 넣기.
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# 2. 이름으로 넣기 가능.

# 3. 졍렬
print("{0:<10}".format("Hi")) # 총 자릿수 10
print("{0:>10}".format("Hi")) # 오른쪽 정렬
print("{0:^10}".format("Hi")) # 가운데 정렬 

## 문자열 관련 함수들 

# 1. 문자 개수 세기(count)
a = "hobby"
print(a.count('b'))

# 2. 위치 알려 주기(find)
a = "Python is the best choice"
a.find('y')
a.find('k') # 문자 존재 하지 않을 경우 -1 반환.

# 3. 문자열 바꾸기
a = "Life is too short"
a = a.replace("Life", "Your leg")
print(a)

# 4. 문자열 나누기
a = "Life is too short"
AList = a.split()
b = "a:b:c:d"
BList = b.split(':')

print(AList,BList)

