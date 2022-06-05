# Allows User to Choose New/Existing File from System to Write Markdown in

# Imports
import tkinter
import sys
from tkinter import filedialog as fd
from datetime import date

# Variables
today = date.today()


# Prompts user to pick between a new or existing file
def choose_new_or_existing(box, fileType):
    while fileType != 'e' and fileType != 'n':
        print("Please decide if you wish to write to an existing file or create a new one.")
        print("To choose an existing file, type 'e'")
        print("To choose a new file, type 'n'")
        fileType = input("Input: ").lower()

    # User chose to use existing file
    if fileType == 'e':
        print("You have chosen to use an existing file.")
        file = get_file()
        return file

    # User chose to create new file
    else:
        print("You have chosen to create a new file for box '{box_name}'.".format(box_name=box))
        file = create_file(box)
        return file


# Opens a tkinter file-explorer for user to choose an existing file
def get_file():
    file = None
    print("Please select a file to write to: ")

    # Prevents an empty tkinter window from appearing
    tkinter.Tk().withdraw()

    # Opens tkinter file-explorer and exits application if none selected
    file = fd.askopenfilename(filetypes=[('markdown', '*.md')])
    if file:
        print("File Selected: " + file)
        return file
    else:
        print("No file selected. Exiting...")
        sys.exit()


# If enabled, prompts user to designate a name for the new file to be used
def get_file_name():

    # Currently not using, because auto-generated HTB-style names in place
    file_name = None
    while not file_name:
        file_name = input("Please enter the name of new file to be created: ")
        if file_name:
            print("File Name: " + file_name)
            return file_name


# Opens a tkinter file-explorer for user to select a new-file save destination folder
def get_file_path():
    file_path = None
    print("Please navigate to the folder you wish to create this new file: ")

    # Prevents an empty tkinter window from appearing
    tkinter.Tk().withdraw()

    # Opens tkinter file-explorer and exits application if no directory is selected
    file_path = fd.askdirectory()
    if file_path:
        print("File Path: " + file_path)
        return file_path
    else:
        print("No path selected. Exiting...")
        sys.exit()


# Creates a new .md file based on datetime and HTB box name in selected path
def create_file(box):

    # Currently not calling below command because HTB-style file name generation is in use
    # file_name = get_file_name()
    date = today.strftime("%Y-%m-%d")
    file_name = date + "-" + box.lower()
    file_path = get_file_path()
    file = file_path + "/" + file_name + ".md"
    print("File Created: " + file)
    return file
