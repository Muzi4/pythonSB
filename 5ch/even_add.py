while True:
    a = int(input("input value : "))
    if a == 'q':
        break
        print("exit")
    else:
        if a % 2 == 0:
            print("a는 짝수 입니다.")
        else:
            print("a는 홀수 입니다.")