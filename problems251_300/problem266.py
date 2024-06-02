# A step word is formed by taking a given word, adding a letter, and anagramming the result.
# For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".
#
# Given a dictionary of words and an input word, create a function that returns all valid step words.

def find_valid_step_words(valid_words, input_word : str):
    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)

    input_word = input_word.lower()
    step_words = set()


    for letter in "abcdefghijklmnopqrstuvwxyz":
        new_word = input_word + letter
        for word in valid_words:
            if is_anagram(new_word, word):
                step_words.add(word)

    return step_words


if __name__ == "__main__":
    dictionary = ["apple", "appeal", "pale", "peal", "lapel"]
    word = "apple"
    print(find_valid_step_words(dictionary, word))