from random import random
from sys import exit

def winCondition(i):
        print("You found it with {} hours of air left".format(15 - i))
        end()
def end():
    print("Play again? Y/N")
    response = input()
    if response.lower() == "y":
        game()
    else:
        exit(0)
def game():
    A = int(7 * random() + 1)
    B = int(7 * random() + 1)
    C = int(7 * random() + 1)
    """
    https://stackoverflow.com/questions/57813858/iteratively-assigning-variables-in-python/57813901#57813901
    """
    def get_input(axis):
        while True:
            user_input = input(f"{axis}-Axis: ")
            try:
                axis_int = int(user_input)
                assert(axis_int <= 7)
            except:
                print("Enter a natural number in the range!")
                continue
            else:
                break
        return axis_int
    for i in range(15):
        print("Input 3 search coordinates")
        D, E, F = [get_input(axis) for axis in "YXZ"]
        print(str(D) + str(E) + str(F))
        if A == D and B == E and F == C:
            winCondition(i)
        else:
            print("You have {} hours of air left.".format(15 - i))
            if A > D:
                print("UP")
            elif A < D:
                print("DOWN")
            if B > E:
                print("PORT")
            elif B < E:
                print("STARBOARD")
            if C > F:
                print("FORWARD")
            elif C < F:
                print("BACKWARD")
            if i == 14:
                print("Choose your next move carefully... HYPOXIA IMMINENT.")
    print("Fail, astronaut dead; capsule was at coords {}.{}.{}".format(A, B, C))
    end()
game()
