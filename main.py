import tkinter

#this will covert it to km once click
def calculate():
    km = int(user_input.get()) * 1.609
    km_answer.config(text=round(km))

# this will create the GUI
window = tkinter.Tk()
window.title("Miles to Kilometer")
window.minsize(width=200, height=100)
window.config(padx=40, pady=20)

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 24))
equal_label.grid(column=0, row=1)

km_answer = tkinter.Label(text="0", font=("Arial", 24))
km_answer.grid(column=1, row=1)

km_label = tkinter.Label(text="km", font=("Arial", 24))
km_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

# this will keep the program running
window.mainloop()
