import tkinter as tk
from tkinter import *
import pyperclip
import EnigmaTkinter #done
import CaesarTkinter #done
import Readtxt
import VigenereTkinter
import PlayfairTkinter #done
import importlib

LARGE_FONT = ("Verdana", 12)


class Encryptodoodle(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage, EncryptPage, DecryptPage, Caesars, Enigma, Playfair, Vigenere, deCaesar, deEnigma, dePlayfair, deVigenere, Output):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to Encryptodoodle!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        message = Label(self,text='Select an option:', font=LARGE_FONT)
        message.pack(side=TOP, pady = 50)

        button = tk.Button(self, text="ENCRYPTION",
                           command=lambda: controller.show_frame(EncryptPage))
        button.config(height=10, width=40)
        button.pack(side=LEFT, padx=100)

        button2 = tk.Button(self, text="DECRYPTION",
                            command=lambda: controller.show_frame(DecryptPage))
        button2.config(height=10, width=40)
        button2.pack(side=RIGHT, padx=100)

class EncryptPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ENCRYPTION", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(WelcomePage), pady=10, padx=10)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Caesar",
                            command=lambda: controller.show_frame(Caesars), pady=10, padx=10)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Enigma",
                            command=lambda: controller.show_frame(Enigma), pady=10, padx=10)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="Playfair",
                            command=lambda: controller.show_frame(Playfair), pady=10, padx=10)
        button4.pack(pady=10)

        button5 = tk.Button(self, text="Vigenere",
                            command=lambda: controller.show_frame(Vigenere), pady=10, padx=10)
        button5.pack(pady=10)

