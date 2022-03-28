sum = 0

desk = int(input("1. 입력할 수식 계산 2. 두 수 사이의 합계 : "))
if desk == 1:
    a = input("수식을 입력 하세요 : ")
    result = eval(a)
    print(result)
elif desk == 2:
    a = int(input("첫 번쨰 숫자를 입력 하세요 : "))
    b = int(input("두 번재 숫자를 입력 하새요 : "))
    for i in range(a, b):
        sum += i
    print("%d +...+ %d = %d 입니다.", a, b, sum)





# a = input('input expression : ')
# result = eval(a)
# print(result)