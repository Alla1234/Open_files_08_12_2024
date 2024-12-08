#3 Задача
# В задаче я использовала три произвольных текста об истории Пайтона
# Посчитала количество строк в каждом файле и вывела на печать

count = 0
count_list = []
mlist = ('1.txt', '2.txt', '3.txt')
f_list = []
for t in mlist:
    with open(t) as f:
        for line in f:
            count += 1
    count_list.append(count)
    count = 0
print(count_list)
print(sorted(count_list))
print(f_list)

f = open('1.txt')
print(type(f))
data = f.read()
print(data, type(data))

f = open('2.txt')
print(type(f))
data = f.read()
print(data, type(data))

f = open('3.txt')
print(type(f))
data = f.read()
print(data, type(data))
