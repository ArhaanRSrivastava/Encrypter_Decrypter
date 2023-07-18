# importing random module
from tkinter import *
from tkinter.filedialog import askopenfilename
import random
import os

# The main code start from here


root = Tk()
root.geometry("670x490")
root.maxsize(width=670 ,height=490)
root.minsize(width=670 ,height=490)

class Text_base():
    def __init__(self):


        self.root = Tk()
        self.root.geometry("670x490")
        self.root.maxsize(width=670 ,height=490)
        self.root.minsize(width=670 ,height=490)



        # Taking input for the action to take Code or Decode

        def decrypt():
            outpu.delete('1.0', 'end')
            word = inp.get()

            word = word.replace('@@///#%$%^*&^&^%#$%^&*%?}|', 'a')
            word = word.replace('@##$%@%!!#$%#$%??|#%&^&#^%', 'e')
            word = word.replace('!$%@#@#%@#$%@#$%&%$^*&^%^&', 'i')
            word = word.replace('#%@#$^%^*&*$$@^@%^#$&%#^&&', 'o')
            word = word.replace('@#$^$%^$@%^@$%^@#$%#$%#!@#', 'u')
            word = word.removesuffix(' ')
            word = word.removesuffix('\n')
            if len(word) <= 3:
                outpu.insert("1.0", word[::-1])
                print(word[::-1])
            elif len(word) > 3:

                word_prefi = word[0:3]
                word_suffi = word[-3:]
                word = word.replace(word_prefi, "")
                word = word.replace(word_suffi, "")

                last_let = word[-1:]
                left_out_wrd = word[:-1]
                fin_word = last_let + left_out_wrd
                outpu.delete('1.0', 'end-1c')
                outpu.insert("1.0", fin_word)
                print(fin_word)
            elif len(word) == 0:
                outpu.delete('1.0', 'end')
                outpu.insert('1.0', "Please enter a word here don't leave it blank.")

        def encrypt():

            outpu.delete('1.0', 'end-1c')
            alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            word = inp.get()

            if len(word) <= 3:
                word = word[::-1]
                word = word.replace('a', '@@///#%$%^*&^&^%#$%^&*%?}|')
                word = word.replace('e', '@##$%@%!!#$%#$%??|#%&^&#^%')
                word = word.replace('i', '!$%@#@#%@#$%@#$%&%$^*&^%^&')
                word = word.replace('o', '#%@#$^%^*&*$$@^@%^#$&%#^&&')
                word = word.replace('u', '@#$^$%^$@%^@$%^@#$%#$%#!@#')
                print(word)
                outpu.insert('1.0', word)

            elif len(word) > 3:
                fron_let = word[0]
                left_out_word = word[1:]
                final_word = left_out_word + fron_let
                rand_alpha = random.choices(alpha, k=3, )
                rando_alpha = random.choices(alpha, k=3, )
                for i in range(len(rand_alpha)):
                    final_word = str(rand_alpha[i]) + final_word
                    final_word = final_word + str(rando_alpha[i])
                    final_word = final_word.replace('a', '@@///#%$%^*&^&^%#$%^&*%?}|')
                    final_word = final_word.replace('e', '@##$%@%!!#$%#$%??|#%&^&#^%')
                    final_word = final_word.replace('i', '!$%@#@#%@#$%@#$%&%$^*&^%^&')
                    final_word = final_word.replace('o', '#%@#$^%^*&*$$@^@%^#$&%#^&&')
                    final_word = final_word.replace('u', '@#$^$%^$@%^@$%^@#$%#$%#!@#')
                print(final_word)
                outpu.insert('1.0', final_word)

            elif len(word) == 0:
                outpu.insert('1.0', "Please enter a word here don't leave it blank.")

        title = Label(self.root, text="Encrypter/Decrypter", font="lucida 30 bold", fg="#430f58", highlightbackground="#5dacbd",
                    highlightthickness=3.4999999999999999999)
        title.pack()

        inp = StringVar()
        out = StringVar()

        main_frame = Frame(self.root, highlightbackground="#142d4c", highlightthickness=4)
        main_frame.pack(pady=10)
        input_fram = Frame(main_frame)
        input_fram.pack()
        Input = Label(input_fram, text="Input: ", font="calibri 26 bold", fg="#27296d")
        Input.pack(anchor="w", padx=9)
        inpu = Entry(input_fram, font="calibri 30", textvariable=inp)
        inpu.pack(padx=9, pady=9)

        output_fram = Frame(main_frame)
        output_fram.pack(pady=20)
        Output = Label(output_fram, text="Output: ", font="calibri 26 bold", fg="#27296d")
        Output.pack(anchor="w", padx=9)
        outpu = Text(output_fram, font="calibri 20", height=3.5, width=28)
        outpu.pack(side=LEFT)

        verti_scrollbar = Scrollbar(output_fram, command=outpu.yview)
        verti_scrollbar.pack(side=RIGHT, fill=Y, anchor='ne')
        outpu.config(yscrollcommand=verti_scrollbar.set)

        btn_frame = Frame(self.root)
        btn_frame.pack()
        Code = Button(btn_frame, text="Encrypt", command=encrypt, font="calibri 19 bold", bg="#eb2632", fg="white",
                    border=3, borderwidth=0)
        Code.pack(padx=9, pady=9, side=LEFT)

        Decode = Button(btn_frame, text="Decrypt", font="calibri 19 bold", command=decrypt, bg="#a2c11c", fg="black",
                        border=3, borderwidth=0)
        Decode.pack(padx=9, pady=9, side=RIGHT)

        self.root.mainloop()

class Image_base():
    def __init__(self):
        pass


def file_based():
    root.destroy()
    self.root.destroy()
    Image_base()


def text_based():
    text_btn.destroy()
    file_btn.destroy()
    root.destroy()
    Text_base()


def open_file():
    file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        f = open(file, "r")
        f.close()
 




text_btn = Button(root, text="Text Based", command=text_based)
text_btn.pack(padx=50, pady=5, anchor=CENTER)

file_btn = Button(root, text="open_file", command=open_file)
file_btn.pack()

root.mainloop()
