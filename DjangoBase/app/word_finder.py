class WordFinder:
    def __init__(self, list):
        self.word_set = set(word.strip() for word in list)

    def is_valid_subset(self, word, candidate):
        word_count = {letter: word.count(letter) for letter in word}
        candidate_count = {letter: candidate.count(letter) for letter in candidate}
        return all(candidate_count[letter] <= word_count[letter] for letter in candidate)

    def longest_word(self, word):
        max_length = 0
        result_word = ""

        for candidate in self.word_set:
            if self.is_valid_subset(word, candidate) and len(candidate) > max_length:
                max_length = len(candidate)
                result_word = candidate

        return result_word