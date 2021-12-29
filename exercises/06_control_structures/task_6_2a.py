# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите ip адрес в формате 10.0.1.1: ')
ip_correct = False

while not ip_correct:
   if ''.join(ip.split('.')).isdigit() == False:
      print('Неправильный IP-адрес')
      break
   elif len(ip.split('.')) != 4:
      print('Неправильный IP-адрес')
      break
   elif int(ip.split('.')[0]) >=1 and int(ip.split('.')[0])<=223:
      print('unicast')
      ip_correct = True
   elif int(ip.split('.')[0]) >=224 and int(ip.split('.')[0])<=239:
      print('multicast')
      ip_correct = True
   elif ip == '255.255.255.255':
      print('local broadcast')
      ip_correct = True
   elif ip == "0.0.0.0":
      print('unassigned')
      ip_correct = True
   else:
      print('unused')
      ip_correct = True