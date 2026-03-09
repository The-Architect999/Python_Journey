import unittest
import guessing_game

class TestMain (unittest.TestCase):

    def setUp(self):
        self.number = 5
        
    def test1 (self):
        guess = 1
        result = guessing_game.run_guess(guess, self.number)
        self.assertFalse(result)

    def test2 (self):
        guess = 'a'
        result = guessing_game.run_guess(guess, self.number)
        self.assertIsInstance(result, TypeError)

if __name__ == '__main__':
    unittest.main()