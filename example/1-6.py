## 집합 자료형

## 집합 자료형 생성 방법.(set)

from tokenize import triple_quoted


s1 = set([1, 2, 3])
s2 = set("hello")

print(s2)
''' 집합 자료형의 특징
1. 중복을 허용하지 않는다.
2. 순서가 없다. -> 인덱싱 불가능.
3. set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환후 해야 한다.
'''

# 1. set자료형 변환

l1 = list(s1)
t1 = tuple(s1) 

# 2. 교집합, 합집합, 차집합 구하기.

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2) # 교집합
print(s1 | s2) # 합집합 
print(s1 - s2) # 차집합

# 3. 값 추가 방법 (1개 : add 여러개 : update 특정값 제거 : remove)

