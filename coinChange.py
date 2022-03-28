fh = 0
oh = 0
ft = 0
ot = 0
ab = 0


num = int(input("교환할 돈은 얼마? : "))

fh = num//500
num = num%500

oh = num//100
num = num%100

ft = num//50
num = num%50

ot = num//10
num = num%10

ab = num

print("%d개"%fh)
print(oh)
print(ft)
print(ot)
print(ab)

