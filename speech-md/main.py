# Main

# Imports
from audio_source import *
from translate import *
from write_source import *


def main():
    box = None
    status = None

    while not box:
        box = input("Name of HTB Machine: ")

    file = choose_new_or_existing(box)
    list_index()
    device = get_input()

    while True:
        status = engine_translate(device, file, box, status)


if __name__ == "__main__":
    main()