from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=250, height=120)
window.maxsize(width=280, height=150)
window.configure(pady=20, padx=20)


def miles_to_km():
    miles = float(miles_entry.get())
    km.configure(text=f"{round(miles * 1.609, 2)}")


miles_entry = Entry(width=7)
miles_entry.grid(row=0, column=1)
miles_entry.configure()
miles_entry.focus()

miles_label = Label(text="Miles to")
miles_label.grid(row=0, column=2)

equal_miles = Label(text="is equal to")
equal_miles.grid(row=1, column=0)

km = Label(text=f"{0}")
km.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate = Button(width=7, text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)


window.mainloop()