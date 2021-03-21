from tkinter import *
from math import *

# some variable..............!

font = ('arial', 20, 'italic bold')
font_menu = ('courier new', 12, 'italic bold')
font_m = ('arial', 9, 'italic')
sc_font = ('arial', 16, 'italic bold')
color = '#4b0082'


# some function..............!


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
    except:
        entry.delete(0, END)
        entry.insert(END, 'syntax error...!')


def one_clear():
    ex = entry.get()
    ex = ex[0: len(ex) - 1]
    entry.delete(0, END)
    entry.insert(0, ex)


def answer():
    try:
        exp_1 = entry.get()
        ans = eval(exp_1)
        entry.delete(0, END)
        entry.insert(0, ans)

    except:
        entry.delete(0, END)
        entry.insert(END, 'syntax error...!')


# creating a window..................!

root = Tk()
root.title('Expert Calculator')
root.iconbitmap('logo.ico')


# center the main window on the screen.........!


def window_center(window_width, window_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 3) - (window_height / 2)

    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))
    root.config(bg='#c0c0c0')


# calling window_center function...............!


window_center(323, 513)

# declare images.......................!

pic_sc = PhotoImage(file='sc_logo64.png')
pic_normal = PhotoImage(file='standard264.png')
pic_programming = PhotoImage(file='programming_logo64.png')
pic = PhotoImage(file='line124.png')
pic_standard_menu = PhotoImage(file='standard_menu116.png')
pic_scientific_menu = PhotoImage(file='scientific_menu16.png')
pic_programmer_menu = PhotoImage(file='programming_menu16.png')

# creating entry box and frame..............!

normal_logo_frame = Frame(root, bg='#c0c0c0', height=80)
sc_logo_frame = Frame(root, bg='#c0c0c0', height=80)
programmer_logo_frame = Frame(root, bg='#c0c0c0', height=80)

entry = Entry(root, font=font, justify=RIGHT, border=6)

st_button_frame = Frame(root, bg='#c0c0c0', padx=5, pady=5)
sc_toggle_button_frame = Frame(root, bg='#c0c0c0')
sc_toggle_button_frame_1 = Frame(root, bg='#c0c0c0')
sc_button_frame = Frame(root, bg='#c0c0c0')
m_button_frame = Frame(root, bg='#c0c0c0', padx=5, pady=5)
programmer_label_1 = Label(root, text='SORRY..!', font=font, bg='#c0c0c0')
programmer_label_2 = Label(root, text='ADDING SOON', font=font, bg='#c0c0c0')

# packing standard calculator frame................!

normal_logo_frame.pack()
entry.pack(fill='x', padx=8, pady=10, ipady=15)
m_button_frame.pack()
st_button_frame.pack()

# packing normal image and label into normal_logo_frame...........!

normal_pic = Label(normal_logo_frame, image=pic_normal, bg='#c0c0c0')
normal_pic.pack()
normal_label = Label(normal_logo_frame, text='Standard', bg='#c0c0c0', pady=0, font=font_menu, foreground=color)
normal_label.pack()

# creating scientific image and label, and packing into sc_logo_frame.................!

sc_pic = Label(sc_logo_frame, image=pic_sc, bg='#c0c0c0')
sc_pic.pack()
sc_label = Label(sc_logo_frame, text='Scientific', bg='#c0c0c0', pady=0, font=font_menu, foreground=color)
sc_label.pack()

# creating programming image and label, and packing into sc_logo_frame...............!

programmer_pic = Label(programmer_logo_frame, image=pic_programming, bg='#c0c0c0')
programmer_pic.pack()
programmer_label = Label(programmer_logo_frame, text='Programmer', bg='#c0c0c0', pady=0, font=font_menu,
                         foreground=color)
programmer_label.pack()

# some only st_button_frame button.........................!

btn_per = Button(st_button_frame, text='%', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                 activebackground='#c0c0c0', border=2, command=percent)
btn_per.grid(row=4, column=1)
btn_rt = Button(st_button_frame, text='√', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                activebackground='#c0c0c0', border=2, command=rt)
btn_rt.grid(row=0, column=3)


# most important button..........................!


