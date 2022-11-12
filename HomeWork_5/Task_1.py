'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''

text = input('Введите текст: ')

text_list = text.split(' ')

result = ' '.join([i for i in text_list if 'абв' not in i])

print(result)