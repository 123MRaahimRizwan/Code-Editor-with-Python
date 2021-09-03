"""
Project : IDE with Python
Author : M.Raahim Rizwan
"""

# Importing the libraries
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

root = Tk()
# Setting the title
root.title("IDE - Visual Studio Code")
file_path = ""
# Creating functions for the menu items


def set_file_path(path):
    """
    Saves the file
    """
    global file_path
    file_path = path


def run():
    """
    Executes the code
    """
    if file_path == "":
        save_prompt = Toplevel()
        text = Label(save_prompt, text="Save your code before executing it",
                     height=5, width=40, bg="yellow", fg="black")
        text.pack()
        return
    command = f"python {file_path}"
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert(END, output)
    code_output.insert(END, error)


def save_as():
    """
    Saves the file by asking the path to save.
    """
    if file_path == "":
        path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def open_file():
    """
    Opens the file from the user's system
    """
    path = askopenfilename(filetypes=[("Python Files", "*.py")])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def cut():
    """
    Cuts the selected area
    """
    global editor
    editor.event_generate("<<Cut>>")


def copy():
    """
    Copies the sentence
    """
    global editor
    editor.event_generate("<<Copy>>")


def paste():
    """
    Pastes the sentence
    """
    global editor
    editor.event_generate("<<Paste>>")


# Creating the menu bar
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

editmenu = Menu(menu_bar, tearoff=0)
editmenu.add_command(label='Cut', command=cut)
editmenu.add_command(label='Copy', command=copy)
editmenu.add_command(label='Paste', command=paste)
menu_bar.add_cascade(label='Edit', menu=editmenu)


run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)


root.config(menu=menu_bar)


# Creating text area
editor = Text()
editor.pack()

# Creating output area
code_output = Text(height=11)
code_output.pack()
# Setting the icon
root.wm_iconbitmap("icon.ico")

root.mainloop()
