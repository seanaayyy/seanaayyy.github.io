//
// Created by Sean Anderson on 5/13/21.
//

#include "graphics.h"
#include "circle.h"
#include "rect.h"
#include "letterButton.h"
#include "word.h"
#include <iostream>
#include <iomanip>
#include <memory>
#include <string>
#include <vector>
using namespace std;

GLdouble width, height;
int wd;
int sPoints, cPoints;
// colors, a fun pastel palette
const color thistle(224.0/255, 187.0/255, 228.0/255);
const color lavender(149.0/255, 125.0/255, 173.0/255);
const color violet(210.0/255, 145.0/255, 188.0/255);
const color cottonCandy(254.0/255, 200.0/255, 216.0/255);
const color lumber(255.0/255, 223.0/255, 211.0/255);

// variables used in testing
const color yellow(1,1,0);
point2D point(100,100);

// control buttons for playing game
LetterButton enter(lavender,{70,70}, 50, "enter word");
LetterButton backSpace(violet,{210,70}, 50, "delete letter");
LetterButton endGame(cottonCandy,{350,70}, 50, "end game");

// score button, but will not be functional with hovering and clicking
double scoreX = 100;
double scoreY = 600;
int scoreInt;
LetterButton scoreGauge(lavender, {scoreX, scoreY}, 30, to_string(scoreInt));
Rect scoreLine(lavender, {350, 600}, {500, 6});

// use enum to switch screens, other global variables
enum Screen {start, game, end};
Screen screen = start;
string letters;
string answer;
string message;
vector<LetterButton> letterButtons;
vector<LetterButton> controlButtons;
vector<Word> solutions;
vector<Word> dictionary;
vector<Word> correctAnswers;
float score;
vector<char> alpha;

void init() {
    width = 700;
    height = 700;
    scoreX = 100;
    scoreY = 600;
    srand(time(0));
    alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    getWordsFromFile("Dictionary.txt", dictionary);
    controlButtons.push_back(enter);
    controlButtons.push_back(backSpace);
    controlButtons.push_back(endGame);
    LetterButton centerLetter(lumber,{width/2.0,height/2.0},50, 'a');
    LetterButton secondLetter(thistle,{(width/2.0)-70,(height/2.0)-113},50, 'a');
    LetterButton thirdLetter(thistle,{(width/2.0)+70,(height/2.0)-113},50, 'a');
    LetterButton fourthLetter(thistle,{(width/2.0)+140,(height/2.0)},50, 'a');
    LetterButton fifthLetter(thistle,{(width/2.0)+70,(height/2.0)+113},50, 'a');
    LetterButton sixthLetter(thistle,{(width/2.0)-70,(height/2.0)+113},50, 'a');
    LetterButton seventhLetter(thistle,{(width/2.0)-140,(height/2.0)},50, 'a');
    letterButtons.push_back(centerLetter);
    letterButtons.push_back(secondLetter);
    letterButtons.push_back(thirdLetter);
    letterButtons.push_back(fourthLetter);
    letterButtons.push_back(fifthLetter);
    letterButtons.push_back(sixthLetter);
    letterButtons.push_back(seventhLetter);
    // initialize random letters and the words to go with it
    // generate random string of letters, no repeat letters
    char letter;
    // make sure letters can make at least 7 words
    while (solutions.size() < 7 && !isPangram()) {
        letters.clear();
        solutions.clear();
        while (letters.size() < 7) {
            letter = alpha[rand() % 26];
            int add = 0;
            for (int i = 0; i < letters.size(); i++) {
                if (letter == letters[i]) {
                    add++;
                }
            }
            if (add == 0) {
                letters.push_back(letter);
                letterButtons[letters.size() - 1].setLetter(letter);
            }
        }
        getPossibleWords(letters, dictionary, solutions);
    }
}

/* Initialize OpenGL Graphics */
void initGL() {
    // Set "clearing" or background color
    glClearColor(255.0/255,204.0/255,229.0/255, 1.0f);
}

/* Handler for window-repaint event. Call back when the window first appears and
 whenever the window needs to be re-painted. */
void display() {
    // Tell OpenGL to use the whole window for drawing
    glViewport(0, 0, 2*width, 2*height); // DO NOT CHANGE THIS LINE

    // Do an orthographic parallel projection with the coordinate
    // system set to first quadrant, limited by screen/window size
    glMatrixMode(GL_PROJECTION); // DO NOT CHANGE THIS LINE
    glLoadIdentity(); // DO NOT CHANGE THIS LINE
    glOrtho(0.0, width, height, 0.0, -1.f, 1.f); // DO NOT CHANGE THIS LINE

    // Clear the color buffer with current clearing color
    glClear(GL_COLOR_BUFFER_BIT); // DO NOT CHANGE THIS LINE

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL); // DO NOT CHANGE THIS LINE

    // Switch between screens
    switch (screen) {
        case start : displayStart();
            break;
        case game : displayGame();
            break;
        case Screen::end : displayEnd();
            break;
    }

    glFlush();  // Render now
}

