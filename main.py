from random import randint
easy_level_turns=10
hard_level_turns=5

def check_answer(guess,turns,answer):
    '''checks answer if guess is right or not '''
    if guess>answer:
        print("too high")
        return turns-1

    elif guess<answer:
        print("too low")

        return turns-1
    else:
        print("you got it. ")
def set_difficulty():
    difficulty=input("enter easy if you want difficulty to be easy and hard if you want it to be hard.")
    if difficulty=="easy":
        return easy_level_turns
    else:
        return hard_level_turns
def game():
    print("welcome to the number guessing game.")
    print("I am computer and i am thinking of a number between 1 to 100.  Can you guess??")
    answer=randint(1,100)
    print(f"Dont tell anyone the answer its {answer}")

    turns=set_difficulty()
    #repeating the guess functionality if they dont get it right.
    guess=0
    while guess!=answer:
        print(f"You have {turns} left to make the correct guess.")

        guess=int(input("enter your guess."))

        turns=check_answer(guess, turns, answer)
        if turns==0:
            print("YOU have run out of turns.")
            return
        elif guess!=answer:
            print("guess again.")

game()