def button():
    m_button_width = 7
    m_button_height = 1

    # number button...(0 - 9)

    btn_zero = Button(add_frame, text='0', font=font, height=1, width=4, relief='ridge', bg='white',
                      activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '0'))
    btn_zero.grid(row=4, column=2)
    btn_1 = Button(add_frame, text='1', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '1'))
    btn_1.grid(row=3, column=1)
    btn_2 = Button(add_frame, text='2', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '2'))
    btn_2.grid(row=3, column=2)
    btn_3 = Button(add_frame, text='3', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '3'))
    btn_3.grid(row=3, column=3)
    btn_4 = Button(add_frame, text='4', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '4'))
    btn_4.grid(row=2, column=1)
    btn_5 = Button(add_frame, text='5', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '5'))
    btn_5.grid(row=2, column=2)
    btn_6 = Button(add_frame, text='6', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '6'))
    btn_6.grid(row=2, column=3)

    btn_7 = Button(add_frame, text='7', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '7'))
    btn_7.grid(row=1, column=1)
    btn_8 = Button(add_frame, text='8', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '8'))
    btn_8.grid(row=1, column=2)
    btn_9 = Button(add_frame, text='9', font=font, height=1, width=4, relief='ridge', bg='white',
                   activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '9'))
    btn_9.grid(row=1, column=3)

    # button (AC, C, /, *, -, +, ., =, )

    btn_ac = Button(add_frame, text='AC', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                    activebackground='#c0c0c0', border=2, command=lambda: entry.delete(0, END))
    btn_ac.grid(row=0, column=1)

    btn_clr = Button(add_frame, text='C', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='#c0c0c0', border=2, command=one_clear)
    btn_clr.grid(row=0, column=2)

    btn_div = Button(add_frame, text='÷', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '/'))
    btn_div.grid(row=0, column=4)

    btn_multi = Button(add_frame, text='x', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                       activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '*'))
    btn_multi.grid(row=1, column=4)
    btn_sub = Button(add_frame, text='-', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '-'))
    btn_sub.grid(row=2, column=4)
    btn_add = Button(add_frame, text='+', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '+'))
    btn_add.grid(row=3, column=4)

    btn_dot = Button(add_frame, text='.', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '.'))
    btn_dot.grid(row=4, column=3)
    btn_equal = Button(add_frame, text='=', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                       activebackground='#c0c0c0', border=2, command=answer)
    btn_equal.grid(row=4, column=4)

    # button (MC, MR, M-, M+, MS)

    btn_mc = Button(m_add_frame, text='MC', font=font_m, height=m_button_height, width=m_button_width, relief='ridge',
                    bg='#c0c0c0',
                    activebackground='#c0c0c0', border=2, padx=2)
    btn_mc.grid(row=0, column=1),
    btn_mr = Button(m_add_frame, text='MR', font=font_m, height=m_button_height, width=m_button_width, relief='ridge',
                    bg='#c0c0c0',
                    activebackground='#c0c0c0', border=2, padx=2)
    btn_mr.grid(row=0, column=2)
    btn_mm = Button(m_add_frame, text='M-', font=font_m, height=m_button_height, width=m_button_width, relief='ridge',
                    bg='#c0c0c0',
                    activebackground='#c0c0c0', border=2, padx=2)
    btn_mm.grid(row=0, column=3)
    btn_mp = Button(m_add_frame, text='M+', font=font_m, height=m_button_height, width=m_button_width, relief='ridge',
                    bg='#c0c0c0',
                    activebackground='#c0c0c0', border=2, padx=2)
    btn_mp.grid(row=0, column=4)
    btn_ms = Button(m_add_frame, text='MS', font=font_m, height=m_button_height, width=m_button_width, relief='ridge',
                    bg='#c0c0c0',
                    activebackground='#c0c0c0', border=2, padx=2)
    btn_ms.grid(row=0, column=5)

    # number button...(0 - 9) hover effect

    btn_1.bind('<Enter>', lambda e: btn_1.config(bg='#808080'))
    btn_1.bind('<Leave>', lambda e: btn_1.config(bg='white'))
    btn_2.bind('<Enter>', lambda e: btn_2.config(bg='#808080'))
    btn_2.bind('<Leave>', lambda e: btn_2.config(bg='white'))
    btn_3.bind('<Enter>', lambda e: btn_3.config(bg='#808080'))
    btn_3.bind('<Leave>', lambda e: btn_3.config(bg='white'))
    btn_4.bind('<Enter>', lambda e: btn_4.config(bg='#808080'))
    btn_4.bind('<Leave>', lambda e: btn_4.config(bg='white'))
    btn_5.bind('<Enter>', lambda e: btn_5.config(bg='#808080'))
    btn_5.bind('<Leave>', lambda e: btn_5.config(bg='white'))
    btn_6.bind('<Enter>', lambda e: btn_6.config(bg='#808080'))
    btn_6.bind('<Leave>', lambda e: btn_6.config(bg='white'))
    btn_7.bind('<Leave>', lambda e: btn_7.config(bg='white'))
    btn_7.bind('<Enter>', lambda e: btn_7.config(bg='#808080'))
    btn_8.bind('<Enter>', lambda e: btn_8.config(bg='#808080'))
    btn_8.bind('<Leave>', lambda e: btn_8.config(bg='white'))
    btn_9.bind('<Enter>', lambda e: btn_9.config(bg='#808080'))
    btn_9.bind('<Leave>', lambda e: btn_9.config(bg='white'))
    btn_zero.bind('<Enter>', lambda e: btn_zero.config(bg='#808080'))
    btn_zero.bind('<Leave>', lambda e: btn_zero.config(bg='white'))

    # button (AC, C, /, *, -, +, ., =, ) hover effect

    btn_ac.bind('<Enter>', lambda e: btn_ac.config(bg='#808080'))
    btn_ac.bind('<Leave>', lambda e: btn_ac.config(bg='#c0c0c0'))
    btn_clr.bind('<Enter>', lambda e: btn_clr.config(bg='#808080'))
    btn_clr.bind('<Leave>', lambda e: btn_clr.config(bg='#c0c0c0'))
    btn_div.bind('<Enter>', lambda e: btn_div.config(bg='#808080'))
    btn_div.bind('<Leave>', lambda e: btn_div.config(bg='#c0c0c0'))
    btn_multi.bind('<Enter>', lambda e: btn_multi.config(bg='#808080'))
    btn_multi.bind('<Leave>', lambda e: btn_multi.config(bg='#c0c0c0'))
    btn_add.bind('<Enter>', lambda e: btn_add.config(bg='#808080'))
    btn_add.bind('<Leave>', lambda e: btn_add.config(bg='#c0c0c0'))
    btn_sub.bind('<Enter>', lambda e: btn_sub.config(bg='#808080'))
    btn_sub.bind('<Leave>', lambda e: btn_sub.config(bg='#c0c0c0'))
    btn_rt.bind('<Leave>', lambda e: btn_rt.config(bg='#c0c0c0'))
    btn_rt.bind('<Enter>', lambda e: btn_rt.config(bg='#808080'))
    btn_per.bind('<Enter>', lambda e: btn_per.config(bg='#808080'))
    btn_per.bind('<Leave>', lambda e: btn_per.config(bg='#c0c0c0'))
    btn_dot.bind('<Enter>', lambda e: btn_dot.config(bg='#808080'))
    btn_dot.bind('<Leave>', lambda e: btn_dot.config(bg='#c0c0c0'))
    btn_equal.bind('<Enter>', lambda e: btn_equal.config(bg='#808080'))
    btn_equal.bind('<Leave>', lambda e: btn_equal.config(bg='#c0c0c0'))

    # button (MC, MR, M-, M+, MS) hover effect

    btn_mc.bind('<Enter>', lambda e: btn_mc.config(bg='#808080'))
    btn_mc.bind('<Leave>', lambda e: btn_mc.config(bg='#c0c0c0'))
    btn_mr.bind('<Enter>', lambda e: btn_mr.config(bg='#808080'))
    btn_mr.bind('<Leave>', lambda e: btn_mr.config(bg='#c0c0c0'))
    btn_mm.bind('<Leave>', lambda e: btn_mm.config(bg='#c0c0c0'))
    btn_mm.bind('<Enter>', lambda e: btn_mm.config(bg='#808080'))
    btn_mp.bind('<Enter>', lambda e: btn_mp.config(bg='#808080'))
    btn_mp.bind('<Leave>', lambda e: btn_mp.config(bg='#c0c0c0'))
    btn_ms.bind('<Enter>', lambda e: btn_ms.config(bg='#808080'))
    btn_ms.bind('<Leave>', lambda e: btn_ms.config(bg='#c0c0c0'))


