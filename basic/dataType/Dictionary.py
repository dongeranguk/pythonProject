# 사전 자료형은 키와 값의 쌍을 데이터로 가지는 자료형 (= Map)
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# 사전 자료형에 특정한 원소가 있는지 검사할 때에는 '원소 in 사전'의 형태를 사용한다.
if '사과' in data :
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

