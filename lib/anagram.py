# your code goes here!class Anagram:
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [w for w in word_list if self.is_anagram(w)]

    def is_anagram(self, other_word):
        other_word_lower = other_word.lower()

        if len(self.word) != len(other_word_lower):
            return False

        return sorted(self.word) == sorted(other_word_lower)