# declare frame..................!


add_frame = st_button_frame
m_add_frame = m_button_frame

# calling button function................!

button()


# some scientific function...........!


def rt_3():
    try:
        r = float(eval(entry.get()))
        rt3 = r ** (1 / 3)
        entry.delete(0, END)
        entry.insert(END, rt3)
    except:
        entry.delete(0, END)
        entry.insert(END, 'syntax error...!')


# DEG and RAD changing function.......!


def click_deg(ee):
    try:

        if ee == 'sin\u207b\u00b9':
            s = asin(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, degrees(s))

        elif ee == 'cos\u207b\u00b9':
            s = acos(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, degrees(s))

        elif ee == 'tan\u207b\u00b9':
            s = atan(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, degrees(s))

        elif ee == 'sin':
            s = sin(radians(float(entry.get())))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))

        elif ee == 'cos':
            s = cos(radians(float(entry.get())))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))
        elif ee == 'tan':
            s = tan(radians(float(entry.get())))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))
    except:
        entry.delete(0, END)
        entry.insert(END, 'please first enter value')


def click_rad(ee):
    try:
        if ee == 'sin\u207b\u00b9':
            s = asin(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))

        elif ee == 'cos\u207b\u00b9':
            s = acos(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))
        elif ee == 'tan\u207b\u00b9':
            s = atan(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))

        elif ee == 'sin':
            s = sin(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))

        elif ee == 'cos':
            s = cos(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))
        elif ee == 'tan':
            s = tan(float(entry.get()))
            entry.delete(0, END)
            entry.insert(END, round(s, 6))
    except:
        entry.delete(0, END)
        entry.insert(END, 'please first enter value')


