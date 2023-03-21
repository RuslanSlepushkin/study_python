sentence = input('Write the sentence: ')
list_sentence = sentence.split()
dict_word = dict()
for word in list_sentence:
    if word in dict_word:
        dict_word[word] += 1
    else:
        dict_word[word] = 1
print(dict_word)