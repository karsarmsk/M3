def single_root_words(root_word, other_words):
    ex = True # флаг проверки на совпадение
    check_words = []  # сюда запишу слова прошедшие проверку
    kluch = []
    world = []
    kluch.extend(root_word.lower())  # ключевое слово разобьем на буквы
    world.extend(other_words.lower()) # входящее слово разобьем на буквы
    for i in range(len(root_word)):
        if (kluch[i] in world):
            ex = True # совпадение итой буквы в любом регистре
        else:
            ex = False
            break  # если нет совпадения больше не проверяем
    if ex == True and other_words != []:
        # elif other_words == (""):
        check_words.append(other_words)

    return ','.join(check_words)

#slova = ('rich', 'richiest', 'orichalcum', 'cheers', 'richies') # 1 входная строка
slova = ('Disablement', 'Able', 'Mable', 'Disable', 'Bagel') # 2 входная строка
same_words = []
root_word = slova[0]                # Ищем наименьшее ключевое слово в строке
for j in range(1,len(slova)):
    if len(slova[j]) < int(len(root_word)):
        root_word = slova[j]  # Наименьшее ключевое слово

for i in slova:
    slovo = single_root_words(root_word, i) # Функция отбора подходящих слов
    same_words.append(slovo)
print('ключ "'+ root_word + '" входит в слова')
print(same_words)