# creating scientific toggle frame button and frame toggle function...........!


def sc_toggle_button():
    global font
    global add_frame

    # toggling function................!

    def frame_toggle():
        global font
        global add_frame
        font = ('arial', 16, 'italic bold')

        if btn_toggle['text'] == '↑':

            sc_toggle_button_frame.pack_forget()
            sc_button_frame.pack_forget()

            # adding sc_toggle_button_1 frame.........!

            add_frame = sc_button_frame
            sc_toggle_button_1()
            sc_toggle_button_frame_1.pack()
            sc_button_frame.pack()
            btn_toggle.config(text='↓', background='#808080', foreground='red')

        else:

            btn_toggle.config(text='↑', background='#c0c0c0', foreground='green')
            sc_toggle_button_frame_1.pack_forget()
            sc_button_frame.pack_forget()

            # adding sc_toggle_button frame.........!

            sc_toggle_button_frame.pack()
            sc_button_frame.pack()

    # sc_toggle_button frame button (DEG: sin, cos, tan)........!

    btn_sin = Button(sc_toggle_button_frame, text='sin', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='white', border=2, command=lambda: click_deg('sin'))
    btn_sin.grid(row=0, column=2)
    btn_cos = Button(sc_toggle_button_frame, text='cos', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='white', border=2, command=lambda: click_deg('cos'))
    btn_cos.grid(row=0, column=3)
    btn_tan = Button(sc_toggle_button_frame, text='tan', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='white', border=2, command=lambda: click_deg('tan'))
    btn_tan.grid(row=0, column=4)

    # sc_toggle_button frame button ( X2, x3, XY, ex).........!

    btn_x2 = Button(sc_toggle_button_frame, text='x\u00b2', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                    activebackground='white', border=2, command=lambda: entry.insert(END, '**2'))
    btn_x2.grid(row=0, column=0)
    btn_x3 = Button(sc_toggle_button_frame, text='x\u00b3', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                    activebackground='white', border=2, command=lambda: entry.insert(END, '**3'))
    btn_x3.grid(row=0, column=1)
    btn_xy = Button(sc_toggle_button_frame, text='x\u02b8', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                    activebackground='white', border=2, command=lambda: entry.insert(END, '**'))
    btn_xy.grid(row=1, column=1)
    btn_ex = Button(sc_toggle_button_frame, text='e\u02e3', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                    activebackground='white', border=2, command=lambda: entry.insert(END, 'exp('))
    btn_ex.grid(row=1, column=4)

    # sc_toggle_button frame button (log, ln).......!

    btn_log = Button(sc_toggle_button_frame, text='log', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='white', border=2, command=lambda: entry.insert(END, 'log10('))
    btn_log.grid(row=1, column=2)
    btn_ln = Button(sc_toggle_button_frame, text='ln', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                    activebackground='white', border=2, command=lambda: entry.insert(END, 'log('))
    btn_ln.grid(row=1, column=3)

    # sc_toggle_button frame button ( frame toggle, R)..........!

    btn_toggle = Button(add_frame, text='↑', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                        activebackground='#c0c0c0', border=2, command=frame_toggle, foreground='green')
    btn_toggle.grid(row=0, column=0)
    btn_s_r = Button(sc_toggle_button_frame, text='R', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='white', border=2, command=lambda: entry.insert(END, 8.314))
    btn_s_r.grid(row=1, column=0)

    # sc_toggle_button frame button (DEG: sin, cos, tan) hover effect...................!

    btn_sin.bind('<Enter>', lambda e: btn_sin.config(bg='#808080'))
    btn_sin.bind('<Leave>', lambda e: btn_sin.config(bg='#c0c0c0'))
    btn_cos.bind('<Enter>', lambda e: btn_cos.config(bg='#808080'))
    btn_cos.bind('<Leave>', lambda e: btn_cos.config(bg='#c0c0c0'))
    btn_tan.bind('<Enter>', lambda e: btn_tan.config(bg='#808080'))
    btn_tan.bind('<Leave>', lambda e: btn_tan.config(bg='#c0c0c0'))

    # sc_toggle_button frame button ( X2, x3, XY, ex) hover effect....................!

    btn_x2.bind('<Enter>', lambda e: btn_x2.config(bg='#808080'))
    btn_x2.bind('<Leave>', lambda e: btn_x2.config(bg='#c0c0c0'))
    btn_x3.bind('<Enter>', lambda e: btn_x3.config(bg='#808080'))
    btn_x3.bind('<Leave>', lambda e: btn_x3.config(bg='#c0c0c0'))
    btn_xy.bind('<Enter>', lambda e: btn_xy.config(bg='#808080'))
    btn_xy.bind('<Leave>', lambda e: btn_xy.config(bg='#c0c0c0'))
    btn_ex.bind('<Enter>', lambda e: btn_ex.config(bg='#808080'))
    btn_ex.bind('<Leave>', lambda e: btn_ex.config(bg='#c0c0c0'))

    # sc_toggle_button frame button (log, ln, R) hover effect......................!

    btn_log.bind('<Enter>', lambda e: btn_log.config(bg='#808080'))
    btn_log.bind('<Leave>', lambda e: btn_log.config(bg='#c0c0c0'))
    btn_ln.bind('<Enter>', lambda e: btn_ln.config(bg='#808080'))
    btn_ln.bind('<Leave>', lambda e: btn_ln.config(bg='#c0c0c0'))
    btn_s_r.bind('<Enter>', lambda e: btn_s_r.config(bg='#808080'))
    btn_s_r.bind('<Leave>', lambda e: btn_s_r.config(bg='#c0c0c0'))
    btn_toggle.bind('<Enter>', lambda e: btn_toggle.config(bg='#808080'))
    btn_toggle.bind('<Leave>', lambda e: btn_toggle.config(bg='#c0c0c0'))


