def edit_story(words, func):
    for word in words:
        print(func(word))

list_words = ['one', 'two', 'three']

def word_capitalizer(word):
    return word.capitalize() + '#'

edit_story(list_words, word_capitalizer)

edit_story(list_words, lambda word: word.capitalize() + "#")