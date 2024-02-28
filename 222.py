list1 =[30, 18, 49, 53, 51, 54, 69, 63, 79, 110, 26, 62, 51, 42, 78, 34]
sum = 0
for i in list1:
    # print(i*(i-1))
    # sum += i*(i-1)*3+i*3
    sum += (i-1)*i*3+i*3*2
    print(sum)

print(sum)