# creating sc_toggle_button_1 frame button function

def sc_toggle_button_1():
    # sc_toggle_button frame button (DEG: en_sin, en_cos, en_tan)............!

    btn_en_sin = Button(sc_toggle_button_frame_1, text='sin\u207b\u00b9', font=font, height=1, width=4, relief='ridge',
                        bg='#c0c0c0',
                        activebackground='white', border=2, command=lambda: click_deg('sin\u207b\u00b9'))
    btn_en_sin.grid(row=0, column=2)
    btn_en_cos = Button(sc_toggle_button_frame_1, text='cos\u207b\u00b9', font=font, height=1, width=4, relief='ridge',
                        bg='#c0c0c0',
                        activebackground='white', border=2, command=lambda: click_deg('cos\u207b\u00b9'))
    btn_en_cos.grid(row=0, column=3)
    btn_en_tan = Button(sc_toggle_button_frame_1, text='tan\u207b\u00b9', font=font, height=1, width=4, relief='ridge',
                        bg='#c0c0c0',
                        activebackground='white', border=2, command=lambda: click_deg('tan\u207b\u00b9'))
    btn_en_tan.grid(row=0, column=4)

    # sc_toggle_button frame button (sc_rt, rt_3, rt_y)............!

    btn_sc_rt = Button(sc_toggle_button_frame_1, text='√', font=font, height=1, width=4, relief='ridge',
                       bg='#c0c0c0',
                       activebackground='white', border=2, command=rt)
    btn_sc_rt.grid(row=0, column=0)
    btn_rt_3 = Button(sc_toggle_button_frame_1, text='\u00b3√', font=font, height=1, width=4, relief='ridge',
                      bg='#c0c0c0',
                      activebackground='white', border=2, command=rt_3)

    btn_rt_3.grid(row=0, column=1)
    btn_rt_y = Button(sc_toggle_button_frame_1, text='\u02e3√', font=font, height=1, width=4, relief='ridge',
                      bg='#c0c0c0',
                      activebackground='white', border=2, command=lambda: entry.insert(END, '**(1/'))
    btn_rt_y.grid(row=1, column=1)

    # sc_toggle_button frame button (h, 10x, x10x, en_x )............!

    btn_h = Button(sc_toggle_button_frame_1, text='h', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                   activebackground='white', border=2, command=lambda: entry.insert(END, (6.626 * 10 ** -34)))
    btn_h.grid(row=1, column=0)
    btn_10x = Button(sc_toggle_button_frame_1, text='10\u02e3', font=font, height=1, width=4, relief='ridge',
                     bg='#c0c0c0',
                     activebackground='white', border=2, command=lambda: entry.insert(END, '10**'))
    btn_10x.grid(row=1, column=2)
    btn_x10_x = Button(sc_toggle_button_frame_1, text='x10\u02e3', font=font, height=1, width=4, relief='ridge',
                       bg='#c0c0c0', activebackground='white', border=2, command=lambda: entry.insert(END, '*10**'))
    btn_x10_x.grid(row=1, column=3)
    btn_en_x = Button(sc_toggle_button_frame_1, text='x\u207b\u00b9', font=font, height=1, width=4, relief='ridge',
                      bg='#c0c0c0',
                      activebackground='white', border=2, command=lambda: entry.insert(0, '1/'))
    btn_en_x.grid(row=1, column=4)

    # sc_toggle_button frame button (DEG: en_sin, en_cos, en_tan) hover effect............!

    btn_en_sin.bind('<Enter>', lambda e: btn_en_sin.config(bg='#808080'))
    btn_en_sin.bind('<Leave>', lambda e: btn_en_sin.config(bg='#c0c0c0'))
    btn_en_cos.bind('<Enter>', lambda e: btn_en_cos.config(bg='#808080'))
    btn_en_cos.bind('<Leave>', lambda e: btn_en_cos.config(bg='#c0c0c0'))
    btn_en_tan.bind('<Enter>', lambda e: btn_en_tan.config(bg='#808080'))
    btn_en_tan.bind('<Leave>', lambda e: btn_en_tan.config(bg='#c0c0c0'))

    # sc_toggle_button frame button (sc_rt, rt_3, rt_y) hover effect............!

    btn_sc_rt.bind('<Enter>', lambda e: btn_sc_rt.config(bg='#808080'))
    btn_sc_rt.bind('<Leave>', lambda e: btn_sc_rt.config(bg='#c0c0c0'))
    btn_rt_3.bind('<Enter>', lambda e: btn_rt_3.config(bg='#808080'))
    btn_rt_3.bind('<Leave>', lambda e: btn_rt_3.config(bg='#c0c0c0'))
    btn_rt_y.bind('<Enter>', lambda e: btn_rt_y.config(bg='#808080'))
    btn_rt_y.bind('<Leave>', lambda e: btn_rt_y.config(bg='#c0c0c0'))

    # sc_toggle_button frame button (h, 10x, x10x, en_x ) hover effect............!

    btn_h.bind('<Enter>', lambda e: btn_h.config(bg='#808080'))
    btn_h.bind('<Leave>', lambda e: btn_h.config(bg='#c0c0c0'))
    btn_x10_x.bind('<Enter>', lambda e: btn_x10_x.config(bg='#808080'))
    btn_x10_x.bind('<Leave>', lambda e: btn_x10_x.config(bg='#c0c0c0'))
    btn_10x.bind('<Enter>', lambda e: btn_10x.config(bg='#808080'))
    btn_10x.bind('<Leave>', lambda e: btn_10x.config(bg='#c0c0c0'))
    btn_en_x.bind('<Enter>', lambda e: btn_en_x.config(bg='#808080'))
    btn_en_x.bind('<Leave>', lambda e: btn_en_x.config(bg='#c0c0c0'))


