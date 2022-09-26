import random
def get_word(spisok):
    spisok = spisok.split(',')
    word = random.choice(spisok).lower()
    return word.lstrip()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play():
    r_word = get_word(word_list)
    print('''*** Давайте играть в угадайку слов! ***\nУ Вас имеется 6 попыток для прохождения игры.
Вам предстоит угадать случайное слово. Тема: "Канцелярские принадлежности". 
Все предметы представлены в единственном числе. Язык ввода - русский!!!\n''')
    tries = 6
    word_completion = '_' * len(r_word)
    guessed_letters = []  # список уже названных букв
    print('Случайное слово:', word_completion)
    while tries != 0:
        display_hangman(tries)
        while True:
            letters = input('Введите букву или слово целиком: ').lower()
            if letters.isalpha() and len(letters) == 1 and letters in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
                if letters not in guessed_letters:
                    guessed_letters += letters
                    break
                else:
                    print('Ошибка ввода. Символ был введен ранее. Повторите попытку еще раз.')
                    continue
            elif letters == r_word:
                break
            elif len(letters) != len(r_word):
                break
            else:
                if letters.isalnum():
                    if letters.isalpha() and letters in 'abcdefghijklmnopqrstuvwxyz':
                        print('Ошибка ввода. Необходимо изменить язык ввода.Повторите попытку.')
                    else:
                        print('Ошибка ввода. Введен недопустимый символ. Повторите попытку')
                elif letters in '!@#$%^&*()_+/.,<>?][{}':
                    print('Ошибка ввода. Недопустимый символ. Повторите попытку.')
                else:
                    print('Ошибка ввода. Буква была введена ранее. Повторите попытку.')
        ss = [i for i in word_completion]
        if len(letters) == 1:
            if letters in r_word:
                for i in range(len(r_word)):
                    if r_word[i] == letters:
                        ss.insert(i, letters)
                        del ss[i + 1]
                word_completion = ss
                if ''.join(word_completion) == r_word:
                    print('\nВы угадали слово!!!')
                    break
                else:
                    print('\nВы угадали букву!\n', *ss, '\nУ вас осталось', tries, 'попыток.')
            elif letters not in r_word:
                tries -= 1
                print('\nВы не угадали. У Вас осталось', tries, 'попыток.')
                print(display_hangman(tries))
        elif 1 < len(letters) < len(r_word) or len(letters) > len(r_word):
            tries -= 1
            print('\nСлово введено не верно. Повторите ввод.\n У Вас осталось', tries, 'попыток.')
        else:
            if letters == r_word:
                print('\nВы угадали слово!!!')
                break
    if (''.join(word_completion) == r_word and tries != 0) or letters == r_word:
        print('\n!!!',r_word, '!!!\n', 'Поздравляем! Вы выиграли.\n')
    else:
        print('\n!!!', r_word, '!!!\n', 'Вы програли.\n')
    while True:
        choice = input('''Желаете сыграть еще раз?
        Если "Да" - введите 1.
        Если "Нет" - введите 0.'
        Ваш выбор - ''')
        if choice == '1':
            print()
            play()
        elif choice == '0':
            print('Конец игры!')
            break
        else:
            print('\nОшибка ввода. Повторите свой выбор.')


word_list = '''ручка, карандаш, маркер, папка, стикер, калькулятор, штамп, степлер, дырокол, ножницы, календарь, 
блокнот, скотч, клей, корректор, ластик, точилка, линейка, скрепка, ватман,кнопка'''

print(play())