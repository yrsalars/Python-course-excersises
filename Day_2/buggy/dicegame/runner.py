from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        game=True
        wins_r = 0
        losses_r = 0
        rounds = 1
        while game:
            runner = cls()

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins_r += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                losses_r += 1
                c = 0
            print("Wins: {} Loses {}".format(wins_r, losses_r))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            else:
                game = False
