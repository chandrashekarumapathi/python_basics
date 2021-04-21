class Reverse:
    def __init__(self, word: list):
        self.word = word
        self.show_reversed()

    def reverse_input(self):
        reversed_word = self.word[::-1]
        return reversed_word

    def check_if_palindrome(self):
        reversed_word = self.reverse_input()
        if self.word == reversed_word:
            return 'is a palindrome'
        else:
            return 'is not a palindrome'

    def show_reversed(self):
        word_reversed = self.reverse_input()
        answer = self.check_if_palindrome()
        print('Word given: ', self.word)
        print('Reverse of the word: ', word_reversed, '\n')
        print(self.word, answer)


test = Reverse(word='Hello')

