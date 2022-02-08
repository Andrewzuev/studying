import random 
numbers = random.randint(1,100)
def input_user():
    pass

print('Загадайте любое число, от 1 до 100. А я попробую отгадать')
print(numbers) 
input_user = input("Если нет, то больше или меньше? ")
#input = input_user: 
while True:
    if input_user == "да":
        print('Ураааа. у меня получилось.Спасибо за игру! ')
        break
    elif input_user == "меньше":
        print(random.randrange(1,numbers))
    elif input_user == "больше":
        print(random.randrange(numbers, 100))

