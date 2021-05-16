import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
#logo
logo = Image.open('Static/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all it's text", font="Garamond")
instructions.grid(columnspan=3, column=0, row=1)


def open_file():
	browse_text.set("Loading...")
	file = askopenfile(parent=root, mode="rb", title="Choose a file", filetype=[("Pdf file", "*.pdf")])
	if file:
		read_pdf = PyPDF2.PdfFileReader(file)
		page = read_pdf.getPage(0)
		page_content = page.extractText()
		print(page_content)


		#text box
		text_box = tk.Text(root, height=10, width=50, padx=10, pady=15, font="Garamond" )
		text_box.insert(1.0, page_content)
		text_box.tag_configure("center", justify="center")
		text_box.tag_add("center", 1.0, "end")
		text_box.grid(column=1, row=3)
		browse_text.set("Browse")



#browse button
browse_text = tk.StringVar()
browse_text.set('Browse')
browse_btn = tk.Button(root, textvariable=browse_text, font="Garamond", bg="#20bebe", fg="white", height=2, width=15, command=lambda:open_file())
browse_btn.grid(column=1, row=2)
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)








root.mainloop()