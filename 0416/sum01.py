num = int(input("정수 입력 : "))
sum = 0
for i in range(1, 101):
    if i < 100:
        print(i, " + ", end="")
    else:
        print(i, " = ", end="" )
    sum += i

print(sum)

for i in range(0, 5):
    print(i)
