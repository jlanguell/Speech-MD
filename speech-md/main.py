# Main Python File / Application Call File

# Imports
import argparse
from audio_source import *
from translate import *
from write_source import *


def main():
    # Local Variables
    parser = argparse.ArgumentParser()
    box = None
    status = None

    # Setup Optional Arguments
    parser.add_argument("--Name", help="Name of the HTB Machine")
    parser.add_argument("-E", "--Existing", help="Use an Existing Writeup", action="store_true")
    parser.add_argument("-N", "--New", help="Create a New Writeup", action="store_true")
    args = parser.parse_args()

    # Prompts user to input a name for their virtual machine, to be used in file/title creation
    if not args.Name:
        while not box:
            box = input("Name of HTB Machine: ")
    else:
        box = args.Name

    # User creates or chooses existing file to be used during application runtime
    fileType = None
    if args.Existing:
        fileType = "e"
    if args.New:
        fileType = "n"
    file = choose_new_or_existing(box, fileType)

    # Lists the found audio input devices from system
    list_index()

    # Prompts user to choose an audio input device
    device = get_input()

    # Forever-loop to analyze speech and write to chosen file
    while True:
        status = engine_translate(device, file, box, status)


if __name__ == "__main__":
    main()