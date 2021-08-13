from tkinter import *
import random, string

m = Tk()
m.title('Password_generator')
# set the container size
m.geometry('312x250+200+100')
m.configure(bg='lightyellow')
# text color and project heading
t = Label(m, text="Password-Generator", bg='Cyan', font="Greek 10 bold").pack(side=TOP, pady=10)
Label(m, text='select length of Password Size', bg='yellow', bd=10, font="Greek 10 bold").pack(side=TOP, pady=10)
pass_len = IntVar()
length = Spinbox(m, from_=8, to_=32, textvariable=pass_len, width=15).pack()
pass_str = StringVar()

def Generate_Password():
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
        for y in range(pass_len.get() - 4):
            password = password + random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)

button = Button(m, text='click here!', command=Generate_Password).pack(side=TOP, pady=8)
Label(m, text="Password Here!", bg='lightgreen', bd=8).pack()
Entry(m, textvariable=pass_str).pack(side=TOP, pady=8)
m.mainloop()
