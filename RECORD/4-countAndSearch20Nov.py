def count_words(sentence):
    words = sentence.split()
    return len(words)

def search_word(sentence, word):
    return word in sentence.lower().split()

sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print("Number of words:", word_count)

search_word = input("Enter a word to search: ")
if search_word in sentence.lower():
    print(f"The word '{search_word}' was found in the sentence.")
else:
    print(f"The word '{search_word}' was not found in the sentence.")
