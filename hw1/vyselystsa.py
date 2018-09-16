import random
def choose_word(num):
    if num == 1:
        with open ("games.txt", encoding = "utf-8") as f:
            a = f.read()
            a = a.split("\n")
            a = random.choice(a)
            return a
    elif num == 2:
        with open ("elements.txt", encoding = "utf-8") as f:
            a = f.read()
            a = a.split("\n")
            a = random.choice(a)
            return a
    elif num == 3:
        with open("scientists.txt", encoding="utf-8") as f:
            a = f.read()
            a = a.split("\n")
            a = random.choice(a)
            return a
    else:
        print("Недопустимый ввод, слово выбрано случайно")
        with open("scientists.txt", encoding="utf-8") as f:
            a = f.read()
            a = a.split("\n")
            a = random.choice(a)
            return a

cat = input("Выберите одну из категорий:\n(1) Карточные игры\n(2) Химические элементы\n(3) Фамилии математиков\n")
word = choose_word(int(cat))
print ("На то, чтобы угадать слово из ",len(word)," букв, у вас есть 7 попыток.")
print("     +---+\n     |   |\n         |\n         |\n         |\n         |\n =========\n")
lifes = 7
right = []
wrong = []

while True:
    for i in word:
        if i in right:
            print (i, end = "")
        else:
            print ("_", end = "")
    print("\n")
    letter = input("Введите букву в нижнем регистре: ")
    if letter in right or letter in wrong:
        print("Вы уже пробовали эту букву ранее.")
    if letter in word and letter not in right:
        print("Вы угадали, такая буква есть!")
        right.append(letter)
        flag = 1
        for i in word:
            if i not in right:
                flag = 0
        if flag == 1:
            print ("Поздравляю, вы угадали слово ",word,"!")
            break
    elif  letter not in word and letter not in wrong:
        if letter not in "йцукенгщзхъфывапролджэячсмитьбю":
            print ("Неккоректный символ!")
        lifes -= 1
        wrong.append(letter)
        if lifes in (5,6,0):
            print ("Вы не угадали, осталось ", lifes, " попыток.")
        elif lifes == 1:
            print ("Вы не угадали, осталась ", lifes, " попытка.")
        else:
            print ("Вы не угадали, осталось ", lifes, " попытки.")
        if lifes == 6:
            print("     +---+\n     |   |\n     0   |\n         |\n         |\n         |\n =========\n")
        elif lifes == 5:
            print("     +---+\n     |   |\n     0   |\n         |\n         |\n         |\n =========\n")
        elif lifes == 4:
            print("     +---+\n     |   |\n     0   |\n    /    |\n         |\n         |\n =========\n")
        elif lifes == 3:
            print("     +---+\n     |   |\n     0   |\n    / \  |\n         |\n         |\n =========\n")
        elif lifes == 2:
            print("     +---+\n     |   |\n     0   |\n    /|\  |\n         |\n         |\n =========\n")
        elif lifes == 1:
            print("     +---+\n     |   |\n     0   |\n    /|\  |\n    /    |\n         |\n =========\n")
        elif lifes == 0:
            print("     +---+\n     |   |\n     0   |\n    /|\  |\n    / \  |\n         |\n =========\n")
            print ("Ты проиграл, ЛОХ!!1")
            break
