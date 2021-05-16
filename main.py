import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk


root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)
#logo
logo = Image.open('Static/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all it's text", font="Garamond")
instructions.grid(columnspan=3, column=0, row=1)

#browse button
browse_text = tk.StringVar()
browse_text.set('Browse')
browse_btn = tk.Button(root, textvariable=browse_text, font="Garamond")
browse_btn.grid(column=1, row=2)




root.mainloop()