from tkinter import *
from tkinter import messagebox

def findBMI():
    bmi = int(weight.get())/(int(height.get())*int(height.get()))*10000
    bmiEmpty.config(text = "Your BMI is: " + str("{:.1f}".format(bmi)))

def nextPage():
    root.destroy()
    import info_pg

def kill_app():
    msg = messagebox.askquestion("Exit?", "Do you really want to exit?")
    if msg == 'yes':
        root.destroy()
    else:
        messagebox.showinfo("Returning back...", "Returning back to the app...")

#def warning(message, title="USE METRIC SYSTEM!"):
    #root = Tk()
    #root.overrideredirect(1)
    #root.withdraw()
    #messagebox.showwarning(title, message)
    #root.destroy()

#warning("This application uses the Metric System!")

root = Tk()


height = IntVar()
weight = IntVar()

label_one = Label(root, text = "Calculate your BMI", font = ("Ubuntu", 18))
label_one.pack(ipadx=10, ipady=10)

height_label = Label(root, text = "Enter your Height: ", font = ("Verdana", 12))
height_label.place(x = 70, y = 98)

weight_label = Label(root, text = "Enter your Weight: ", font = ("Verdana", 12))
weight_label.place(x = 70, y = 148)

info_label = Label(root, text = "For more info -> ", font = ("Anonymous Pro", 10))
info_label.place(x = 10, y = 360)

bmiEmpty = Label(root, font = ("Verdana", 12))
bmiEmpty.place(x = 140, y = 220)

signature = Label(root, text = "made by Rale", font = ("Anonymous Pro", 10))
signature.place(x = 300, y = 360)

height = Entry(root, width = 10, textvariable = height, font = ("Verdana", 12))
height.place(x = 250, y = 100)

weight = Entry(root, width = 10, textvariable = weight, font = ("Verdana", 12))
weight.place(x = 250, y = 150)

run_btn = Button(root, text = "Run", font = ("Ubuntu", 12), width = 5, command = findBMI)
run_btn.place(x = 150, y = 280)

info_btn = Button(root, text = "Info", font = ("Ubuntu", 10), command = nextPage)
info_btn.place(x = 130, y = 355)

exit_btn = Button(root, text = "Exit", width = 5, font = ("Ubuntu", 12), command = kill_app)
exit_btn.place(x = 230, y = 280)

root.geometry("400x400")
root.resizable(0, 0)
root.title("Calculate your BMI")
root.mainloop()