class Caesars(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Caesar", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to encrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Shift')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()


        button1 = tk.Button(self, text="Encrypt")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            message = entry_1.get()
            message = message.replace('\n', ' ').lower()
            whitelist = 'abcdefghijklmnopqrstuvwxyz '
            message = ''.join(filter(whitelist.__contains__, message))
            encrypted = CaesarTkinter.encrypt(message, entry_2.get())
            results.set(encrypted)
            pyperclip.copy(encrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)

class Enigma(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enigma", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to encrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Rotor Order 1')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()

        label_3 = Label(self, text = 'Rotor Order 2')
        label_3.pack()

        entry_3 = Entry(self)
        entry_3.pack()

        label_4 = Label(self, text = 'Rotor Order 3')
        label_4.pack()

        entry_4 = Entry(self)
        entry_4.pack()

        label_5 = Label(self, text = 'Rotor 1 Position')
        label_5.pack()

        entry_5 = Entry(self)
        entry_5.pack()

        label_6 = Label(self, text = 'Rotor 2 Position')
        label_6.pack()

        entry_6 = Entry(self)
        entry_6.pack()

        label_7 = Label(self, text = 'Rotor 3 Position')
        label_7.pack()

        entry_7 = Entry(self)
        entry_7.pack()


        button1 = tk.Button(self, text="Encrypt")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            message = entry_1.get()
            message = message.replace('\n', ' ').lower()
            whitelist = 'abcdefghijklmnopqrstuvwxyz '
            message = ''.join(filter(whitelist.__contains__, message))
            encrypted = EnigmaTkinter.encrypt(message, entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get(), entry_6.get(), entry_7.get())
            results.set(encrypted)
            pyperclip.copy(encrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)

class Playfair(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Playfair", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to encrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Keyword')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()


        button1 = tk.Button(self, text="Encrypt")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            message = entry_1.get()
            message = message.replace('\n', ' ').lower()
            whitelist = 'abcdefghijklmnopqrstuvwxyz '
            message = ''.join(filter(whitelist.__contains__, message))
            encrypted = PlayfairTkinter.encrypt(message, entry_2.get())
            results.set(encrypted)
            pyperclip.copy(encrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)

class Vigenere(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Vigenere", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to encrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Key')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()


        button1 = tk.Button(self, text="Encrypt")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            message = entry_1.get()
            message = message.replace('\n', ' ').lower()
            whitelist = 'abcdefghijklmnopqrstuvwxyz '
            message = ''.join(filter(whitelist.__contains__, message))
            encrypted = VigenereTkinter.encrypt(message, entry_2.get())
            results.set(encrypted)
            pyperclip.copy(encrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)


class DecryptPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="DECRYPTION", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(WelcomePage), pady=10, padx=10)
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Caesar",
                            command=lambda: controller.show_frame(deCaesar), pady=10, padx=10)
        button2.pack(pady=10)

        button3 = tk.Button(self, text="Enigma",
                            command=lambda: controller.show_frame(deEnigma), pady=10, padx=10)
        button3.pack(pady=10)

        button4 = tk.Button(self, text="Playfair",
                            command=lambda: controller.show_frame(dePlayfair), pady=10, padx=10)
        button4.pack(pady=10)

        button5 = tk.Button(self, text="Vigenere",
                            command=lambda: controller.show_frame(deVigenere), pady=10, padx=10)
        button5.pack(pady=10)

class deCaesar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Caesar", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to decrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Shift')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()


        button1 = tk.Button(self, text="Decrypt")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            decrypted = CaesarTkinter.decrypt(entry_1.get(), entry_2.get())
            results.set(decrypted)
            pyperclip.copy(decrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)

class deEnigma(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enigma", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to Decrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Rotor Order 1')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()

        label_3 = Label(self, text = 'Rotor Order 2')
        label_3.pack()

        entry_3 = Entry(self)
        entry_3.pack()

        label_4 = Label(self, text = 'Rotor Order 3')
        label_4.pack()

        entry_4 = Entry(self)
        entry_4.pack()

        label_5 = Label(self, text = 'Rotor 1 Position')
        label_5.pack()

        entry_5 = Entry(self)
        entry_5.pack()

        label_6 = Label(self, text = 'Rotor 2 Position')
        label_6.pack()

        entry_6 = Entry(self)
        entry_6.pack()

        label_7 = Label(self, text = 'Rotor 3 Position')
        label_7.pack()

        entry_7 = Entry(self)
        entry_7.pack()


        button1 = tk.Button(self, text="Decrypt")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            decrypted = EnigmaTkinter.decrypt(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get(), entry_6.get(), entry_7.get())
            results.set(decrypted)
            pyperclip.copy(decrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)

class dePlayfair(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Playfair", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to decrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Keyword')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()


        button1 = tk.Button(self, text="Decrypt")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            decrypted = PlayfairTkinter.encrypt(entry_1.get(), entry_2.get())
            results.set(decrypted)
            pyperclip.copy(decrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)

class deVigenere(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Vigenere", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = Label(self, text = 'Message to decrypt')
        label_1.pack()

        entry_1 = Entry(self)
        entry_1.pack()

        label_2 = Label(self, text = 'Key')
        label_2.pack()

        entry_2 = Entry(self)
        entry_2.pack()


        button1 = tk.Button(self, text="Decrypted")
         #                   ,command=lambda: controller.show_frame(Output))

        button2 = tk.Button(self, text="Go back",command=lambda: controller.show_frame(WelcomePage))

        results = StringVar()
        results.set('')
        test_result = Label(self, textvariable = results, font=LARGE_FONT)
        test_result.pack()

        def ButtonHandler(t):
            decrypted = VigenereTkinter.decrypt(entry_1.get(), entry_2.get())
            results.set(decrypted)
            pyperclip.copy(decrypted)

            label_10 = Label(self, text='The output has been copied to your clipboard!')
            label_10.pack()

        button1.bind("<Button-1>", lambda t: ButtonHandler(t))
        button1.pack(side=BOTTOM, anchor=S, pady=10)
        button2.pack(side=BOTTOM, anchor=E, padx=10)


class Output(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Output Text", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

app = Encryptodoodle()
app.geometry('1000x600')
app.mainloop()