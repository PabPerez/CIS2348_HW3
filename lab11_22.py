#Pablo Perez
#PSID: 177045
user_words = input()
word_list = user_words.split(" ")

for word in word_list:
    print(word, word_list.count(word))