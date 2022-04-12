//
// Created by Sean Anderson on 4/29/21.
//

#ifndef RUNNER_BIRD_H
#define RUNNER_BIRD_H
#include <iostream>
#include "shape.h"

class Bird {
private:
    bool wingUp;
    color fill;
    point2D center;
    bool isDay;
public:
    double speed;
    /*Constructors*/
    Bird();
    explicit Bird(color fill);

    /*Destructor*/
    virtual ~Bird() = default;

    /*Getters*/
    double getCenterX() const;
    double getCenterY() const;
    bool getWingUp() const;

    /*Setter*/
    void setWing(bool s);
    void setDay(bool d);
    void setColor(color c);
    void moveX(double deltaX);
    void moveY(double deltaY);
    void flap();

    /*Draw*/
    void draw() const;
};

#endif //RUNNER_BIRD_H
