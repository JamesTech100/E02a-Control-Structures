
# E02a-Control-Structures

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
    I expect the program to greet me, then prompt me for my favorite color
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
      The program displayed "Greetings!" then asked me what is my favorite color, after responding to the question, the program stops
  - What do you think the program did with what you typed in answer to the question?
      absolutely nothing, it doesn't store the response anywhere
- Open main02.py. Before running it, describe how this is different than main01.py.
    This program will store the prompted color into a variable named 'color', then prints the input
  - What do you think the color = input() will do?
    stores whatever is input into the variable 'color'
  - Run the program in the terminal and answer the question. Did the program do what you expected?
    yes, the program returned the input I gave
- Open main03.py. Before running it, describe how this is different than main02.py.
  this one contains different responses based on what color is input
  - What is happening on lines 9–12?
    an if/else statement, if the guessed color is 'Red', you will get a different prompt from any other input
  - Why are lines 10 and 12 indented?
    they are the results of the cases of the if/else statements
  - Run the program and answer the question. What happens if you don’t capitalize Red?
    it is not correct, since the if statement requires the response to be capitalized
  - What does this tell you about "color"?
    the "color" string variable is case-sensitive
- Open main04.py. Before running it, describe how this is different than main03.py.
  this contains an 'or' operator inside of the if statement case
  - What problem is this trying to solve?
    the problem of how the program should accept "Red" and "red"
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
    you still receive that they are incorrect, since the casing doesn't match the if statement case
- Open main05.py. What do you expect line 9 to do?
  temporarily changes the color variable to all lowercase, then checks if it matches "red"
  - What problem is it trying to solve?
    the problem of 8 different types of writing the word "red" in different casing
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
    the answer is incorrect, as the spaces are stored into the string
 - Open main06.py. How is line 9 different than in main05.py?
  adds a '.strip' into how it affects the variable, 'color'
   - What would you guess .strip() is doing?
    .strip takes away unnecessary spaces before or after the string
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
    only way i could break writing "red" was typing it out letter by letter with spaces in between characters
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
  responds with "close" if color is pink instead of being incorrect
   - What is happening on line 12?
    detects if color is pink, part of the else if statement cluster
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
  loops the program until the correct color is guessed
   - Why are lines 10–17 indented?
    they are nested in the while loop
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
    it would infinitely display the same message if color isn't red, but not even display anything if color was red
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13?
  this line counts how many attempts at guessing the color are taken
   - What is the purpose of “count”?
    to count attempts at guessing the correct color
   - What is happening on line 22?
    line 21 prints how many tries it took to guess the color
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
  
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
