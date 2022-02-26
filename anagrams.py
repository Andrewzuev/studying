# Анаrраммы (Word JumЬle)
#
# Компьютер выбирает какое-либо слово и хаотически переставляет его буквы 
#Задача иrрока - восстановить исходное слово

import random
from turtle import position
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
HINTS = ("Есть вид таких змей ", "В какую игру мы играем сейчас?: ",
        "Антоним к слову 'сложная': ", "Можно описать, как 'трудная': ",
        "Вопрос - ...... ", "Место, куда можно поставить стакан: ")
points = 0
used_words = []



def make_anagramm(word):
    jumble = ''
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return jumble    

def guess_word(word):
    correct = word
    jumble = make_anagramm(word)
    hint = HINTS[WORDS.index(correct)]
    hint_flag = 0
    
    print("Boт анаграмма:", jumble)
    guess = input("\nПопробуйте отгадать исходное слово: ")

    while guess != correct:
        if guess == 'h':
            print(hint)
            guess = input("Попробуйте огадать еще раз: ")   
            hint_flag = 2
        elif guess == "":
            print("Программа завершена.")
            exit(256)
        else:
            guess = input("Попробуйте огадать еще раз: ")

    if guess == correct:
        print("Дa. Именно так! Вы отгадали!\n")
        return 3 - hint_flag
        
# начало игры
print(
'''
        Добро пожаловать в игру 'Анаграммы'!
Надо переставить буквы так, чтобы получилось осмысленное слово.
У вас, будет возможность попросить подсказку.Что бы посмотреть подсказку, нажмите "h". 
При этом, вы заработайте всего лишь 1 балл.
Если отгадаете без подсказки, получите 3 балла.
(Для выхода нажмите Enter. не вводя своей версии.)
'''
)

while WORDS:
    position_word = random.randrange(len(WORDS))
    used_words += WORDS[position_word]
    input = guess_word
    WORDS = WORDS[:position_word] + WORDS[(position_word + 1):]
    
    

    




#for word in WORDS:
#    points += guess_word(word)

print("Cnacибo за игру.")
print("Вы заработали: ", points, "балла\ов.")
input("\n\nHaжмитe Enter. чтобы выйти.")
