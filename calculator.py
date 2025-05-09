a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
action = input("Введите + или - либо / либо *")

if action == "+":
    result = a + b
elif action == "-":
    result = a - b
elif action == "/":
    result = a / b
elif action == "*":
    result = a * b
else:
    print("Неверное действие")
    
print(result)

if result % 2 == 1:
    print("Число не четное")
else:
    print("Число четное")

if result > 25:
    print("огурец")
else:
    print("помидор")

if result > 50:
    print("Колбаски")
else:
    print("чечевица")

if result > 100 and result %5==0:
    print("action camera")

if result > 2 and result < 10:
    print("чашка чая")

if result < 5 or result >100:
    print("утюг")

    

    
