from tkinter import *

# creating basic window
window = Tk()


################################### functions ######################################
# 'btn_click' function continuously updates the input field whenever you enters a number
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'btn_clear' function clears the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# 'btn_equal' calculates the expression present in input field
def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval' function evalutes the string expression directly
    # you can also implement your own function to evalute the expression istead of 'eval' function
    input_text.set(result)
    expression = ""

expression = ""
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()


# creating a frame for the input field
input_frame = Frame(window)
input_frame.pack(side = TOP)


# creating a input field inside the 'Frame'
input_field = Entry(input_frame, textvariable = input_text, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # 'ipady' is internal padding to increase the height of input field


# creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(window)
btns_frame.pack()


# first row
clear = Button(btns_frame, text = "C",  command = lambda: btn_clear()).grid(row = 4, column=1)
close=Button(btns_frame, text="close", command=window.quit).grid(row=4, column=3)
divide = Button(btns_frame, text = "/",  command = lambda: btn_click("/")).grid(row = 3, column = 3)


# second row
seven = Button(btns_frame, text = "7",  command = lambda: btn_click(7)).grid(row = 0, column = 0)
eight = Button(btns_frame, text = "8",  command = lambda: btn_click(8)).grid(row = 0, column = 1)
nine = Button(btns_frame, text = "9", command = lambda: btn_click(9)).grid(row = 0, column = 2)
multiply = Button(btns_frame, text = "*",  command = lambda: btn_click("*")).grid(row = 0, column = 3)


# third row
four = Button(btns_frame, text = "4",  command = lambda: btn_click(4)).grid(row = 1, column = 0)
five = Button(btns_frame, text = "5",  command = lambda: btn_click(5)).grid(row = 1, column = 1)
six = Button(btns_frame, text = "6",  command = lambda: btn_click(6)).grid(row = 1, column = 2)
minus = Button(btns_frame, text = "-",  command = lambda: btn_click("-")).grid(row = 1, column = 3)


# fourth row
one = Button(btns_frame, text = "1", command = lambda: btn_click(1)).grid(row = 2, column = 0)
two = Button(btns_frame, text = "2",  command = lambda: btn_click(2)).grid(row = 2, column = 1)
three = Button(btns_frame, text = "3",  command = lambda: btn_click(3)).grid(row =2, column = 2)
plus = Button(btns_frame, text = "+",  command = lambda: btn_click("+")).grid(row =2, column = 3)


# fourth row
zero = Button(btns_frame, text = "0",  command = lambda: btn_click(0)).grid(row = 3, column = 0)
point = Button(btns_frame, text = ".",  command = lambda: btn_click(".")).grid(row = 3, column = 1)
equals = Button(btns_frame, text = "=",  command = lambda: btn_equal()).grid(row = 3, column = 2)


window.mainloop()