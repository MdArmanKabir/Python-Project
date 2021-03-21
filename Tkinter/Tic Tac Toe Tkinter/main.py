import tkinter as tk
from tkinter import messagebox

player = 'X'
count = 0
root = tk.Tk()
root.geometry()


def reset():
    global count
    count = 0

    def button_disable():
        b1.config(state='disabled')
        b2.config(state='disabled')
        b3.config(state='disabled')
        b4.config(state='disabled')
        b5.config(state='disabled')
        b6.config(state='disabled')
        b7.config(state='disabled')
        b8.config(state='disabled')
        b9.config(state='disabled')

    def wining_condition(player_xy):
        bg = '#000000'
        fg = 'RED'
        if b1['text'] == b2['text'] == b3['text'] == player_xy:
            b1.config(bg=bg, disabledforeground=fg)
            b2.config(bg=bg, disabledforeground=fg)
            b3.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', 'Congratulation Player ' + player_xy + ' win...!')

        elif b4['text'] == b5['text'] == b6['text'] == player_xy:
            b4.config(bg=bg, disabledforeground=fg)
            b5.config(bg=bg, disabledforeground=fg)
            b6.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', ' Congratulation Player ' + player_xy + ' win....!')

        elif b7['text'] == b8['text'] == b9['text'] == player_xy:
            b7.config(bg=bg, disabledforeground=fg)
            b8.config(bg=bg, disabledforeground=fg)
            b9.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', ' Congratulation Player ' + player_xy + ' win....!')

        elif b1['text'] == b4['text'] == b7['text'] == player_xy:
            b1.config(bg=bg, disabledforeground=fg)
            b4.config(bg=bg, disabledforeground=fg)
            b7.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', ' Congratulation Player ' + player_xy + ' win....! ')

        elif b2['text'] == b5['text'] == b8['text'] == player_xy:
            b2.config(bg=bg, disabledforeground=fg)
            b5.config(bg=bg, disabledforeground=fg)
            b8.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', ' Congratulation Player ' + player_xy + ' win....! ')

        elif b3['text'] == b6['text'] == b9['text'] == player_xy:
            b3.config(bg=bg, disabledforeground=fg)
            b6.config(bg=bg, disabledforeground=fg)
            b9.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', ' Congratulation Player ' + player_xy + ' win....! ')

        elif b1['text'] == b5['text'] == b9['text'] == player_xy:
            b1.config(bg=bg, disabledforeground=fg)
            b5.config(bg=bg, disabledforeground=fg)
            b9.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', ' Congratulation Player ' + player_xy + ' win....! ')

        elif b3['text'] == b5['text'] == b7['text'] == player_xy:
            b3.config(bg=bg, disabledforeground=fg)
            b5.config(bg=bg, disabledforeground=fg)
            b7.config(bg=bg, disabledforeground=fg)
            button_disable()
            messagebox.showerror('TIC TAC TOE', ' Congratulation Player ' + player_xy + ' win....! ')
        elif count == 9:
            button_disable()
            messagebox.showerror('TIC TAC TOE', '  Match tie...! ')

    def button_clicked(b):

        global player, count
        count += 1
        if b['text'] == '' and player == 'X':
            b.config(text=player)
            wining_condition(player)
            player = 'O'

        elif b['text'] == '' and player == 'O':
            b.config(text=player)
            wining_condition(player)
            player = 'X'
        else:
            messagebox.showerror('TIC TAC TOE', 'Try again')
        print(count)

    root.title('Tic Tac Toe')
    background_colour = '#9370db'

    b1 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b1))
    b1.grid(row=1, column=0)
    b2 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b2))
    b2.grid(row=1, column=1)
    b3 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b3))
    b3.grid(row=1, column=2)
    b4 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b4))
    b4.grid(row=2, column=0)
    b5 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b5))
    b5.grid(row=2, column=1)
    b6 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b6))
    b6.grid(row=2, column=2)
    b7 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b7))
    b7.grid(row=3, column=0)
    b8 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b8))
    b8.grid(row=3, column=1)
    b9 = tk.Button(root, font=('arial', 39, 'bold'), width=4, height=2, bg=background_colour,
                   command=lambda: button_clicked(b9))
    b9.grid(row=3, column=2)


label = tk.Label(root, text='RESET GAME -->', font=('arial', 10, 'bold'), fg='red')
label.grid(row=0, column=0)
reset_btn = tk.Button(root, text='reset', font=('arial', 10, 'bold'), bg='#9370db', fg='black', command=reset)
reset_btn.grid(row=0, column=1)
reset()
tk.mainloop()
