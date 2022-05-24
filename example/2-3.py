## for문

'''
for 변수 in 리스트(또는 튜플, 문자열)
    수행할 문장1
    수행할 문자2
'''

# 1. 예제

test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)
    
# 2. for문의 응용
# "총 5명의 학생이 시험을 보았는데 60점 이상이면 합격 아니면 불합격. -> 결과값 표시"

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격 입니다." % number)
        
# 3. continue

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)
    
    
# 4. for문과 함께 자주 사용하는 range 함수.

add = 0

for i in range(1, 11): # for i = 1 ; i ++ ; i < 11 
    add = add + i

print(add)

# 5. 60점 이상이면 합격

marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number + 1))
    
# 6. for와 range를 이용한 구구단

for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')



