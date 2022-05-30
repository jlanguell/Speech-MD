# Speech-MD: A Speech-to-Markdown Python Application  

![Speech-MD Image](Speech-MD.png)  

## A Little Background:  

Lately, I have been studying cybersecurity concepts, many of which apply to challenges like HackTheBox, TryHackMe and CTFs. I decided to make a **[blog](https://jlanguell.github.io/)** for my write-ups, to include useful notes/commands that may be of help during penetration tests.  

This is my way of tracking this journey, while hopefully giving back to the cyber community in some way. One focus of mine has been on **HackTheBox challenges**, and I have been publishing write-ups for each *retired* box that I complete. However, producing the markdown files for each one has grown tedious.  

I built this app out of curiosity to see if I could **save time by automating some of this file production via voice commands.**  
The idea is to have my microphone turned on and Speech-MD running while I *"hack the box"* in another window, speaking the write-up file into existence.  

As of 26 May 2022, the application currently saves the file as if it were being used in a **Jekyll + Minimal Mistakes** web configuration (this is easy to replace/omit).  

## Installation:  


**1)** Clone the repository to a local folder  


**2)** In an IDE or your terminal, please install the necessary modules via pip from the requirements.txt file like so:  


```bash  
pip install -r requirements.txt  
```  


**3)** One of the modules in requirements.txt is PyAudio. If you are not running your IDE as Administrator, or for some other reason, PyAudio may fail to install.  

If this happens, you can manually download the wheel file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio  

First, check your python version and architecture by typing 'python --version' in your terminal.  
There are download options for many different python versions (2.7, 3.8, 3.10, etc.) and builds (x32, x64).  
After downloading it, you need to pip install the module file straight from your downloads folder.  

Wheel for pyaudio, if pip install fails:  

```bash
Example:	
pip install C:\Users\jacob\Downloads\PyAudio-0.2.11-cp38-cp38-win32.whl  
```  


**4)** Additionally, if PyAudio failed to install, pyttsx3 module may have failed as well. Now that you have installed the PyAudio wheel, try to install the pyttsx3 module again.  

```bash  
-pip install pyttsx3

if pypiwin32 not installed with pyttsx3:

-pip install pypiwin32
```  


### NOTE -- Runtime Issue:   


If your app is having trouble running continuously and hanging in the terminal, try this potential fix:  


>If the user clicks into the black console window, the cursor changes to a filled white rectangle, and the app hangs at the next Console.Write statement, until another click is made.
>It is a generic feature of the Console window when its "QuickEdit Mode" is enabled.
>In order to disable that feature, you should:
>
>> **Right-click the head of the terminal and uncheck the "QuickEdit Mode" option of your app's console window in preferences & defaults at run-time**


## Features:  

The app is extremely customizable for your own needs. 

Upon running the app, it will:  

1. Attempt to **detect** all of your connected **audio-input devices** and create a list of them for you to choose from  

2. Prompt you to either **create a new markdown file**, or **open an existing one** to append to  

3. **Write all speech** to the markdown file in a semi-pretty way  

4. Accept **pre-defined/customizable commands** from a list if speech begins with *"system command"*  
>>
> * System Commands can be edited in Speech-MD/speech-md/data_write.py


## Existing System Commands:  


**NOTE : All existing commands are pretexted by saying "system command" before each one**  



> **"clip"** :  
>> 
> * Pastes current clipboard text  

> **"code"** :  
>> 
> * Begins BASH code-block ('''bash \n)  

> **"end"** :  
>> 
> * Ends a code-block ('''  \n\n)  

> **"single/double/triple hash 'title'"** :  
>> 
> * Creates 'title' with size of h1/h2/h3   

> **"next line"** :  
>> 
> * Goes to next line (  \n)  

> **"new line"** :  
>> 
> * Leaves an empty line, then creates new line (  \n\n)  

> **"space"** :  
>> 
> * Creates one space ( )  

> **"carrot"** :  
>> 
> * Creates a markdown indent (> )  

> **"title"** :  
>> 
> * Prints out a HTB + Jekyll specific header for the file  

> **"colon"** :  
>> 
> * Prints a colon (:)

> **"pause"** :  
>> 
> * Pauses the application; must press 'r' inside terminal/IDE to resume  

> **"exit"** :  
>> 
> * Exits the application, prints goodbye  


## Pause Function:  

To pause the application at any time, say "system command pause".  

This prompts the application to stop handling/sending audio and waits for a keypress of the "r" key in active terminal to resume.  

