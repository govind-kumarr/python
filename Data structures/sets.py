magic_word = "abracadabra"

unique_alphabets: set[str] = set(magic_word)


print(unique_alphabets)


sentence = "the big blue sky and the big blue ocean"
word_list = sentence.split()
# print(word_list)
unique_words = set(word_list)

unique_words.update(["govind", "kumar"])
print(unique_words)