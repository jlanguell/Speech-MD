# Writes Translated-Audio/Commands to Specified Write File

# Imports:
import sys
import pyperclip
from datetime import datetime

# Variables
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
date_time = date + "T" + time


# Writes data + handles system commands
def write(file, recog, box):

    # Opens passed file to 'a' append
    with open(file, "a") as f:

        # Checks if multiple-word commands begin wih "system command"
        if len(recog.split()) > 1:
            cmd = recog.split()[0] + recog.split()[1]

            # Handles system commands
            if cmd.lower() == 'systemcommand':
                recog = recog.lower()

                # Splits "system command" from the actual command being given into 'recog' variable
                recog = recog.partition('system command ')[2]

                # Command pastes current clipboard item
                if recog == 'clip':
                    f.write(pyperclip.paste() + "\n")

                # Command begins a bash code-block
                elif recog == 'code':
                    f.write("```bash\n")

                # Command ends a code-block
                elif recog == 'end':
                    f.write("```  \n\n")

                # Command creates 'h1' html header with following title name
                elif 'single hash' in recog:
                    if len(recog.split()) > 2:
                        f.write("# " + recog.partition('single hash ')[2].title() + "  \n\n")
                    else:
                        f.write('# ')

                # Command creates 'h2' html header with following title name
                elif 'double hash' in recog:
                    if len(recog.split()) > 2:
                        f.write("## " + recog.partition('double hash ')[2].title() + "  \n\n")
                    else:
                        f.write("## ")

                # Command creates 'h3' html header with following title name
                elif 'triple hash' in recog:
                    if len(recog.split()) > 2:
                        f.write("### " + recog.partition('triple hash ')[2].title() + " \n\n")
                    else:
                        f.write("### ")

                # Command creates 1 new line
                elif recog == 'next line':
                    f.write("  \n")

                # Command creates 2 new lines
                elif recog == 'new line':
                    f.write("  \n\n")

                # Command prints a single space
                elif recog == 'space':
                    f.write(" ")

                # Command begins an indentation
                elif recog == 'carrot':
                    f.write("> ")

                # Command prints a HTB-style title based on box name and current datetime
                elif recog == 'title':
                    f.write('---\ntitle: "HTB Walkthrough: {0}" \ndate: {1} \ncategories:\n  - HackTheBox\n'
                            'header:\n  teaser: /assets/images/HTB/{0}/{0}.png\ntags:\n  - \n---\n\n'.format(box, date_time))

                # Command prints a single colon
                elif recog == 'colon':
                    f.write(":")

                # Command closes the application
                elif recog == 'exit':
                    print("Thanks for using Speech-MD.")
                    sys.exit()

                # Command notifies user the command was not found
                else:
                    print("System Command '" + recog + "' Not Found.")

            # Any non-command text is appended to end of working file
            else:
                f.write(recog.capitalize() + ".\n")

        # Any non-command text is appended to end of working file
            else:
                f.write(recog.capitalize() + ".\n")

    # Close the write function for current processing speech-text request
    f.close()
    return
