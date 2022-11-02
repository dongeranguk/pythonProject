# 리스트 초기화 방법
array = []
for i in range(20) :
    if i % 2 == 1 :
        array.append(i)
print(array)

# 리스트 초기화 방법2 (= 리스트 컴프리헨션)
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 둘의 결과는 같지만, 리스트 컴프리헨션을 사용했을 때 소스코드가 더 간결해진다.

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# 2차원 리스트를 초기화할 때에는 반드시 리스트 컴프리헨션 사용
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)
# array[1][1]의 값을 바꾸고 싶었지만, 3개의 리스트에서 인덱스 1에 해당하는 원소들의 값이 모두 5로 바뀜
# 이는 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문

array = [[0] * m for _ in range(n)]
array[1][1] = 5
print(array)
# 리스트 컴프리헨션을 사용하면, 바꾸고자 한 array[1][1]의 값을 바꿀 수 있다.
