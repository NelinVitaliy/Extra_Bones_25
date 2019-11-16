str_user = input('Enter string: ')
list_words = str_user.split()

# print(list_words)
index_word = 0


for i in range(1, len(list_words)):
    if len(list_words[index_word]) < len(list_words[i]):
        index_word = i

print(list_words[index_word])






# С комментариями:
#
# # исходная строка и ее вывод на экран
# str = "python java c c++ javascript pascal php"
# print(str)
#
# # преобразование строки в список слов,
# # разделение происходит по пробелу
# listWords = str.split()
#
# # предполагается, что самое длинное слово находится первым
# # в списке, т. е. имеет индекс 0
# idLongestWord = 0
#
# # остальные слова перебираются в цикле
# for i in range(1,len(listWords)):
#     # Если длина слова под индексом idLongestWord больше,
#     # чем длина слова под текущим индексом,
#     if len(listWords[idLongestWord]) < len(listWords[i]):
#         # то следует записать индекс текущего слова в
#         # переменную idLongestWord
#         idLongestWord = i
#
# # извлечение из списка listWords
# # слова с индексом idLongestWord и его вывод на экран
# print(listWords[idLongestWord])