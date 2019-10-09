numbers =[]
total = 0
med = 0
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
if count % 2 == 0:
    med = (numbers[count % 2]+numbers[count % 2 -1])/2
else:
    med = numbers[count // 2 +1]
print ("Всего:", count, "Сумма:",total,"Мин:",numbers[0],"Мах:",numbers[count-1],"Среднее:",total/count, "Медиана:", med)
    

