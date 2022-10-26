import tkinter as tk
from tkinter import ttk, messagebox

from math import log, sqrt


# Creating app class for the calculator.
# the tk.Tk in the parenthesis afaik just creates a             
class App(tk.Tk):
    # This is useful for the ans button, to save values.
    ANS_RESULT = ''

    def __init__(self):
        super().__init__()

        self.title("Calculator")
        # self.iconbitmap('calc.ico')

        # Starting the func that stores all tkinter settings
        self.create_widgets()

    def create_widgets(self):
        self['padx'] = 5
        self['pady'] = 5

        # - - - - - - - - - - - - - - - - - - - - - 
        # Button command section
        def clear_after_equal():
            if operation_label['text']:
                if operation_label['text'][-1] == '=':
                    operation_label['text'] = ''

        # When key pressing these buttons, I just add a str value to the operation screen.
        def press0():
            clear_after_equal()
            operation_label['text'] += '0'

        def press1():
            clear_after_equal()
            operation_label['text'] += '1'

        def press2():
            clear_after_equal()
            operation_label['text'] += '2'

        def press3():
            clear_after_equal()
            operation_label['text'] += '3'

        def press4():
            clear_after_equal()
            operation_label['text'] += '4'

        def press5():
            clear_after_equal()
            operation_label['text'] += '5'

        def press6():
            clear_after_equal()
            operation_label['text'] += '6'

        def press7():
            clear_after_equal()
            operation_label['text'] += '7'

        def press8():
            clear_after_equal()
            operation_label['text'] += '8'

        def press9():
            clear_after_equal()
            operation_label['text'] += '9'

        def press11():
            clear_after_equal()
            operation_label['text'] += '*'

        def press12():
            clear_after_equal()
            operation_label['text'] += '/'

        def press13():
            clear_after_equal()
            operation_label['text'] += '-'

        def press14():
            clear_after_equal()
            operation_label['text'] += '+'

        def press15():
            clear_after_equal()
            operation_label['text'] += '.'

        def press16():
            clear_after_equal()
            operation_label['text'] += '('

        def press17():
            clear_after_equal()
            operation_label['text'] += ')'

        def press18():
            clear_after_equal()
            operation_label['text'] += 'log('

        def press19():
            clear_after_equal()
            operation_label['text'] += 'sqrt('

        def equal():
            operation_label['text'] += '='
            result()

        def clear_all():
            operation_label['text'] = ''
            result_label['text'] = ''

        def clear_last_digit():
            expression = operation_label['text']
            new_exp = expression[:-1]
            operation_label['text'] = new_exp

        def result():
            expression = operation_label['text']

            result_label['text'] = eval(expression[:-1])

        def ans():
            clear_after_equal()
            if result_label['text'] != '':
                App.ANS_RESULT = result_label['text']
                if App.ANS_RESULT != '':
                    operation_label['text'] = str(App.ANS_RESULT)
            else:
                operation_label['text'] = str(App.ANS_RESULT)

        # - - - - - - - - - - - - - - - - - - - - -
        # Result frame
        result_frame = ttk.Frame(self, relief=tk.RIDGE)
        result_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        operation_label = ttk.Label(result_frame, text="")
        operation_label.grid(row=1, column=1, sticky=tk.W, pady=5, padx=10)

        result_label = ttk.Label(result_frame, text="")
        result_label.grid(row=2, column=1, pady=5, padx=10, sticky=tk.W)

        # - - - - - - - - - - - - - - - - - - - - -
        # function frame
        func_frame = ttk.Frame(self)
        func_frame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        left_parenthesis_btn = tk.Button(func_frame, text='(', width=4, command=press16)
        left_parenthesis_btn.grid(row=1, column=1, pady=5, padx=5, ipadx=1)

        right_parenthesis_btn = tk.Button(func_frame, text=')', width=4, command=press17)
        right_parenthesis_btn.grid(row=1, column=2, pady=5, padx=5, ipadx=1)

        log_btn = tk.Button(func_frame, text='log', width=4, command=press18)
        log_btn.grid(row=1, column=3, pady=5, padx=5, ipadx=1)

        sqrt_btn = tk.Button(func_frame, text='sqrt', width=4, command=press19)
        sqrt_btn.grid(row=1, column=4, pady=5, padx=5, ipadx=1)

        # - - - - - - - - - - - - - - - - - - - - -
        # BOTTOM FRAME
        btm_frame = ttk.Frame(self)
        btm_frame.grid(row=3, column=1)

        # Button Numbers frame
        num_frame = ttk.Frame(btm_frame, relief=tk.RAISED)
        num_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        one_btn = tk.Button(num_frame, text='1', width=4, command=press1)
        one_btn.grid(row=3, column=1, pady=5, padx=5, ipadx=1)

        two_btn = tk.Button(num_frame, text='2', width=4, command=press2)
        two_btn.grid(row=3, column=2, pady=5, padx=5)

        three_btn = tk.Button(num_frame, text='3', width=4, command=press3)
        three_btn.grid(row=3, column=3, pady=5, padx=5)

        four_btn = tk.Button(num_frame, text='4', width=4, command=press4)
        four_btn.grid(row=2, column=1, pady=5, padx=5)

        five_btn = tk.Button(num_frame, text='5', width=4, command=press5)
        five_btn.grid(row=2, column=2, pady=5, padx=5)

        six_btn = tk.Button(num_frame, text='6', width=4, command=press6)
        six_btn.grid(row=2, column=3, pady=5, padx=5)

        seven_btn = tk.Button(num_frame, text='7', width=4, command=press7)
        seven_btn.grid(row=1, column=1, pady=5, padx=5)

        eight_btn = tk.Button(num_frame, text='8', width=4, command=press8)
        eight_btn.grid(row=1, column=2, pady=5, padx=5)

        nine_btn = tk.Button(num_frame, text='9', width=4, command=press9)
        nine_btn.grid(row=1, column=3, pady=5, padx=5)

        zero_btn = tk.Button(num_frame, text='0', width=4, command=press0)
        zero_btn.grid(row=4, column=1, pady=5, padx=5)

        dot_btn = tk.Button(num_frame, text='.', width=4, command=press15)
        dot_btn.grid(row=4, column=2, pady=5, padx=5)

        exp_btn = tk.Button(num_frame, text='EXP', width=4)
        exp_btn.grid(row=4, column=3, pady=5, padx=5)

        # Operations frame
        op_frame = ttk.Frame(btm_frame, relief=tk.RAISED)
        op_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        del_btn = tk.Button(op_frame, text='DEL', width=4, bg='red', fg='white', command=clear_last_digit)
        del_btn.grid(row=1, column=1, pady=5, padx=5)

        ac_btn = tk.Button(op_frame, text='AC', width=4, bg='lightgreen', command=clear_all)
        ac_btn.grid(row=1, column=2, pady=5, padx=5)

        mult_btn = tk.Button(op_frame, text='*', width=4, command=press11)
        mult_btn.grid(row=2, column=1, pady=5, padx=5)

        div_btn = tk.Button(op_frame, text='/', width=4, command=press12)
        div_btn.grid(row=2, column=2, pady=5, padx=5)

        add_btn = tk.Button(op_frame, text='+', width=4, command=press14)
        add_btn.grid(row=3, column=1, pady=5, padx=5)

        min_btn = tk.Button(op_frame, text='-', width=4, command=press13)
        min_btn.grid(row=3, column=2, pady=5, padx=5)

        ans_btn = tk.Button(op_frame, text='Ans', width=4, command=ans)
        ans_btn.grid(row=4, column=1, pady=5, padx=5)

        equal_btn = tk.Button(op_frame, text='=', width=4, command=equal)
        equal_btn.grid(row=4, column=2, pady=5, padx=5)

        # - - - - - - - - - - - - - - - - - - - - -
        # Menus
        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.quitting)
        menubar.add_cascade(label="File", menu=filemenu)

        self.config(menu=menubar)

    def quitting(self):
        answer = messagebox.askyesno("Question", "Do you really want to quit?")
        if answer is True:
            # I need the () at the end if I am not giving the command to a button.
            self.quit()


if __name__ == "__main__":
    app = App()
    app.mainloop()
