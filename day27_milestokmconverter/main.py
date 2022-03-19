from tkinter import *


def button_clicked():
    new_text = int(input.get())*1.6
    my_label2.config(text=new_text)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=30, pady=30)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

#Miles
my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(column=2, row=0)
my_label.config(padx=50)

#Label
my_label1 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label1.grid(column=0, row=1)
my_label1.config(padx=10)

my_label2 = Label(text="0", font=("Arial", 24, "bold"))
my_label2.grid(column=1, row=1)
my_label2.config(padx=10)

my_label3 = Label(text="Km", font=("Arial", 24, "bold"))
my_label3.grid(column=2, row=1)
my_label3.config(padx=10)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)





window.mainloop()
