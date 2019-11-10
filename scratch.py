import tkinter

root = tkinter.Tk()
root.title("Encryptodoodles")
frame = tkinter.Frame(root)
frame.pack()

topframe = tkinter.Frame(root)
topframe.pack(side=tkinter.TOP)
bottomframe = tkinter.Frame(root)
bottomframe.pack(side=tkinter.BOTTOM)

def get_text_type():
    label = tkinter.Label(topframe,
        text='Text Type\nOption 1: use .txt file\n'
        'Option 2: enter a message to encrypt or decrypt\n'
        'Enter 1 or 2: ')
    label.pack()

    button1 = tkinter.Button(root, text = "1", width = 10, height = 2)
    button1.pack(side = tkinter.TOP)
    button2 = tkinter.Button(root, text = "2", width = 10, height = 2)
    button2.pack(side = tkinter.TOP)


def get_cypher_type():
    label = tkinter.Label(topframe, text='Option 1: encryption\nOption 2: decryption\n'
                       'Enter 1 or 2: ')
    label.pack()

    button1 = tkinter.Button(root, text = "1", width = 10, height = 2)
    button1.pack(side = tkinter.TOP)
    button2 = tkinter.Button(root, text = "2", width = 10, height = 2)
    button2.pack(side = tkinter.TOP)


def get_encryption_type():
    label = tkinter.Label(topframe, text='Cipher Options')
    label.pack()

    button1 = tkinter.Button(root, text = "1: Caesar", width = 10, height = 2)
    button1.pack(side = tkinter.TOP)
    button2 = tkinter.Button(root, text = "2: Vigenere", width = 10, height = 2)
    button2.pack(side = tkinter.TOP)
    button3 = tkinter.Button(root, text = "3: Enigma", width = 10, height = 2)
    button3.pack(side = tkinter.TOP)
    button4 = tkinter.Button(root, text = "4: AES", width = 10, height = 2)
    button4.pack(side = tkinter.TOP)
    button5 = tkinter.Button(root, text = "5: Playfair", width = 10, height = 2)
    button5.pack(side = tkinter.TOP)


def cont():
    label = tkinter.Label(topframe, text='Continue?')
    label.pack()

    button1 = tkinter.Button(root, text = "Yes", width = 5, height = 2)
    button1.pack()
    button2 = tkinter.Button(root, text = "No", width = 5, height = 2)
    button2.pack()


# get_text_type()
# get_cypher_type()
get_encryption_type()
# cont()

root.mainloop()
