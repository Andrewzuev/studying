import random 
low_numbers = 1
hight_numbers = 100
numbers = random.randint(low_numbers, hight_numbers)
list_numbers = [numbers]

print('Загадайте любое число, от 1 до 100. А я попробую отгадать')
print(numbers) 
input_user = input("Если нет, то больше или меньше? ")
#input = input_user: 
while True:
    if input_user == "да":
        print('Ураааа. у меня получилось.Спасибо за игру! ')
        break
    elif input_user == "меньше":
        hight_numbers = numbers
        while numbers in list_numbers:
            numbers = random.randint(low_numbers,hight_numbers) 
            print("===>" + str(numbers))  
        list_numbers.append(numbers) 
        print(numbers)
        print(list_numbers)
        input_user = input("я угадал? ")
    elif input_user == "больше":
        low_numbers = numbers
        while numbers in list_numbers:
            numbers = random.randint(low_numbers, hight_numbers)
            print("===>" + str(numbers)) 
        list_numbers.append(numbers)
        print(numbers)
        print(list_numbers)
        input_user = input("я угадал? ")

