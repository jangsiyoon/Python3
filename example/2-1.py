## 프로그램의 구조를 쌓는다 !. (제어문)

## if문 

from email import message


money = 2000

if money >= 3000:
    print("택시를 타고 간다.")
else:
    print("걸어가라.")
    
'''
    조건문에 사용되는 비교연산자
    < 
    >
    ==
    !=
    >=
    <=
'''

## 1. and, or, not 

# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."

money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 2. x in s, x not in s : s에 리스트, 튜플, 문자열 가능

# 예제.

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
    
# 3. elif 사용 예제

pocket = ['paper', 'cellphone']
card = True 
if 'money' in pocket:
    print("택시를 타고 가라")
elif card == True:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
## 조건부 표현식

score = 60

message = "success" if score >= 60 else "failure"
print(message)




    