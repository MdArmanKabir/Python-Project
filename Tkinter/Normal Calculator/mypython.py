from tkinter import *
from tkinter.messagebox import *
from math import *

# some variable
font = ('arial', 21, 'italic bold')


# some function

def percent():
    z = eval(entry.get())
    p = z / 100
    entry.delete(0, END)
    entry.insert(END, p)


def rt():
    try:
        x = sqrt(float(entry.get()))
        entry.delete(0, END)
        entry.insert(0, x)
    except Exception as ei:
        entry.delete(0, END)
        entry.insert(END, 'syntax error...!')

        print('error..', ei)
        showerror('ERROR', ei)


def one_clear():
    ex = entry.get()
    ex = ex[0: len(ex) - 1]
    entry.delete(0, END)
    entry.insert(0, ex)


def click(event):
    b = event.widget
    tex = b['text']

    if tex == 'x':
        entry.insert(END, '*')
        return
    if tex == '÷':
        entry.insert(END, '/')
        return
    if tex == 'AC':
        entry.delete(0, END)
        return

    if tex == '=':
        try:
            exp_1 = entry.get()
            answer = eval(exp_1)
            entry.delete(0, END)
            entry.insert(0, answer)

        except Exception as ex:
            entry.delete(0, END)
            entry.insert(END, 'syntax error...!')

            showerror('ERROR', ex)

        return
    if entry.get() == 'syntax error...!':
        entry.delete(0, END)

    entry.insert(END, tex)


# creating a window

root = Tk()
root.title('CALCULATOR')
root.iconbitmap('logo.ico')

# center the main window on the screen
window_width = 330
window_height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 3) - (window_height / 2)
print(y_coordinate, x_coordinate)

root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))
root.config(bg='#c0c0c0')

# creating entry box
frame = Frame(root, height=29)
frame.pack(side=TOP)

entry = Entry(root, font=font, justify=RIGHT, border=6)
entry.pack(fill='x', padx=8, pady=10, ipady=15)

# creating button

button_frame = Frame(root, bg='#c0c0c0')
button_frame.pack(side=TOP, padx=5, pady=5)

tamp = 7
for i in range(2, 5):
    for j in range(3):

        btn = Button(button_frame, text=str(tamp), font=font, height=1, width=4, bg='#c0c0c0', relief='ridge', border=2,
                     highlightbackground='red', activebackground='white')

        btn.grid(row=i, column=j)
        tamp = tamp + 1
        btn.bind('<Button>', click)
        if tamp == 10 and i == 2:
            tamp = 4
        if tamp == 7 and i == 3:
            tamp = 1

btn_mc = Button(button_frame, text='MC', font=font, height=1, width=4, relief='ridge', bg='white',
                activebackground='#c0c0c0', border=2)
btn_mc.grid(row=0, column=0),
btn_mr = Button(button_frame, text='MR', font=font, height=1, width=4, relief='ridge', bg='white',
                activebackground='#c0c0c0', border=2)
btn_mr.grid(row=0, column=1)
btn_mm = Button(button_frame, text='M-', font=font, height=1, width=4, relief='ridge', bg='white',
                activebackground='#c0c0c0', border=2)
btn_mm.grid(row=0, column=2)
btn_mp = Button(button_frame, text='M+', font=font, height=1, width=4, relief='ridge', bg='white',
                activebackground='#c0c0c0', border=2)
btn_mp.grid(row=0, column=3)

btn_ac = Button(button_frame, text='AC', font=font, height=1, width=4, relief='ridge', bg='white',
                activebackground='#c0c0c0', border=2)
btn_ac.grid(row=1, column=0)
btn_clr = Button(button_frame, text='C', font=font, height=1, width=4, relief='ridge', bg='white',
                 activebackground='#c0c0c0', border=2, command=one_clear)
btn_clr.grid(row=1, column=1)
btn_rt = Button(button_frame, text='√', font=font, height=1, width=4, relief='ridge', bg='white',
                activebackground='#c0c0c0', border=2, command=rt)
btn_rt.grid(row=1, column=2)
btn_div = Button(button_frame, text='÷', font=font, height=1, width=4, relief='ridge', bg='white',
                 activebackground='#c0c0c0', border=2)
btn_div.grid(row=1, column=3)

btn_multi = Button(button_frame, text='x', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2)
btn_multi.grid(row=2, column=3)
btn_sub = Button(button_frame, text='-', font=font, height=1, width=4, relief='ridge', bg='white',
                 activebackground='#c0c0c0', border=2)
btn_sub.grid(row=3, column=3)
btn_add = Button(button_frame, text='+', font=font, height=1, width=4, relief='ridge', bg='white',
                 activebackground='#c0c0c0', border=2)
btn_add.grid(row=4, column=3)

btn_per = Button(button_frame, text='%', font=font, height=1, width=4, relief='ridge', bg='white',
                 activebackground='#c0c0c0', border=2, command=percent)
btn_per.grid(row=5, column=0)
btn_zero = Button(button_frame, text='0', font=font, height=1, width=4, relief='ridge', bg='white',
                  activebackground='#c0c0c0', border=2)
btn_zero.grid(row=5, column=1)
btn_dot = Button(button_frame, text='.', font=font, height=1, width=4, relief='ridge', bg='white',
                 activebackground='#c0c0c0', border=2)
btn_dot.grid(row=5, column=2)
btn_equal = Button(button_frame, text='=', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2)
btn_equal.grid(row=5, column=3)

# binding button

# btn_mc.bind('<Button>', click)
# btn_mr.bind('<Button>', click)
# btn_mm.bind('<Button>', click)
# btn_mp.bind('<Button>', click)


btn_ac.bind('<Button-1>', click)
btn_div.bind('<Button-1>', click)
btn_multi.bind('<Button-1>', click)
btn_sub.bind('<Button-1>', click)
btn_add.bind('<Button-1>', click)

btn_zero.bind('<Button-1>', click)
btn_dot.bind('<Button-1>', click)
btn_equal.bind('<Button-1>', click)

root.mainloop()
