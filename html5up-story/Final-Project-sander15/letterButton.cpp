//
// Created by Sean Anderson on 5/13/21.
//

#include "letterButton.h"
#include "graphics.h"
using namespace std;

LetterButton::LetterButton(color fill, point2D center, double radius, char letter) : Circle(fill, center, radius) {
    this->letter = letter;
    originalFill = fill;
    hoverFill = {fill.red + 0.3, fill.green + 0.3, fill.blue + 0.3};
    pressFill = {fill.red - 0.3, fill.green - 0.3, fill.blue - 0.3};
}
LetterButton::LetterButton(color fill, point2D center, double radius, string message) : Circle(fill, center, radius) {
    this->letter = '/';
    this->message = message;
    originalFill = fill;
    hoverFill = {fill.red + 0.1, fill.green + 0.1, fill.blue + 0.1};
    pressFill = {fill.red - 0.1, fill.green - 0.1, fill.blue - 0.1};
}

void LetterButton::draw() const {
    Circle::draw();
    glColor3f(0, 0, 0);
    glRasterPos2i(center.x - (message.length()/2.0)*5, center.y);
    // if letter is set to '/', then it should print the string message
    if (letter != '/') {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, letter);
    } else {
        for (const char &c : message) {
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, c);
        }
    }
}

/* Returns true if the coordinate is inside the box */
bool LetterButton::isOverlapping(int x, int y) const {
    double addX, addY;
    addX = getRadius();
    addY = getRadius();
    // Check if coordinates are within x and y bounds
    if (x >= (center.x - addX) && x <= (center.x + addX) &&
        y >= (center.y - addY) && y <= (center.y +addY)) {
        return true;
    } else {
        return false;
    }
}

/* Change color of the box when the user is hovering over it */
void LetterButton::hover() {
    setColor(hoverFill);
}

/* Change color of the box when the user is clicking on it */
void LetterButton::pressDown() {
    setColor(pressFill);
}

/* Change the color back when the user is not clicking/hovering */
void LetterButton::release() {
    setColor(originalFill);
}

/* Set letter */
void LetterButton::setLetter(char l) {
    letter = l;
}

/* Set message */
void LetterButton::setMessage(std::string m) {
    message = m;
}

/* Get letter */
char LetterButton::getLetter() const {
    return letter;
}

/* Get message */
std::string LetterButton::getMessage() const {
    return message;
}