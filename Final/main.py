# importing random module
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random
import os

# The main code start from here

root = Tk()
root.geometry("690x510")
root.maxsize(width=690, height=510)
root.minsize(width=690, height=510)
mod = 0

# Taking input for the action to take Code or Decode
def text_based():
    global mod
    global super_fram
    if mod == 0:
        main_title.destroy()
        text_btn.destroy()
        file_btn.destroy()
    elif mod == 1:
        super_fram.destroy()
    elif mod == 2:
        ultra_fram.destroy()
    
    # main_title.destroy()
    # text_btn.destroy()
    # file_btn.destroy()

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

    menu_bar = Menu(root)
    mode_menu = Menu(menu_bar, tearoff=0)
    mode_menu.add_radiobutton(label="Text based", command=text_based)
    mode_menu.add_radiobutton(label="File based", command=file_based)
    menu_bar.add_cascade(label="Mode type", menu=mode_menu)
    root.config(menu=menu_bar)
    super_fram = Frame(root, bg="#455d7a")
    super_fram.pack()
    title = Label(super_fram, text="Encrypter/Decrypter", font="lucida 30 bold", fg="#430f58", highlightbackground="#5dacbd",
                  highlightthickness=3.499999999999999999, bg="#e3e3e3")
    title.pack(pady=5)

    inp = StringVar()
    out = StringVar()

    main_frame = Frame(super_fram, highlightbackground="#142d4c", highlightthickness=4, bg="#e3e3e3")
    main_frame.pack(pady=10)
    input_fram = Frame(main_frame, bg="#e3e3e3")
    input_fram.pack()
    Input = Label(input_fram, text="Input: ", font="calibri 26 bold", fg="#27296d", bg="#e3e3e3")
    Input.pack(anchor="w", padx=9)
    inpu = Entry(input_fram, font="calibri 30", textvariable=inp)
    inpu.pack(padx=9, pady=9)

    output_fram = Frame(main_frame, bg="#e3e3e3")
    output_fram.pack(pady=20)
    Output = Label(output_fram, text="Output: ", font="calibri 26 bold", fg="#27296d", bg="#e3e3e3")
    Output.pack(anchor="w", padx=9)
    outpu = Text(output_fram, font="calibri 20", height=3.5, width=28)
    outpu.pack(side=LEFT)

    verti_scrollbar = Scrollbar(output_fram, command=outpu.yview)
    verti_scrollbar.pack(side=RIGHT, fill=Y, anchor='ne')
    outpu.config(yscrollcommand=verti_scrollbar.set)

    btn_frame = Frame(super_fram, bg="#455d7a")
    btn_frame.pack()
    Code = Button(btn_frame, text="Encrypt", command=encrypt, font="calibri 19 bold", bg="#eb2632", fg="white",
                  border=3, borderwidth=0)
    Code.pack(padx=9, pady=9, side=LEFT)

    Decode = Button(btn_frame, text="Decrypt", font="calibri 19 bold", command=decrypt, bg="#a2c11c", fg="black",
                    border=3, borderwidth=0)
    Decode.pack(padx=9, pady=9, side=RIGHT)
    mod = 1

