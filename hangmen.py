import re
from words import Generator


class HangmenGame:
    g = Generator()
    wordGuessed = False                      # indicates if the word is guessed Y/N
    word_to_guess = g.get_from_dictionary()  # the word to guess
    words_guessed = []                       # array with the letters that are already guessed
    tries_done = 0                           # how many tries the guesser has made
    max_tries = 10                           # max amount of tries

    # define the word (step 1 of the whole game)
    def set_word(self, hangmen_word):
        self.word_to_guess = hangmen_word

    # returns true if it is a valid input
    def checklist(self, to_check):
        if to_check in self.words_guessed:
            return False
        else:
            return True

    # shows the guessed letters, if a letter is not guessed it will display a dot ( . )
    def hashed_word(self):
        output = ""
        good_guesses = 0
        for w in self.word_to_guess:
            if w in self.words_guessed:
                good_guesses += 1
                output = output + " " + w + " "
            else:
                output = output + " . "
        if good_guesses == len(self.word_to_guess):
            self.wordGuessed = True
        return output

    # returns true if the letter (guessed) is in the word_to_guess
    def check_guess(self, to_check):
        if re.search(to_check, self.word_to_guess):
            return True
        else:
            return False

    # return true if all tries are done
    def end_of_game(self):
        if self.max_tries - self.tries_done <= 0:
            print(self.max_tries - self.tries_done)
            self.wordGuessed = True

    # add letter to the "guessed" letters list
    def add_letter(self, letter):
        self.words_guessed.append(letter)

    # a guess of the guessing player (is a single letter)
    def guess(self, user_guess):
        self.end_of_game()
        if not self.wordGuessed:
            if not self.checklist(user_guess):
                return "This letter is already guessed"
            elif self.check_guess(user_guess):
                self.add_letter(user_guess)
                return "YES! this letter is in the word"
            else:
                self.add_letter(user_guess)
                self.tries_done = self.tries_done + 1
                return "WRONG!, this letter isn't in the word"
        else:
            return "END OF GAME: THE WORD IS: " + self.word_to_guess

    def get_tries(self):
        return str(self.tries_done)
