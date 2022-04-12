//
// Created by Sean Anderson on 5/13/21.
//

#ifndef FINAL_PROJECT_SANDER15_GRAPHICS_H
#define FINAL_PROJECT_SANDER15_GRAPHICS_H

#include <stdlib.h>
#include <string>
#include <vector>
#include "word.h"
using namespace std;
#ifdef _WIN32
#include <windows.h>
#else
#include <sys/time.h>
#endif

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

// Program initialization NOT OpenGL/GLUT dependent,
// as we haven't created a GLUT window yet

void init();

// Initialize OpenGL Graphics
void InitGL();

// Callback functions for GLUT

// Draw the window - this is where all the GL actions are
void display();

// Draw the start screen
void displayStart();

// Draw the game screen
void displayGame();

// Draw the end screen
void displayEnd();

// Trap and process alphanumeric keyboard events
void kbd(unsigned char key, int x, int y);

// Trap and process special keyboard events
void kbdS(int key, int x, int y);

// Handle "mouse cursor moved" events
void cursor(int x, int y);

// Calls itself after a specified time
void timer(int dummy);

// Handle mouse button pressed and released events
void mouse(int button, int state, int x, int y);

// Functions for spelling bee game
void getWordsFromFile(string filename, vector<Word> &dictionary);
void getPossibleWords(string &letters, vector<Word> &dictionary, vector<Word> &solutions);
bool isPangram();

// Testing functions
bool testLetterButton();
bool testWord();


#endif //FINAL_PROJECT_SANDER15_GRAPHICS_H
