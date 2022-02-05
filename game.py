import random

print('Привет, вы вошли в игру "Отгадай число". \nЯ загадываю число от 1 до 100, а вы попробуете отгадать. \nПоехали' )
number = random.randint(1,100)
guess = int(input('Ваше предположение:....? '))
attempt = 1
while True:   
    if guess == number:
        print('Поздравляяяяяем!!!!! \nВы угадали. \nЭто действительно число', number)
        print('Вам понадобилось ', attempt, 'попыток')
        break
    elif guess < number:
        print('больше')
    else:
        print('меньше')
    guess = int(input('Ваше предположение:....? '))
    attempt += 1

    if attempt > 5:
        print('Вы использовали слишком много попыток. Удачи в следующий раз. ')
        break
        
#print('Поздравляяяяяем!!!!! \nВы угадали. \nЭто действительно число', number)
#print('Вам понадобилось ', attempt, 'попыток')