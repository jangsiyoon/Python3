## 2장 연습문제

# 01.
result = (80 + 75 + 55) / 3
print(result)

# 02.

'''
    2로 나누기 했을때 나머지가 0이면 : 짝수, 1이면 : 홀수
'''

# 03. 

id = "881120-1068234"
yeardate = id[0:6]
number = id[8:]

print(yeardate, number)

# 04. 

pin = "881120-1068234"
result = pin[7]

print(result)

# 05.

a = "a:b:c:d"
result = a.replace(":","#")

print(result)

# 06.

a = [1,3,5,4,2]
a.sort()
print(a)

# 07.

a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)


# 08.

t1 = (1,2,3)
t2 = (4,)
result = t1 + t2

print(result)

# 09.

'''
    2. key 값은 리스트나 튜플이 들어 갈수 없다.
    3. 리스트 
'''

# 10.

a = {'A' : 90, 'B' : 80, 'C' : 70}
result = a.pop('B') # pop하면 출력  하면서 쌍으로 제거 됨.

print(result)

# 11.

a = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5]
result = list(set(a))

print(result)

# 12.

a = b = [1, 2, 3]
a[1] = 4

print(b)

'''
    b값도 동일하게 변경 된다 -> 같은 메모리 주소를 가리키기 때문에.
'''


