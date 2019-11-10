import tkinter as tk

root = tk.Tk()
root.title("Encryptodoodles")
frame = tk.Frame(root)
frame.pack()

topframe = tk.Frame(root)
topframe.pack(side=tk.TOP)
bottomframe = tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM)

def get_text_type():
    label = tk.Label(topframe,
        text='Text Type\nOption 1: use .txt file\n'
        'Option 2: enter a message to encrypt or decrypt\n'
        'Enter 1 or 2: ')
    label.pack()

    button1 = tk.Button(root, text = "1", width = 10, height = 2)
    button1.pack(side = tk.TOP)
    button2 = tk.Button(root, text = "2", width = 10, height = 2)
    button2.pack(side = tk.TOP)


def get_cypher_type():
    label = tk.Label(topframe, text='Option 1: encryption\nOption 2: decryption\n'
                       'Enter 1 or 2: ')
    label.pack()

    button1 = tk.Button(root, text = "1", width = 10, height = 2)
    button1.pack(side = tk.TOP)
    button2 = tk.Button(root, text = "2", width = 10, height = 2)
    button2.pack(side = tk.TOP)


def get_encryption_type():
    label = tk.Label(topframe, text='Cipher Options')
    label.pack()

    button1 = tk.Button(root, text = "1: Caesar", width = 10, height = 2)
    button1.pack(side = tk.TOP)
    button2 = tk.Button(root, text = "2: Vigenere", width = 10, height = 2)
    button2.pack(side = tk.TOP)
    button3 = tk.Button(root, text = "3: Enigma", width = 10, height = 2)
    button3.pack(side = tk.TOP)
    button4 = tk.Button(root, text = "4: AES", width = 10, height = 2)
    button4.pack(side = tk.TOP)
    button5 = tk.Button(root, text = "5: Playfair", width = 10, height = 2)
    button5.pack(side = tk.TOP)


def cont():
    label = tk.Label(topframe, text='Continue?')
    label.pack()

    button1 = tk.Button(root, text = "Yes", width = 5, height = 2)
    button1.pack()
    button2 = tk.Button(root, text = "No", width = 5, height = 2)
    button2.pack()


def printSomething(output):
    label = tk.Label(root, text=output)
    label.pack()

root.mainloop()
