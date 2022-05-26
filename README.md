# Speech-MD: A Speech-to-Markdown Python Application  

![Speech-MD Image](Speech-MD.png)  

## A Little Background:  

Lately, I have been studying cybersecurity concepts, many of which apply to challenges like HackTheBox, TryHackMe and CTFs. I decided to make a **[blog](https://jlanguell.github.io/)** for my write-ups, to include useful notes/commands that may be of help during penetration tests.  

This is my way of tracking this journey, while hopefully giving back to the cyber community in some way. One focus of mine has been on **HackTheBox challenges**, and I have been publishing write-ups for each *retired* box that I complete.  

However, producing the markdown files for each one has grown tedious.  

I built this app out of great curiosity to see if I could **save time by automating some of this file production via voice commands.**  

The idea is to have my microphone turned on and Speech-MD running while I *"hack the box"* in another window, speaking the write-up file into existence.  

As of 26 May 2022, the application currently saves the file as if it were being used in a **Jekyll + Minimal Mistakes** web configuration (this is easy to replace/omit).  

## Features:  

The app is extremely customizable for your own needs. 

Upon running the app, it will:  

1. Attempt to **detect** all of your connected **audio-input devices** and create a list of them for you to choose from  

2. Prompt you to either **create a new markdown file**, or **open an existing one** to append to  

3. **Write all speech** to the markdown file in a semi-pretty way  

4. Accept **pre-defined/customizable commands** from a list if speech begins with *"system command"*  


## Existing System Commands:  

- "clip" :  Pastes current clipboard text  

- "code" :  Begins BASH code-block ('''bash \n)  

- "end" :  Ends a code-block ('''  \n\n)  

- "single/double/triple hash **'Some Title Name Here'**" :  Creates Title size of #/##/### hashes with whatever speech follows the command  

- "next line" : Goes to next line (  \n)  

- "new line" :  Leaves an empty line, then creates new line (  \n\n)  

- "space" :  Creates one space ( )  

- "carrot" :  Creates a markdown indent (> )  

- "title" :  Prints out a HTB + Jekyll specific header for the file  

- "colon" :  Prints a colon (:)  

- "exit" :  Exits the application, prints goodbye  

## Pause Function:  

To pause the application at any time, say "system pause".  

This prompts the application to stop handling/sending audio and waits for a keypress of the "r" key in active terminal to resume.  

