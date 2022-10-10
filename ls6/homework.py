sum = 0
for i in range(1, 1001):
    if i%3==0 and i%5==0 and i%7==0:
        sum += i
    print(i)
print(sum)

print("_____________")

sum = 0 

for i in range(105, 1001, 105):
    sum += i
    print(i)
print(sum)