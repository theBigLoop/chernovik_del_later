#Программа по работе со словом
#Функции
# 1 - количество букв
def first(word):
    return len(word)

# 2 - количество гласных и согласных
def second(word):
    vowels = ['a','e','i','o','u','y','а','е','ё','и','о','у','ы','э','ю','я']
    counter_vowels = 0
    counter_consonants = 0
    for i in word.lower():
        if i in vowels:
            counter_vowels += 1
        else:
            counter_consonants += 1
    return f"Гласные: {counter_vowels}, Согласные: {counter_consonants}"


#3 - Определить язык 
def third(word):
    russ = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    eng = 'abcdefghijklmnopqrstuvwxyz'
    language = ''
   
    if word[0] in russ:
        language = 'Руссикий'
    elif word[0] in eng:
        language = 'English'
    else:
        language = 'Not known language'

    return f'Определяем язык: {language} ' 



# --- меню ---

print('1 - cколько букв в слове')
print('2 - cколько гласных и согласных в слове')
print('3 - какой это язык')
action = input('choose action: 1/2/3 - ') # Выбираем действие 
word = input('Введите длинное слово - ') # Введите слово



if action == '1':
    print(first(word))
elif action == '2':
    print(second(word))
elif action == '3':
    print(third(word))
else:
    print('Wrong')



#выбор пользователя


    
