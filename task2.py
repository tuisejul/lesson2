price = int(input('Введите цену'))
count = float(input('Введите количество подукта'))
money = int(input('Введите внесенные средства'))
print(money - (price*count)) #Задачи 1-2

name = str(input('Введите название товара'))
weight = float(input('Введите вес товара'))
price1 = float(input('Введите цену товара'))
S = price1*weight
Cash = float(input('Введите внесенные средства'))
A = Cash - S
print('Чек', name, 'вес', weight, 'цена', price1,
      'Итого:', S,
      'Внесено:', Cash,
      'Сдача:', A ) #Задача 3

N = int(input('Введите натуральное число'))
print(str('Купи конструктор!')*N, sep="\n" #Задача 4

B = int(input('Введите натуральное число'))
F = str(input('Введите любимое дело'))
print(('обожаю писать' + F) * B, sep="\n") #Задача 5
