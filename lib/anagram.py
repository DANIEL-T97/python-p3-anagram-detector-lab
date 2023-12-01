class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        return [candidate for candidate in possible_anagrams if self.is_anagram(candidate)]

    def is_anagram(self, candidate):
        return sorted(self.word) == sorted(candidate)
