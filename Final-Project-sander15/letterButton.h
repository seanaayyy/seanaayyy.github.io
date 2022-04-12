//
// Created by Sean Anderson on 5/13/21.
//

#ifndef FINAL_PROJECT_SANDER15_LETTERBUTTON_H
#define FINAL_PROJECT_SANDER15_LETTERBUTTON_H

#include "circle.h"
#include <string>

class LetterButton : public Circle {
private:
    char letter;
    std::string message;
    color originalFill, hoverFill, pressFill;

public:
    LetterButton(color fill, point2D center, double radius, char letter);
    LetterButton(color fill, point2D center, double radius, std::string message);
    /* Uses OpenGL to draw the box with the label on top */
    void draw() const override;

    /* Returns true if the coordinate is inside the box */
    bool isOverlapping(int x, int y) const;

    /* Change color of the Button when the user is hovering over it */
    void hover();

    /* Change color of the Button when the user is clicking on it */
    void pressDown();

    /* Change the color back when the user is not clicking/hovering */
    void release();

    /* Sets letter */
    void setLetter(char l);

    /* Sets message */
    void setMessage(std::string m);

    /* Gets letter */
    char getLetter() const;

    /* Gets message */
    std::string getMessage() const;
};

#endif //FINAL_PROJECT_SANDER15_LETTERBUTTON_H