import tkinter as tk
from random import random
from sys import exit

root = tk.Tk()
currentGameText = "LOST IN SPACE:\nYou have fifteen hours to find a capsule lost in a SEVEN kilometer cube of space.\n"
currentInteractionText = "Understood. What must I do?"

#Game Logic
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
#Game Logic Ends. GUI begins.
"""
root.title("Tim Hartnell’s Lost In Space")
visibleGameText = tk.Label(root, text=currentGameText)
visibleGameText.grid(row = 0, columnspan=3)
xLabel = tk.Label(root, text="Y coordinate: ")
yLabel = tk.Label(root, text="X coordinate: ")
zLabel = tk.Label(root, text="Z coordinate: ")
xLabel.grid(row=1, column=0)
yLabel.grid(row=1, column=1)
zLabel.grid(row=1, column=2)
xCoordField = tk.Entry(root)
yCoordField = tk.Entry(root)
zCoordField = tk.Entry(root)
xCoordField.grid(row=2, column=0)
yCoordField.grid(row=2, column=1)
zCoordField.grid(row=2, column=2)
coordOptions = (xLabel, yLabel, zLabel, xCoordField, yCoordField, zCoordField)
for i in coordOptions:
    i.grid_forget()
#TODO: same thing but with i.grid() to make them visible again
blankLabel = tk.Label(root, text="")
blankLabel.grid(row=3, columnspan=3)
resultButton = tk.Button(root, text=currentInteractionText, background="red")
resultButton.grid(row=4, columnspan=3, ipadx=5, ipady=10)
root.mainloop()
"""
game()
