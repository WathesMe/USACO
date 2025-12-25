#ChatGPT Milk 1

numMilk = int(input())
milkList = []

print(milkList)

while numMilk > 0:
    bob = int(input())
    milkList.append(bob)
    numMilk -= 1

current = milkList[0]
total = 0

for num in milkList:
    if num < current:
        num = current - num
        total = total + num
    if num > current:
        current = num

print(total)