# creating scientific button for sc_button_frame...........!

def toggle_deg_rad():
    if btn_deg_rad['text'] == 'DEG':
        btn_deg_rad.config(text='RAD')

        # sc_toggle_button frame button (RAD: sin, cos, tan)........!

        btn_sin = Button(sc_toggle_button_frame, text='sin', font=font, height=1, width=4, relief='ridge',
                         bg='#c0c0c0',
                         activebackground='white', border=2, command=lambda: click_rad('sin'))
        btn_sin.grid(row=0, column=2)
        btn_cos = Button(sc_toggle_button_frame, text='cos', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                         activebackground='white', border=2, command=lambda: click_rad('cos'))
        btn_cos.grid(row=0, column=3)
        btn_tan = Button(sc_toggle_button_frame, text='tan', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                         activebackground='white', border=2, command=lambda: click_rad('tan'))
        btn_tan.grid(row=0, column=4)

        # sc_toggle_button frame button (RAD: en_sin, en_cos, en_tan)............!

        btn_en_sin = Button(sc_toggle_button_frame_1, text='sin\u207b\u00b9', font=font, height=1, width=4,
                            relief='ridge',
                            bg='#c0c0c0',
                            activebackground='white', border=2, command=lambda: click_rad('sin\u207b\u00b9'))
        btn_en_sin.grid(row=0, column=2)
        btn_en_cos = Button(sc_toggle_button_frame_1, text='cos\u207b\u00b9', font=font, height=1, width=4,
                            relief='ridge',
                            bg='#c0c0c0',
                            activebackground='white', border=2, command=lambda: click_rad('cos\u207b\u00b9'))
        btn_en_cos.grid(row=0, column=3)
        btn_en_tan = Button(sc_toggle_button_frame_1, text='tan\u207b\u00b9', font=font, height=1, width=4,
                            relief='ridge',
                            bg='#c0c0c0',
                            activebackground='white', border=2, command=lambda: click_rad('tan\u207b\u00b9'))
        btn_en_tan.grid(row=0, column=4)

    else:

        btn_deg_rad.config(text='DEG')

        # sc_toggle_button frame button (DEG: sin, cos, tan)...........!

        btn_sin = Button(sc_toggle_button_frame, text='sin', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                         activebackground='white', border=2, command=lambda: click_deg('sin'))
        btn_sin.grid(row=0, column=2)
        btn_cos = Button(sc_toggle_button_frame, text='cos', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                         activebackground='white', border=2, command=lambda: click_deg('cos'))
        btn_cos.grid(row=0, column=3)
        btn_tan = Button(sc_toggle_button_frame, text='tan', font=font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                         activebackground='white', border=2, command=lambda: click_deg('tan'))
        btn_tan.grid(row=0, column=4)

        # sc_toggle_button frame button (DEG: en_sin, en_cos, en_tan)............!

        btn_en_sin = Button(sc_toggle_button_frame_1, text='sin\u207b\u00b9', font=font, height=1, width=4,
                            relief='ridge', bg='#c0c0c0',
                            activebackground='white', border=2, command=lambda: click_rad('sin\u207b\u00b9'))
        btn_en_sin.grid(row=0, column=2)
        btn_en_cos = Button(sc_toggle_button_frame_1, text='cos\u207b\u00b9', font=font, height=1, width=4,
                            relief='ridge', bg='#c0c0c0',
                            activebackground='white', border=2, command=lambda: click_rad('cos\u207b\u00b9'))
        btn_en_cos.grid(row=0, column=3)
        btn_en_tan = Button(sc_toggle_button_frame_1, text='tan\u207b\u00b9', font=font, height=1, width=4,
                            relief='ridge', bg='#c0c0c0',
                            activebackground='white', border=2, command=lambda: click_rad('tan\u207b\u00b9'))
        btn_en_tan.grid(row=0, column=4)

    # sc_toggle_button frame button (sin, cos, tan) hover effect...................!

    btn_sin.bind('<Enter>', lambda e: btn_sin.config(bg='#808080'))
    btn_sin.bind('<Leave>', lambda e: btn_sin.config(bg='#c0c0c0'))
    btn_cos.bind('<Enter>', lambda e: btn_cos.config(bg='#808080'))
    btn_cos.bind('<Leave>', lambda e: btn_cos.config(bg='#c0c0c0'))
    btn_tan.bind('<Enter>', lambda e: btn_tan.config(bg='#808080'))
    btn_tan.bind('<Leave>', lambda e: btn_tan.config(bg='#c0c0c0'))

    # sc_toggle_button frame button (en_sin, en_cos, en_tan) hover effect............!

    btn_en_sin.bind('<Enter>', lambda e: btn_en_sin.config(bg='#808080'))
    btn_en_sin.bind('<Leave>', lambda e: btn_en_sin.config(bg='#c0c0c0'))
    btn_en_cos.bind('<Enter>', lambda e: btn_en_cos.config(bg='#808080'))
    btn_en_cos.bind('<Leave>', lambda e: btn_en_cos.config(bg='#c0c0c0'))
    btn_en_tan.bind('<Enter>', lambda e: btn_en_tan.config(bg='#808080'))
    btn_en_tan.bind('<Leave>', lambda e: btn_en_tan.config(bg='#c0c0c0'))


