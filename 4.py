import random
import collections
import operator

random.seed()

names = ['michail','anastasia','viktor','Noah','Liam','William','Mason','James','Benjamin','Jacob','Michael','Elijah','Ethan']

#1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

def f(names,n):
    list_names = []
    for i in range(n):
        list_names.append(names[random.randint(0,len(names)-1)])
    return list_names


#2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

def n(list_names):
    temp = dict(collections.Counter(new_list))
    temp = sorted(temp.items(), key=operator.itemgetter(1), reverse = True)
    return temp[0]

#3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.

def g(list_names):
    list_t = map(lambda x:x[0],list_names)
    list_t = dict(collections.Counter(list_t))
    return sorted(list_t.items(), key=operator.itemgetter(1), reverse = False)[0]


new_list = f(names,20)
print(new_list)

print('Часто встречается ',n(new_list))
print('Cамой редкая буква, с которого начинаются имена в списке = ', g(new_list))

#4.  В файле с логами найти дату самого позднего лога (по метке времени):
import pandas as pd
df = pd.read_csv('log', sep=" - ",names=['time', 'event', 'info', 'description'])
df.sort_values(by="time",inplace=True)
print(df.iloc[-1:])