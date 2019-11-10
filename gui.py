from tkinter import *
import tkinter.messagebox

#
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text = 'Button 1', fg='red')
# button2 = Button(topFrame, text = 'Button 1', fg='blue')
# button3 = Button(topFrame, text = 'Button 1', fg='green')
# button4 = Button(bottomFrame, text = 'Button 1', fg='purple')
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)
#
# one = Label(root, text='one', bg='red', fg='white')
# one.pack()
# two = Label(root, text='two', bg='green', fg='black')
# two.pack(fill = X)
# three = Label(root, text= 'three', bg = 'blue', fg = 'white')
# three.pack(side = LEFT, fill = Y)

# label_1 = Label(root, text = 'Name')
# label_2 = Label(root, text = 'Password')
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1)
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# c= Checkbutton(root, text = 'Keep me logged in')
# c.grid(columnspan = 2)
#
# def printName(event):
#     print('hello my name is sichun')
#
# button_1 = Button(root, text = 'print name', )
# button_1.bind("<Button-1>", printName)
# button_1.pack(fill = X)

# def leftClick(event):
#     print('left')
#
# def rightClick(event):
#     print('right')
#
# def middleClick(event):
#     print('middle')
#
# frame = Frame(root, width = 300, height = 250)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>", middleClick)
# frame.bind("<Button-3>", rightClick)
# frame.pack()

#MAKING MENUS
def doNothing():
    print('ok I will do nothing')

root = Tk()

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label = 'file', menu= fileMenu)
fileMenu.add_command(label = 'New project', command = doNothing)
fileMenu.add_command(label = 'New', command = doNothing)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = doNothing)

editMenu = Menu(menu)
menu.add_cascade(label = 'edit', menu= editMenu)
editMenu.add_command(label = 'redo', command = doNothing)

toolbar = Frame(root, bg = 'blue')
insertButt = Button(toolbar, text = 'Insert image', command = doNothing)
insertButt.pack(side = LEFT, padx=2, pady=2)
PrintBut = Button(toolbar, text = 'Print', command = doNothing)
PrintBut.pack(side = LEFT, padx=2, pady=2)

toolbar.pack(side = TOP, fill=X)

status = Label(root, text = 'Preparing to do nothing...', bd=1, relief = SUNKEN, anchor=W)
status.pack(side = BOTTOM, fill = X)

# tkinter.messagebox.showinfo('message', 'title')
# answer = tkinter.messagebox.askquestion('Question title', 'question')
#
# if answer == 'yes':
#     print('console output')


root.mainloop()