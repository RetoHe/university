import tkinter as tk

def add(event):
    results = int(input_entry1.get()) + int(input_entry2.get())
    output_result.set(results)

def substract(event):
    results = int(input_entry1.get()) - int(input_entry2.get())
    output_result.set(results)

def muliply(event):
    results = int(input_entry1.get()) * int(input_entry2.get())
    output_result.set(results)

def divide(event):
    results = int(input_entry1.get()) / int(input_entry2.get())
    output_result.set(results)

window = tk.Tk()
window.title("Calculator")
window.geometry("400x300")
window.resizable(False, False)

input_entry1 = tk.StringVar()
input_entry2 = tk.StringVar()
output_result = tk.StringVar()

input_1 = tk.Label(window, text = "Input Number 1:", font = "Helvetica 9 bold")
input_1.grid(column = 1, row = 1)

input_2 = tk.Label(window, text = "Input Number 2:", font = "Helvetica 9 bold")
input_2.grid(column = 1, row = 2)

result = tk.Label(window, text = "Result:", font = "Helvetica 9 bold")
result.grid(column = 1, row = 4)

entry1 = tk.Entry(window, textvariable = input_entry1)
entry1.grid(column = 2, row = 1, columnspan = 4)
input_entry1.set("")

entry2 = tk.Entry(window, textvariable = input_entry2)
entry2.grid(column = 2, row = 2, columnspan = 4)
input_entry2.set("")

entry_result = tk.Entry(window, textvariable = output_result)
entry_result.grid(column = 2, row = 4, columnspan = 4)
output_result.set("")

add_button = tk.Button(window, text ="+", font = "Helvetica 11 bold", bg = "grey")
add_button.grid(row = 3, column = 2)
add_button.bind("<Button-1>", add)

substract_button = tk.Button(window, text ="-", font = "Helvetica 11 bold", bg = "grey")
substract_button.grid(row = 3, column = 3)
substract_button.bind("<Button-1>", substract)

multiply_button = tk.Button(window, text ="*", font = "Helvetica 11 bold", bg = "grey")
multiply_button.grid(row = 3, column = 4)
multiply_button.bind("<Button-1>", muliply)

divide_button = tk.Button(window, text ="/", font = "Helvetica 11 bold", bg = "grey")
divide_button.grid(row = 3, column = 5)
divide_button.bind("<Button-1>", divide)

window.mainloop()
