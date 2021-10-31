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


box  = Entry(root, width="50" , font = ('calibri',40,'bold'))
box.pack()
clear_screen = Button(root , text = 'C', font = ('calibri',25,'bold') , command = add_my_values)
clear_screen.place(x=10,y = 100)


root.mainloop()

