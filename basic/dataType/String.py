# 문자열 변수를 초기화할 때에는 따옴표나 쌍 따옴표를 사용
data = 'Hello World'
print(data)

# 따옴표나 쌍 따옴표를 출력하기 위해서는 백슬래쉬를 사용하면 된다.
data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)

# 문자열 변수를 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러번 더해진다.
a = "String"
print(a * 3)

# 문자열은 내부적으로 리스트와 같이 처리되므로, 리스트와 마찬가지로 인덱싱과 슬라이싱을 사용할 수 있다.
a = "ABCDEF"
print(a[2:4])