// Display screen prompts user to hit start button
void displayStart() {
    vector<string> instructions;
    string line = "Welcome to Spelling Bee — a puzzle in which players try to make words from a set of seven unique";
    instructions.push_back(line);
    line = "letters while using the center letter at least once. To spell words, you may click the buttons";
    instructions.push_back(line);
    line = "displayed in the window or type out words using the keyboard (only valid letters will be accepted)";
    instructions.push_back(line);
    line = "Once you have written a word, hit enter on you keyboard or click the 'enter word' button. You may";
    instructions.push_back(line);
    line = "also delete letters from your word by hitting delete on your keyboard or by clicking 'delete letter'.";
    instructions.push_back(line);
    line = "Your progress is tracked at the bottom of the window and your correct answers are displayed to the right.";
    instructions.push_back(line);
    line = "When you are done, click 'end game'. Press '7' on your keyboard to start.";
    instructions.push_back(line);
    glColor3f(1, 1, 1);
    double y = 200;
    for (string&s:instructions) {
        glRasterPos2i(100, y);
        for (const char &letter : s) {
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
        }
        y += 20;
    }
}

void displayGame() {
    for (LetterButton &b:controlButtons) {
        b.draw();
    }
    for (LetterButton &b:letterButtons) {
        b.draw();
    }
    // display word being written by user
    glColor3f(1, 1, 1);
    glRasterPos2i(350 - answer.length()*4, 160);
    for (const char &letter : answer) {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
    }

    // display correct answers by user
    glColor3f(1, 1, 1);
    glRasterPos2i(600, 20);
    for (const char &letter : "Correct answers:") {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
    }
    int x = 600;
    int y = 40;
    for (Word &w:correctAnswers) {
        glRasterPos2i(x, y);
        for (const char &letter : w.getWord()) {
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
        }
        y += 20;
    }

    // Display progress of user, gauge how many correct answers they have
    // Calculate score
    // Tally up total points in solutions
    sPoints = 0;
    for (Word &w : solutions) {
        sPoints += w.getPoints();
    }
    // Tally up points from answers
    cPoints = 0;
    for (Word &w : correctAnswers) {
        cPoints += w.getPoints();
    }
    // Record score
    score = (float(cPoints)/sPoints) * 100;
    // Display message to user depending on score
    if (score <= 20) {
        message = "BEGINNER";
    } else if (score <= 40) {
        message = "MOVING UP";
    } else if (score <= 60) {
        message = "SOLID";
    } else if (score <=80) {
        message = "GREAT";
    } else if (score <= 100) {
        message = "GENIUS";
    }
    // display score gauge at bottom of window, move it to the right as score increases
    scoreInt = score;
    scoreGauge.setCenterX(score * 5 + 100);
    scoreGauge.setMessage(to_string(scoreInt));
    scoreLine.draw();
    scoreGauge.draw();

    // display score message to user
    glColor3f(1, 1, 1);
    glRasterPos2i(350 - (message.length()/2.0)*5, 650);
    for (const char &letter : message) {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
    }
}

void displayEnd() {
    // Calculate score
    // Tally up total points in solutions
    sPoints = 0;
    for (Word &w : solutions) {
        sPoints += w.getPoints();
    }
    // Tally up points from answers
    cPoints = 0;
    for (Word &w : correctAnswers) {
        cPoints += w.getPoints();
    }
    // Record score
    score = (float(cPoints)/sPoints) * 100;

    // Display score to user
    glColor3f(1, 1, 1);
    glRasterPos2i(400, 100);
    // Missed words
    for (const char &letter : "Score:" + to_string(score) + "%") {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
    }
    // Display message to user depending on score
    if (score <= 20) {
        message = "BEGINNER";
    } else if (score <= 40) {
        message = "MOVING UP";
    } else if (score <= 60) {
        message = "SOLID";
    } else if (score <=80) {
        message = "GREAT";
    } else if (score <= 100) {
        message = "GENIUS";
    }
    // display score message to user
    glColor3f(1, 1, 1);
    glRasterPos2i(400, 120);
    for (const char &letter : message) {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
    }

    // Display correct answers to user
    glColor3f(1, 1, 1);
    glRasterPos2i(100, 100);
    // Missed words
    for (const char &letter : "Missed words:") {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
    }
    int missed;
    // Only display words that were not found
    int x = 100;
    int y = 120;
    for (Word&s:solutions) {
        missed = 0;
        for (Word&a:correctAnswers) {
            if (s.getWord() != a.getWord()) {
                missed++;
            }
        }
        if (missed == correctAnswers.size() && s.getWord().length() > 3) {
            // If word will get printed off the page, reposition x and y to make new column of words
            if (y >= 670) {
                x = 200;
                y = 120;
            }
            glRasterPos2i(x, y);
            // Missed words
            for (const char &letter : s.getWord()) {
                glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
            }
            y += 20;
        }
    }
}

