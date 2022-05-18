## 프로그램의 구조를 쌓는다 !. (제어문)

## if문 

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

