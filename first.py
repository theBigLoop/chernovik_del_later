

word = input('Введите длинное слово - ') # Введите слово
''' 
print('1 - cколько букв в слове')
print('2 - cколько гласных в слове')
print('3 - cколько согласных в слове')
print('4 - какой это язык')
action = input('choose action: 1/2/3/4 ') # Выбираем действие 
''' 

#Функции
# 1 - количество букв
def first(word):
    return len(word)

# 2 - количество гласных
def second(word):
    vowels = ['a','e','i','o','u','y','а','е','ё','и','о','у','ы','э','ю','я']
    counter = 0
    for i in word.lower():
        if i in vowels:
            counter += 1
    return counter




# 3 - количество 

#Разбираем слова

    