# creating scientific button for sc_button_frame (SC_%, !, pi, (, ) )

btn_sc_per = Button(sc_button_frame, text='%', font=sc_font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                    activebackground='#c0c0c0', border=2, command=percent)
btn_sc_per.grid(row=1, column=0)
btn_fact = Button(sc_button_frame, text='x!', font=sc_font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                  activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, 'factorial('))
btn_fact.grid(row=2, column=0)
btn_pi = Button(sc_button_frame, text='π', font=sc_font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, pi))
btn_pi.grid(row=3, column=0)
btn_bk_1 = Button(sc_button_frame, text='(', font=sc_font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                  activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, '('))
btn_bk_1.grid(row=4, column=0)
btn_bk = Button(sc_button_frame, text=')', font=sc_font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                activebackground='#c0c0c0', border=2, command=lambda: entry.insert(END, ')'))
btn_bk.grid(row=4, column=1)

# button for changing DEG, RAD (deg_red)................!

btn_deg_rad = Button(sc_button_frame, text='DEG', font=sc_font, height=1, width=4, relief='ridge', bg='#c0c0c0',
                     activebackground='#c0c0c0', border=2, command=toggle_deg_rad)
btn_deg_rad.grid(row=0, column=3)

# creating scientific button for sc_button_frame (SC_%, !, pi, (, ), deg_rad )................!

