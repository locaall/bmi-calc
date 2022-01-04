from tkinter import *

def returnBack():
    root.destroy()
    import bmi

root = Tk()

heading = Label(root, text = "BMI Category", font = ("Ubuntu", 15))
heading.place(x = 110, y = 10)

label_one = Label(root, text = "<18.5 --> Underweight", font = ("Ubuntu", 12))
label_one.place(x = 85, y = 60)

label_two = Label(root, text = "18.5 - 25 --> Normal weight", font = ("Ubuntu", 12))
label_two.place(x = 65, y = 100)

label_three = Label(root, text = "25 - 30 --> Overweight", font = ("Ubuntu", 12))
label_three.place(x = 85, y = 140)

label_four = Label(root, text = "30 - 35 --> Obese Class I", font = ("Ubuntu", 12))
label_four.place(x = 80, y = 180)

label_five = Label(root, text = "35 - 40 --> Obese Class II", font = ("Ubuntu", 12))
label_five.place(x = 80, y = 220)

label_six = Label(root, text = "> 40 --> Obese Class III", font = ("Ubuntu", 12))
label_six.place(x = 85, y = 260)

returnBtn = Button(root, text = "Return", font = ("Ubuntu", 10), command = returnBack)
returnBtn.place(x = 150, y = 300)

root.resizable(0, 0)
root.geometry("350x350")
root.title("BMI Information")
root.mainloop()
