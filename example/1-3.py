## 1-3 : 리스트 자료형

odd = [1, 2, 3, 4, 5]
a = ['Life', 'is', 'too', 'short']
b = [1, 2, 'Life', 'is']
c = [1, 2, ['Life','is']] # 리스트 안에는 어떠한 자료형도 포함시킬 수 있다.

print(b, c)

## 리스트 연산 하기.

# 1. 리스트 더하기.
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

# 2. 리스트 반복 하기.

a = [1, 2, 3]

print(a * 3)

# 3. 리스트 길이 구하기.

print(len(a))

# 4. 초보자가 범하기 쉬운 실수 (형변환)

a = [1, 2, 3]
print(str(a[2]) + "Hi") # 리스트 안의 1,2,3 은 정수 즉 문자열과 더하기 할 수 없다.

## 리스트의 수정과 삭제

# 1. del 함수 사용해 리스트 요소 삭제 하기.

odd = [1, 2, 3]
del odd[1]

print(odd)

## 리스트 관련 함수들

# 1. 리스트에 요소 추가(append) - 마지막에 추가 하는 함수

a = [1, 2, 3]
a.append(4)

print(a)

# 2. 리스트 정렬(sort)

odd = [1, 4, 3, 2]
odd.sort()

print(odd)

# 3. 리스트 뒤집기(reverse)

odd = ['a','b','c']
odd.reverse()

print(odd)

# 4. 위치 반환
odd = [1 ,2 ,3]

print(odd.index(3))

# 5. 리스트에 요소 삽입 및 삭제

odd = [1 ,2 ,3]

odd.insert(0,4)
odd.remove(4)

print(odd)
