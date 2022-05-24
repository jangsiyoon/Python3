## while문

''' 
while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
'''

# "열 번 찍어 안 넘어가는 나무 없다."

treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        
        
# 1. while문 만들기

prompt ='''
1. Add
2. Del
3. List
4. Quit

Enter number:
'''

number = 0
while number != 4:
    print(prompt)
    number = int(input())
    

# 2. 커피 자판기 프로그램

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    

# 3. while문의 맨 처음으로 돌아가기(continue)

a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0 : continue
    print(a)
    

## 항상 while문의 경우에는 무한루프를 조심해서 사용해야 한다.

