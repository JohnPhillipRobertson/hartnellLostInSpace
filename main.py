import tkinter as tk
import random
root = tk.Tk()
root.title(“Tim Hartnell’s Lost In Space”)
visibleGameText = tk.Label(root, currentGameText)
visibleGameText.grid()
xCoordField = tk.Entry(root, “X coordinate:”)
yCoordField = tk.Entry(root, “Y coordinate:”)
zCoordField = tk.Entry(root, “Z coordinate:”)
xCoordField.grid(row=1, column=0)
yCoordField.grid(row=1, column=1)
zCoordField.grid(row=1, column=2)
resultButton = tk.Button(root, “Launch search for capsule.”)
resultButton.grid(row=2, columnspan=3)
root.mainloop()
“””
Pseudo code:
Print “lost in space”
“You have fifteen hours to find a capsule lost in a 7km cube of space”
A, B, C = 7*random+1
For i in range 15:
Print “Input 3 search coords”
D, E, F = input
os (“cls”)
Print D E F
If A B C == DEF goto winCondition
Else:
“You have {15 - i} hours of air left”
If a > d print UP
If a < d print DOWN
If b < e print starboard
If b> e print port
If c > f print forward
If c < f print backward
If i == 14 print “Danger death imminent”
Print “Fail, astronaut dead; capsule was at coords {}{}{}”
Goto end
winCondition:
“You found it with {} hours of air left”
end:
Print “play again”?
Check for yes or no

From “Making the most of your ZX 81” by Tim Hartnell“
“””
