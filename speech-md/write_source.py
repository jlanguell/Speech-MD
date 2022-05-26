# Ultimately Decides a File Path to Write Markdown To

# Imports
import tkinter
from tkinter import filedialog as fd
from datetime import date
import sys

# Variables
today = date.today()


def choose_new_or_existing(box):
    filetype = None

    while filetype != 'e' and filetype != 'n':
        print("Please decide if you wish to write to an existing file or create a new one.")
        print("To choose an existing file, type 'e'")
        print("To choose a new file, type 'n'")
        filetype = input("Input: ").lower()
    if filetype == 'e':
        file = get_file()
        return file
    else:
        file = create_file(box)
        return file


def get_file():
    file = None
    print("Please select a file to write to: ")
    # prevents an empty tkinter window from appearing
    tkinter.Tk().withdraw()

    file = fd.askopenfilename(filetypes=[('markdown', '*.md')])
    if file:
        print("File Selected: " + file)
        return file
    else:
        print("No file selected. Exiting...")
        sys.exit()


def get_file_name():
    # Currently not using, because auto-generated HTB-style names
    file_name = None
    while not file_name:
        file_name = input("Please enter the name of new file to be created: ")
        if file_name:
            print("File Name: " + file_name)
            return file_name


def get_file_path():
    file_path = None
    print("Please navigate to the folder you wish to create this new file: ")
    tkinter.Tk().withdraw()
    file_path = fd.askdirectory()
    if file_path:
        print("File Path: " + file_path)
        return file_path
    else:
        print("No path selected. Exiting...")
        sys.exit()


def create_file(box):
    # Currently not calling below command because HTB-style file name generation is in use
    # file_name = get_file_name()
    date = today.strftime("%Y-%m-%d")
    file_name = date + "-" + box.lower()
    file_path = get_file_path()
    file = file_path + "/" + file_name + ".md"
    print("File Created: " + file)
    return file