// http://www.theasciicode.com.ar/ascii-control-characters/escape-ascii-code-27.html
void kbd(unsigned char key, int x, int y) {
    // escape
    if (key == 27) {
        glutDestroyWindow(wd);
        exit(0);
    }
    // if any letter is pressed and it is a letter displayed as a button, act as if button was pressed
    for (char&c:alpha) {
        if (key == c && screen == game) {
            if (letters.find(c) != std::string::npos) {
                answer.push_back(c);
            }
        }
    }
    // enter key
    if (key == 13 && screen == game) {
        int add = 0;
        for (Word&w: solutions) {
            if (answer == w.getWord()) {
                for (Word &c: correctAnswers){
                    if (answer == c.getWord()) {
                        add++;
                    }
                }
                if (add == 0) {
                    correctAnswers.push_back(answer);
                }
            }
        }
        answer.clear();
    }
    // backspace key
    if (key == 127 && screen == game) {
        answer.pop_back();
    }

    // switch to game screen when 7 pressed
    switch(key){
        case '7' :
            screen = game;
            break;
    }
    glutPostRedisplay();
}

void kbdS(int key, int x, int y) {
    switch(key) {
        case GLUT_KEY_DOWN:

            break;
        case GLUT_KEY_LEFT:

            break;
        case GLUT_KEY_RIGHT:

            break;
        case GLUT_KEY_UP:

            break;
    }
    glutPostRedisplay();
}

void cursor(int x, int y) {
    // Change sky, sun, and moon depending on cursor position on grass
    for (LetterButton&b:letterButtons) {
        if (b.isOverlapping(x, y)) {
            b.hover();
        } else {
            b.release();
        }
    }
    for (LetterButton&b:controlButtons) {
        if (b.isOverlapping(x, y)) {
            b.hover();
        } else {
            b.release();
        }
    }
    glutPostRedisplay();
}

// LetterButton will be GLUT_LEFT_LetterButton or GLUT_RIGHT_LetterButton
// state will be GLUT_UP or GLUT_DOWN
void mouse(int button, int state, int x, int y) {
    // If the left LetterButton is down and the cursor is overlapping with the LetterButton, call the pressDown method.
    // Otherwise, call the release method.
    for (LetterButton&b:letterButtons) {
        if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && b.isOverlapping(x, y)) {
            b.pressDown();
        } else {
            b.release();
        }
        // If the left LetterButton is up and the cursor is overlapping with the LetterButton, add letter
        if (button == GLUT_LEFT_BUTTON && state == GLUT_UP && b.isOverlapping(x, y)) {
            answer.push_back(b.getLetter());
        }
    }

    // Enter button
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && enter.isOverlapping(x, y)) {
        enter.pressDown();
    } else {
        enter.release();
    }
    // If the left LetterButton is up and the cursor is overlapping with the LetterButton, add letter
    if (button == GLUT_LEFT_BUTTON && state == GLUT_UP && enter.isOverlapping(x, y)) {
        int add = 0;
        for (Word&w: solutions) {
            if (answer == w.getWord()) {
                for (Word &c: correctAnswers){
                    if (answer == c.getWord()) {
                        add++;
                    }
                }
                if (add == 0) {
                    correctAnswers.push_back(answer);
                }
            }
        }
        answer.clear();
    }

    // delete button
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && backSpace.isOverlapping(x, y)) {
        backSpace.pressDown();
    } else {
        backSpace.release();
    }
    // If the left LetterButton is up and the cursor is overlapping with the LetterButton, remove last letter
    if (button == GLUT_LEFT_BUTTON && state == GLUT_UP && backSpace.isOverlapping(x, y)) {
        answer.pop_back();
    }

    // end game button
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && endGame.isOverlapping(x, y)) {
        endGame.pressDown();
    } else {
        endGame.release();
    }
    // If the left LetterButton is up and the cursor is overlapping with the LetterButton, move to endGame screen
    if (button == GLUT_LEFT_BUTTON && state == GLUT_UP && endGame.isOverlapping(x, y)) {
        screen = Screen::end;
    }
    glutPostRedisplay();
}

void getWordsFromFile(string filename, vector<Word> &dictionary) {
    // Read daily cases in from file
    ifstream fIn;
    fIn.open("../" + filename);
    string word;

    // while the file stream is in a good state and
    // we are not at the end-of-file
    while (fIn && fIn.peek() != EOF) {
        // Read in the date
        getline(fIn, word, '\n');

        // Create a Word object and add it to the vector if at least four letters long
        if (word.size() > 3) {
            dictionary.push_back(Word(word));
        }
    } fIn.close();
}

