# 반복문
#   1. for      -> 반복 횟수를 아는경우
#   2. while    -> 반복 횟수를 모르는 경우

# 컬렉션과 함께 자주 사용!
#   -> 컬렉션의 길이만큼 반복
for num in [1, 2, 3]:
    print(num)
    
# range(시작:끝:인터벌)
# range(1,5,1)  -> 1, 2, 3, 4
# range(1,5)    -> 1, 2, 3, 4 (인터벌 생략: 1)
# range(1,5,2)  -> 1, 3
# range(7)      -> 0, 1, 2, 3 , 4, 5, 6 (시작 생략)

# 1 ~ 10 까지 출력
for num in range(1, 11):
    print(num)
    
# 반복 횟수 인덱스를 사용 하고 싶은 경우
#   -> enumerate()를 사용하면 인덱스 사용 가능
a = ['A', 'B', 'C']
for i, val in enumerate(a):
    print(i, val)
    
# 구구단 2단
# 2x1=2
# ...
# 2x9=18

for i in range(1, 10):
    print(f"2x{i}={i*2}")
    
# 숙제  
#   중첩 for 문을 사용해서 구구단 2단부터 9단까지 출력하는 코드 작성
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")
        
# while 반복문
#   - 반복 횟수를 모르는 경우
#   - 조건이 만족하는 동안 계속 반복
#   - 조건 True     -> 반복
#   - 조건 False    -> 반복종료
#   - while 조건에 True 명시하면 -> 무한 Loop
#     (break문과 함꼐 사용)

#  * for, while 반복문에서 사용할 수 있는 키워드
#   1. break    : 즉시 반복문을 빠져 나오세요(반복문 종료)
#   2. continue : 즉시 다음 반복으로 넘어가세요

while True:
    if True:
        break

"""
while 조건:
    code
"""
# 숙제: for 문으로 작성한 구구단 2단 코드를 while 문으로 변경하세요
# for i in range(1, 10):
#     print(f"2x{i}={i*2}")
n = 1
while n < 10:
    print(f"2x{n}={n*2}")
    n += 1