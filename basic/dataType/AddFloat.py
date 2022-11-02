a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)
# 컴퓨터가 실수를 정확히 표현하지 못함

a = 0.3 + 0.6
print(round(a,4))

if round(a,4) == 0.9 :
    print(True)
else :
    print(False)

# 따라서, round() 함수를 이용해서 소수점 특정 자릿수에서 반올림하여 비교