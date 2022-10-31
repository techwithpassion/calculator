from tkinter import *

root = Tk()

root.geometry('400x600')
root.resizable(False,False)
# box  = Entry(root,width="50" , font = ('calibri',40,'bold'))
# box.pack()



# clear_screen = Button(root , text = 'C', font = ('calibri',25,'bold') , command = clear_my_screen)
# clear_screen.place(x=10,y = 100)

def clear_my_screen():
    box.config(text = 'hi')
    clear_screen.config(text = 'Clear' , state  = 'disabled')
    # box.place()

def add_my_values():
    make = False
    x = box.get()
    for i in x:
        if '+' in i:
            make = True
    if make:
        print('alright')
        a = ''
        for i in x:   
            if x == int():
                a += x
        print(a)

    else:
        print('leave it! ')
        
 def substract_my_values():
    make = False
    x = box.get()
    for i in x:
        if '-' in i:
            make = True
    if make:
        print('alright')
        a = ''
        for i in x:   
            if x == int():
                a -= x
        print(a)

    else:
        print('leave it! ')
        
def multiply_my_values():
    make = False
    x = box.get()
    for i in x:
        if '*' in i:
            make = True
    if make:
        print('alright')
        a = ''
        for i in x:   
            if x == int():
                a *= x
        print(a)

    else:
        print('leave it! ')
        
def divide_my_values():
    make = False
    x = box.get()
    for i in x:
        if '/' in i:
            make = True
    if make:
        print('alright')
        a = ''
        for i in x:   
            if x == int():
                a /= x
        print(a)

    else:
        print('leave it! ')

box  = Entry(root, width="50" , font = ('calibri',40,'bold'))
box.pack()
clear_screen = Button(root , text = 'C', font = ('calibri',25,'bold') , command = add_my_values)
Button(root , text = 'substract', font = ('calibri',25,'bold') , command = substract_my_values).place(x=10, y=200)
clear_screen.place(x=10,y = 100)


root.mainloop()

