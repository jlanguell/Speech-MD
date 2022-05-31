# Main Python File / Application Call File

# Imports
from audio_source import *
from translate import *
from write_source import *


def main():
    # Local Variables
    box = None
    status = None

    # Prompts user to input a name for their virtual machine, to be used in file/title creation
    while not box:
        box = input("Name of HTB Machine: ")

    # User creates or chooses existing file to be used during application runtime
    file = choose_new_or_existing(box)

    # Lists the found audio input devices from system
    list_index()

    # Prompts user to choose an audio input device
    device = get_input()

    # Forever-loop to analyze speech and write to chosen file
    while True:
        status = engine_translate(device, file, box, status)


if __name__ == "__main__":
    main()