void getPossibleWords(string &letters, vector<Word> &dictionary, vector<Word> &solutions) {
    // The first letter must be in all possible words
    char needed = letters[0];
    vector<string> possible;
    // Preliminary, check if central letter in word
    for (Word &w : dictionary) {
        int add = 0;
        for (char &c : w.getWord()) {
            if (c == needed) {
                add++;
            }
        }
        // if the needed letter was found at least once, add the word to possible vector
        if (add > 0) {
            possible.push_back(w.getWord());
        }
    }

    // Secondary, check if all letters in word available
    for (string &w : possible) {
        int accept = 0;
        for (char &c : w) {
            if (c == letters[0]) {
                ++accept;
            } else if (c == letters[1]) {
                ++accept;
            } else if (c == letters[2]) {
                ++accept;
            } else if (c == letters[3]) {
                ++accept;
            } else if (c == letters[4]) {
                ++accept;
            } else if (c == letters[5]) {
                ++accept;
            } else if (c == letters[6]) {
                ++accept;
            }
        }
        // If word has all the right letters and long enough, add to vector solutions
        if (accept == w.length() && w.length() >= 4) {
            solutions.push_back(Word(w));
        }
    }
}

bool isPangram() {
    int pangrams = 0;
    int found = 0;
    for (Word &w: solutions) {
        for (char &c: w.getWord()) {
            for ( char &l: letters) {
                if (c == l) {
                    found++;
                }
            }
            if (found == w.getWord().length()) {
                pangrams++;
            }
        }
    }
    if (pangrams > 0) {
        return true;
    } else {
        return false;
    }
}

bool testLetterButton() {
    bool passed = true;
    // test constructor with letter field
    LetterButton lb(yellow, point, 20, 'a');
    if (lb.getLetter() != 'a') {
        passed = false;
        cout << "FAILED letter constructor test case" << endl;
    }
    // test constructor with string field
    LetterButton lb2(yellow, point, 20, "hello");
    if (lb2.getLetter() != '/') {
        passed = false;
        cout << "FAILED string constructor test case" << endl;
    }
    // test hover function
    lb.hover();
    if (lb.getColor().blue == yellow.blue) {
        passed = false;
        cout << "FAILED hover test case" << endl;
    }
    // test release function
    lb.release();
    if (lb.getColor().blue != yellow.blue) {
        passed = false;
        cout << "FAILED release test case" << endl;
    }
    // test press down function
    lb.pressDown();
    if (lb.getColor().blue == yellow.blue) {
        passed = false;
        cout << "FAILED pressDown test case" << endl;
    }
    return passed;
}

bool testWord() {
    bool passed = true;
    Word w;
    // test word default constructor
    if (w.getWord() != "") {
        passed = false;
        cout << "FAILED word default constructor word test case" << endl;
    }
    if (w.getPoints() != 0) {
        passed = false;
        cout << "FAILED word default constructor points test case" << endl;
    }
    // test word string constructor
    Word w2("hello");
    if (w2.getWord() != "hello") {
        passed = false;
        cout << "FAILED word string constructor word test case" << endl;
    }
    if (w2.getPoints() != 2) {
        passed = false;
        cout << "FAILED word string constructor points test case" << endl;
    }
    return passed;
}

void timer(int dummy) {
    glutPostRedisplay();
    glutTimerFunc(30, timer, dummy);
}


/* Main function: GLUT runs as a console application starting at main()  */
int main(int argc, char** argv) {
    // testing
    if (testLetterButton()) {
        cout << "Passed all letterButton test cases" << endl;
    }
    if (testWord()) {
        cout << "Passed all Word test cases" << endl;
    }

    init();

    glutInit(&argc, argv);          // Initialize GLUT

    glutInitDisplayMode(GLUT_RGBA);

    glutInitWindowSize((int)width, (int)height);
    glutInitWindowPosition(100, 200); // Position the window's initial top-left corner
    /* create the window and store the handle to it */
    wd = glutCreateWindow("Spelling Bee" /* title */ );

    // Register callback handler for window re-paint event
    glutDisplayFunc(display);

    // Our own OpenGL initialization
    initGL();

    // register keyboard press event processing function
    // works for numbers, letters, spacebar, etc.
    glutKeyboardFunc(kbd);

    // register special event: function keys, arrows, etc.
    glutSpecialFunc(kbdS);

    // handles mouse movement
    glutPassiveMotionFunc(cursor);

    // handles mouse click
    glutMouseFunc(mouse);

    // handles timer
    glutTimerFunc(0, timer, 0);

    // Enter the event-processing loop
    glutMainLoop();

    return 0;
}