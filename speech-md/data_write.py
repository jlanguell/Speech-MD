# This Script Writes Translated Audio to Specified Write File,
# Including Special Commands

# Imports:
import sys
import pyperclip
from datetime import datetime

# Variables
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
datime = date + "T" + time


def write(file, recog, box):
    with open(file, "a") as f:
        if len(recog.split()) > 1:
            cmd = recog.split()[0] + recog.split()[1]
            if cmd.lower() == 'systemcommand':
                recog = recog.lower()
                recog = recog.partition('system command ')[2]
                if recog == 'clip':
                    f.write(pyperclip.paste() + "\n")
                elif recog == 'code':
                    f.write("```bash\n")
                elif recog == 'end':
                    f.write("```  \n\n")
                elif 'single hash' in recog:
                    if len(recog.split()) > 2:
                        f.write("# " + recog.partition('single hash ')[2].title() + "  \n\n")
                    else:
                        f.write('# ')
                elif 'double hash' in recog:
                    if len(recog.split()) > 2:
                        f.write("## " + recog.partition('double hash ')[2].title() + "  \n\n")
                    else:
                        f.write("## ")
                elif 'triple hash' in recog:
                    if len(recog.split()) > 2:
                        f.write("### " + recog.partition('triple hash ')[2].title() + " \n\n")
                    else:
                        f.write("### ")
                elif recog == 'next line':
                    f.write("  \n")
                elif recog == 'new line':
                    f.write("  \n\n")
                elif recog == 'space':
                    f.write(" ")
                elif recog == 'carrot':
                    f.write("> ")
                elif recog == 'title':
                    f.write('---\ntitle: "HTB Walkthrough: {0}" \ndate: {1} \ncategories:\n  - HackTheBox\n'
                            'header:\n  teaser: /assets/images/HTB/{0}/{0}.png\ntags:\n  - \n---\n\n'.format(box, datime))
                elif recog == 'colon':
                    f.write(":")
                elif recog == 'exit':
                    print("Thanks for using Speech-MD.")
                    sys.exit()
                else:
                    print("System Command '" + recog + "' Not Found.")
            else:
                f.write(recog.capitalize() + ".\n")
    f.close()
    return
