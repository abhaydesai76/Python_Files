from string import ascii_lowercase
from words import get_words
from random_words import RandomWords

def get_num_attempts():
    while True:
        num_attempts = input("How many incorrect attempts do you want? [1-25]")

        try:
            num_attempts = input(num_attempts)

            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print("{0} is not between 1 and 25".format(num_attempts))

        except ValueError:
            print("{0} is not an integer between 1 and 25".format(num_attempts))

def get_min_word_length():
    while True:
        min_word_length = input("What minimum word length do you want? [4-16]")

        try:
            min_word_length = int(min_word_length)

            if 4 <= min_word_length <= 16:
                return min_word_length

            print("Word : {0}".format(get_display_word(word,idxs)))
            print("Attempts Remaining: {0}".format(attempts_remaining))
            print("Previous Guesses: {0}".format(' '.join(wrong_letters)))

            next_letter = get_next_letter(remaining_letters)

            if next_letter in word:
                print("{0} is in the word!".format(next_letter))

                for i in range(len(word)):
                    if word[i] == next_letter:
                        idxs[i] = True
            else:
                print("{0} is not in the word!".format(next_letter))

                attempts_remaining -= 1
                wrong_letters.append(next_letter)

            if false not in (idxs):
                word_solved = True
            print()

        print("The word is {0}".format(word))

        if word_solved:
            print("Congratulations ! You Won!")
        else:
            print("Try again next time !")

        try_again = input("Would you like to try again? [y/Y]")
        return try_again.lower() == 'y'

        if __name__ == '__main__':
            while play_hangman():
                print()



