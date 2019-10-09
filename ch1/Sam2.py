numbers =[]
total = 0
while True:
    line = input("Enter a number or Enter to finish:")
    if line:
        try:
            numbers.append(int(line))
        except ValueError as err:
            print(err)
            continue
    else:
        break
numbers.sort()
count = len(numbers)
for i in numbers:
    total += i
print ("Всего:", count, "Сумма:",total,"Мин:",numbers[0],"Мах:",numbers[count-1],"Среднее:",total/count)
    