btn_sc_per.bind('<Enter>', lambda e: btn_sc_per.config(bg='#808080'))
btn_sc_per.bind('<Leave>', lambda e: btn_sc_per.config(bg='#c0c0c0'))
btn_fact.bind('<Enter>', lambda e: btn_fact.config(bg='#808080'))
btn_fact.bind('<Leave>', lambda e: btn_fact.config(bg='#c0c0c0'))
btn_pi.bind('<Enter>', lambda e: btn_pi.config(bg='#808080'))
btn_pi.bind('<Leave>', lambda e: btn_pi.config(bg='#c0c0c0'))
btn_bk.bind('<Enter>', lambda e: btn_bk.config(bg='#808080'))
btn_bk.bind('<Leave>', lambda e: btn_bk.config(bg='#c0c0c0'))
btn_bk_1.bind('<Enter>', lambda e: btn_bk_1.config(bg='#808080'))
btn_bk_1.bind('<Leave>', lambda e: btn_bk_1.config(bg='#c0c0c0'))
btn_deg_rad.bind('<Enter>', lambda e: btn_deg_rad.config(bg='#808080'))
btn_deg_rad.bind('<Leave>', lambda e: btn_deg_rad.config(bg='#c0c0c0'))


# mode changing function...........!

def normal_clc():
    global font

    # forget all frame..........!

    sc_logo_frame.pack_forget()
    entry.pack_forget()
    m_button_frame.pack_forget()
    sc_toggle_button_frame.pack_forget()
    sc_toggle_button_frame_1.pack_forget()
    sc_button_frame.pack_forget()
    st_button_frame.pack_forget()
    programmer_label_1.pack_forget()
    programmer_label_2.pack_forget()
    normal_logo_frame.pack_forget()
    programmer_logo_frame.pack_forget()

    # packing standard calculator frame......!

    window_center(323, 513)
    normal_logo_frame.pack()
    entry.pack(fill='x', padx=8, pady=10, ipady=15)
    m_button_frame.pack()
    st_button_frame.pack()


def scientific_clc():
    global font
    global add_frame
    font = ('arial', 16, 'italic bold')
    add_frame = sc_button_frame

    # forget all frame..........!

    normal_logo_frame.pack_forget()
    entry.pack_forget()
    m_button_frame.pack_forget()
    st_button_frame.pack_forget()
    sc_toggle_button_frame.pack_forget()
    sc_toggle_button_frame_1.pack_forget()
    sc_button_frame.pack_forget()
    programmer_logo_frame.pack_forget()
    programmer_label_1.pack_forget()
    programmer_label_2.pack_forget()

    # calling some function...........!

    window_center(323, 523)
    button()
    sc_toggle_button()

    # packing scientific frame.........!

    sc_logo_frame.pack()
    entry.pack(fill='x', padx=8, pady=10, ipady=15)
    m_button_frame.pack()
    sc_toggle_button_frame.pack()
    sc_button_frame.pack()


def programmer():
    # forget all frame..........!

    normal_logo_frame.pack_forget()
    entry.pack_forget()
    m_button_frame.pack_forget()
    st_button_frame.pack_forget()
    sc_logo_frame.pack_forget()
    entry.pack_forget()
    sc_toggle_button_frame.pack_forget()
    sc_toggle_button_frame_1.pack_forget()
    sc_button_frame.pack_forget()
    programmer_label_1.pack_forget()
    programmer_label_2.pack_forget()

    # packing programmer frame........!

    programmer_logo_frame.pack()
    programmer_label.pack()
    entry.pack()
    programmer_label_1.pack()
    programmer_label_2.pack()


# creating navigation bar

menubutton = Menubutton(root, image=pic, background='#c0c0c0', activebackground='#c0c0c0', relief='flat', border=0)
menu = Menu(menubutton, tearoff=0)
menubutton['menu'] = menu

menu.add_command(label='   Standard', command=normal_clc, image=pic_standard_menu, compound='left', font=font_menu,
                 background='#c0c0c0', activebackground='white', activeforeground='black', foreground=color)
menu.add_command(label='   Scientific', command=scientific_clc, image=pic_scientific_menu, compound='left',
                 font=font_menu, background='#c0c0c0',
                 activebackground='white', activeforeground='black', foreground=color)
menu.add_command(label='   Programmer', command=programmer, image=pic_programmer_menu, compound='left', font=font_menu,
                 background='#c0c0c0', activebackground='white', activeforeground='black', foreground=color)

menubutton.place(x=6, y=10)

# main loop.......!

root.mainloop()