def file_based():
    global mod
    global ultra_fram
    global super_fram
    if mod == 0:
        main_title.destroy()
        text_btn.destroy()
        file_btn.destroy()
    elif mod == 1:
        super_fram.destroy()
    elif mod == 2:
        ultra_fram.destroy()

    global final_doc
    final_doc = ''

    def file_entry():
        global f_lines
        global file_open
        file_open = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file_open == "":
            file = None
        else:
            root.title(os.path.basename(file_open) + " - File")
            f = open(file_open, "r+")
            f_lines = f.read()
            file = os.path.abspath(file_open)
            directory_entry.configure(state="normal")
            directory_entry.insert(0, file)
            directory_entry.configure(state="readonly")
            f.close()

    def decrypt():
        word = f_lines
        word = word.replace('@@///#%$%^*&^&^%#$%^&*%?}|', 'a')
        word = word.replace('@##$%@%!!#$%#$%??|#%&^&#^%', 'e')
        word = word.replace('!$%@#@#%@#$%@#$%&%$^*&^%^&', 'i')
        word = word.replace('#%@#$^%^*&*$$@^@%^#$&%#^&&', 'o')
        word = word.replace('@#$^$%^$@%^@$%^@#$%#$%#!@#', 'u')
        word = word.removesuffix(' ')
        word = word.removesuffix('\n')
        if len(word) <= 3:
            print(word[::-1])
        elif len(word) > 3:
            word_prefi = word[0:3]
            word_suffi = word[-3:]
            word = word.replace(word_prefi, "")
            word = word.replace(word_suffi, "")
            last_let = word[-1:]
            left_out_wrd = word[:-1]
            fin_word = last_let + left_out_wrd
            final_doc = fin_word
            print(final_doc)
            # print(fin_word)
        elif len(word) == 0:
            pass
        fi = os.path.basename(file_open)
        fi = fi.replace("(Encrypted)", "")
        fi = fi.split('.')

        files = asksaveasfilename(initialfile=f'{fi[0]}_{fi[1]}(Decrypted).txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        with open(files, "w") as te:
            te.write(final_doc)

    def encrypt():
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'm', 'n', 'o',
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        word = f_lines

        if len(word) <= 3:
            word = word[::-1]
            word = word.replace('a', '@@///#%$%^*&^&^%#$%^&*%?}|')
            word = word.replace('e', '@##$%@%!!#$%#$%??|#%&^&#^%')
            word = word.replace('i', '!$%@#@#%@#$%@#$%&%$^*&^%^&')
            word = word.replace('o', '#%@#$^%^*&*$$@^@%^#$&%#^&&')
            word = word.replace('u', '@#$^$%^$@%^@$%^@#$%#$%#!@#')
            final_doc = word
            print(word)

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
            final_doc = final_word
            print(final_word)

        elif len(word) == 0:
            pass
        fi = os.path.basename(file_open)
        fi = fi.split('.')
        files = asksaveasfilename(initialfile=f'{fi[0]}_{fi[1]}(Encrypted)', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        with open(files, "w") as te:
            te.write(final_doc)

    menu_bar = Menu(root)
    mode_menu = Menu(menu_bar, tearoff=0)
    mode_menu.add_radiobutton(label="Text based", command=text_based)
    mode_menu.add_radiobutton(label="File based", command=file_based)
    menu_bar.add_cascade(label="Mode type", menu=mode_menu)
    root.config(menu=menu_bar)
    ultra_fram = Frame(root, bg="#455d7a")
    ultra_fram.pack()
    title1 = Label(ultra_fram, text="File Encrypter/Decrypter.", font="lucida 30 bold", fg="#352f44",
                   highlightbackground="#7c73e6",
                   highlightthickness='4', bg="#e3e3e3")
    title1.pack(padx=9, pady=19, fill=X)
    main_frame = Frame(ultra_fram, highlightbackground="#a2a8d3", highlightthickness=4, bg="#e3e3e3")
    main_frame.pack(padx=9, pady=19)
    directory_entry = Entry(main_frame, font="calibri 27 bold", width=45, state="readonly")
    directory_entry.pack(pady=9, padx=50)
    btn_frame = Frame(main_frame, bg="#e3e3e3")
    btn_frame.pack(pady=9)
    directory_btn = Button(btn_frame, text="Browse", font="calibri 17 bold", border=0, command=file_entry, width=8,
                           borderwidth=0, bg="#a2c11c")
    directory_btn.grid(row=1, column=2, padx=25)

    decode_btn = Button(btn_frame, text="Decode", font="calibri 17 bold", border=0, command=decrypt, width=8,
                        borderwidth=0,
                        bg="#a2c11c")
    decode_btn.grid(row=1, column=1, padx=25)

    encode_btn = Button(btn_frame, text="Encode", font="calibri 17 bold", border=0, command=encrypt, width=8,
                        borderwidth=0,
                        bg="#a2c11c")
    encode_btn.grid(row=1, column=3, padx=25)
    mod = 2



root.configure(bg="#455d7a")
photo = PhotoImage(file="text (1).png")
photo2 = PhotoImage(file="folder (2).png")
main_title = Label(root, text="File and Text based Encrypter/Decryper", font="lucida 25 bold", highlightthickness=4,
                   highlightbackground="#66bfbf", bg="#e3e3e3")
main_title.pack(pady=5)
text_btn = Button(root, text="Text Based", image=photo, command=text_based, font="lucida 20 bold", compound="top",
                  borderwidth=0, bg="#e3e3e3")
text_btn.pack(padx=25, pady=5, side=LEFT)

file_btn = Button(root, text="File Based", image=photo2, command=file_based, font="lucida 20 bold", compound="top",
                  borderwidth=0, bg="#e3e3e3")
file_btn.pack(side=RIGHT, padx=25, pady=5)

root.mainloop()
