# Final-Project-sander15
## Final Project Requirements
### Must use concepts from at least two modules
My project uses concepts from modules 2 and 4.
####Module 2
Has-A and Is-A class relationships - the LetterButton class inherits from the Circle class
Testing - there is a testing suite in graphics.cpp main function that tests the functionality
of functions from the Word and LetterButton classes since I made those classes on my own. The
other classes like rect, shape, and circle were copied over from other guided projects, so I
already knew they functioned properly.
####Module 4
Graphics - the game is displayed using graphics and different screens
Keyboard and mouse input - the user can use both the keyboard and the mouse to play my game
### Must include some form of input that is validated
Keyboard - the user may play the game using keyboard input, which is validated; only letters 
displayed on the screen can be used for typing out words.
### Must include at least one visual element
The game is displayed and interactive using graphics
### Must test all nontrivial functions and methods
Functions from my classes LetterButton and Word are tested in main

## Directions for running program
To run this program, just hit run and the start screen for the game will show up after a few moments,
which has instructions written on it for how to play the Spelling Bee game. To get past the start screen,
press '7' on your keyboard. Once at the game screen, you can use your mouse to click the buttons or use
your keyboard to write out your words. Your correct answers are displayed on the right and your progress
is displayed at the bottom of the screen. Once you are done, hit the 'end game' button and you will
be taken to the end screen that displays your score and the words you missed. The game may take a few
seconds to start, since it reads through all of Dictionary.txt, generates a random set of unique letters,
and creates a list of words from those letters.
### Operating system
I have only run this program on Mac, but I used the CMakeLists from another graphics guided project
that includes Windows, so it should work on other operating systems. No installations are necessary for
this program.

## Classes authored by me
This program uses classes and functionality from guided projects: rect, shape, circle. My own classes, Word
and LetterButton, are described below.
### LetterButton
LetterButton is used for the Spelling Bee game and is an adaptation of the Button class from Confettify. 
Seven buttons are displayed in a cluster in the middle of the screen, each with its own unique letter,
and clicking one of them adds that letter to a word you are building. The three other buttons on the
screen are also LetterButtons, but they display strings instead of characters; there are different
constructors for using strings and characters and the draw method works differently for them to display
either string or character.
### Word
The Word class is used for storing words from the Dictionary and how many points they are worth. It only has
two fields for int points and string Word and getters and setters for the fields, no important functions.

## Important methods in graphics.cpp
### display()
The display method will display the start screen, game screen, or end screen depending on the value of 
enum Screen, which is changed by user input.
### displayStart()
This method displays the start screen for the game. It displays instructions for how to play the game
and prompts the user to press '7' to start.
### displayGame() 
This method displays the game to the user by drawing all LetterButton objects and displaying text to show
the user's correct answers and word they are currently writing. 
### displayEnd()
This method displays the words missed by the user, their score out of 100, and a message reflecting
their score (beginner, moving up, solid, great, or genius).
### kbd
Handles keystrokes. While game screen is shown, user can type out words using only the 7 letters
provided instead of clicking the LetterButtons, can use backspace instead of using the LetterButton,
and hit enter on a word instead of using the LetterButton. Pressing 7 sends user to the game screen.
### kbdS
Not used for this program.
### cursor
If user cursor is overlapping with any button on the screen, it calls the hover function and release
when the cursor leaves.
### timer
Not used for this program.
### mouse
Clicking any of the 7 buttons with letter on them will add that letter to the word being spelled. Clicking
any of the control buttons (enter word, delete letter, end game) will check a word to see if it is valid and
add it to the correct answers list, delete the last letter of the word being spelled, and send the user to
the end screen, respectively.
### getWordsFromFile
This method takes in a string filename and vector<Word> &dictionary as arguments. The file (Dictionary.txt)
is read through line by line, adding each word as a Word to the dictionary vector, only accepting words
four letters or longer.
### getPossibleWords
This method takes in the 7 letters being used for the game, the dictionary, and a vector<Word> solutions.
The method loops through the dictionary, checking which words are made of only the 7 letters provided,
and loads the solutions vector with the answers.