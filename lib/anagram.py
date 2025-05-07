# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Sort the characters of the original word
        sorted_word = sorted(self.word)

        # Use a list comprehension to filter anagrams
        return [w for w in word_list if sorted(w) == sorted_word]
