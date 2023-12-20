from django.test import TestCase
from app.word_finder import WordFinder

class WordFinderTestCase(TestCase):
    def test_longest_word(self):
        word_list = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
        word_finder = WordFinder(word_list)
        result = word_finder.longest_word('ajsxuytcnhre')
        self.assertEqual(result, 'saturn')


