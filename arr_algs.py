# -*- coding: utf-8 -*-
array = raw_input('Массив: ')
list_array = [int(i) for i in array.split(' ')]
min_el = min(list_array)
a=sum(list_array)
b=len(list_array)
sr_ar=a/b
print 'Минимальный элемент: ', min_el
print 'Среднее арифметическое: ', sr_ar
