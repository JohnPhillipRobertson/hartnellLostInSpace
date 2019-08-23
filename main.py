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
