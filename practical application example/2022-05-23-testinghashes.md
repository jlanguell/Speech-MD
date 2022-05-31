---
title: "HTB Walkthrough: TestingHashes" 
date: 2022-05-23T01:07:59 
categories:
  - HackTheBox
header:
  teaser: /assets/images/HTB/TestingHashes/TestingHashes.png
tags:
  - 
---

# Testing Hashes  

This test was done to illustrate the use of hashtags as title markers.
The main purpose of this is to ensure that titles after the hashtags are capitalized using pythons title function.
  
## A Demonstration  

I am editing the data right file.
It should look a little something like this.
  
```bash
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
                    f.write("```  \n")
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
```  
  
## Summary  

> Note, if everything went according to plan, this should be a beautiful markdown file.
  
### Suggestions  

If you have any additional questions or any constructive criticism please email me at the link below.
Additionally, shoot me an email if you would like to be part of the github repository contributors list.
  
> xxxxxxxxxxxxxxx@gmail.com
