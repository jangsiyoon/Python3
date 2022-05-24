## 3장 연습문제

# 01.

import re


result = "shirt"

# 02.

number = 1
result = 0

while number <= 1000:
    if(number % 3 ==0):
        result = result + number
    number += 1
print(result)

# 03.
i = 0

while True:
    i += 1 
    if i > 5: break
    print('*' * i) # 문자열 곱하기 사용.
    

# 04.

for i in range(1, 101):
    print(i)

# 05.

Amarks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in Amarks:
    total += score

average = total/len(Amarks)
print("5번 문제 결과 값: %d " % average)



