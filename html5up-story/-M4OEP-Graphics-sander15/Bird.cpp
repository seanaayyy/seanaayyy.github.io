//
// Created by Sean Anderson on 4/29/21.
//

#include "Bird.h"
#include "graphics.h"
#include <iostream>
#include "math.h"
#include "shape.h"
using namespace std;

/********************* Bird Class ********************/

Bird::Bird() : wingUp(true), fill({(rand()%255)/255.0, rand()%255/255.0, rand()%255/255.0}),
               center(1000,rand()%400 + 100), speed(rand()%6+4){
}

Bird::Bird(color fill) : wingUp(true), fill(fill), center(1000,rand()%200 + 200),
speed(rand()%4+1){
}

double Bird::getCenterX() const {
    return center.x;
}

double Bird::getCenterY() const {
    return center.y;
}

bool Bird::getWingUp() const {
    return wingUp;
}

void Bird::setWing(bool s) {
    wingUp = s;
}

void Bird::setDay(bool d) {
    isDay = d;
}

void Bird::setColor(color c) {
    fill = c;
}

void Bird::moveX(double deltaX) {
    center.x += deltaX;
}

void Bird::moveY(double deltaY) {
    center.y += deltaY;
}

void Bird::flap() {
    // flap bird's wings, move it up and down
    if (wingUp == true) {
        center.y -= 10;
        wingUp = false;
    } else if (wingUp == false) {
        center.y += 10;
        wingUp = true;
    }
}

void Bird::draw() const{
    // if daytime, draw a bird
    if (isDay) {
        // Set drawing color to fill color
        glColor3f(fill.red, fill.green, fill.blue);
        // Draw body of bird as circle as Triangle fan
        glBegin(GL_TRIANGLE_FAN);
        // Draw center point
        glVertex2i(center.x, center.y);
        // Draw points on edge of circle
        for (double i = 0; i < 2.0 * PI + 0.05; i += (2.0 * PI) / 360.0) {
            glVertex2i(center.x + (10 * cos(i)),
                       center.y + (10 * sin(i)));
        }
        // Draw head of bird as circle
        // Draw center point
        glVertex2i(center.x - 4, center.y);
        // Draw points on edge of circle
        for (double i = 0; i < 2.0 * PI + 0.05; i += (2.0 * PI) / 360.0) {
            glVertex2i(center.x - 4 + (5 * cos(i)),
                       center.y + (5 * sin(i)));
        }
        // Draw beak of bird as triangle
        glBegin(GL_TRIANGLES);
        // Draw beak in yellow
        glColor3f(1, 1, 0);
        // Draw points of beak
        glVertex2i(center.x - 30, center.y);
        glVertex2i(center.x - 13, center.y - 4);
        glVertex2i(center.x - 13, center.y + 4);
        // Draw wing as triangle
        glColor3f(fill.red - 0.1, fill.green - 0.1, fill.blue - 0.1);
        // Draw points of wing
        if (wingUp) {
            glVertex2i(center.x - 7, center.y);
            glVertex2i(center.x, center.y - 20);
            glVertex2i(center.x + 7, center.y);
        } else {
            glVertex2i(center.x - 7, center.y);
            glVertex2i(center.x, center.y + 20);
            glVertex2i(center.x + 7, center.y);
        }
    } else {
        // Set drawing color to black
        glColor3f(0,0,0);
        // Draw body of Bat as circle as Triangle fan
        glBegin(GL_TRIANGLE_FAN);
        // Draw center point
        glVertex2i(center.x, center.y);
        // Draw points on edge of circle
        for (double i = 0; i < 2.0*PI+0.05; i += (2.0*PI)/360.0) {
            glVertex2i(center.x + (10 * cos(i)),
                       center.y + (10 * sin(i)));
        }
        // Draw head of Bat as circle
        // Draw center point
        glVertex2i(center.x - 6, center.y);
        // Draw points on edge of circle
        for (double i = 0; i < 2.0*PI+0.05; i += (2.0*PI)/360.0) {
            glVertex2i(center.x - 6 + (8 * cos(i)),
                       center.y + (8 * sin(i)));
        }
        // Draw ears of Bat as triangle
        glBegin(GL_TRIANGLES);
        // Draw ears in dark gray
        glColor3f(0.1,0.1,0.1);
        // Draw points of ear
        glVertex2i(center.x - 18, center.y - 7);
        glVertex2i(center.x - 16, center.y - 15);
        glVertex2i(center.x - 14, center.y - 7);
        // Draw wing as triangle
        glColor3f(0.1,0.1,0.1);
        // Draw points of wing
        if (wingUp) {
            glVertex2i(center.x - 7, center.y);
            glVertex2i(center.x, center.y - 20);
            glVertex2i(center.x + 7, center.y);
        } else {
            glVertex2i(center.x - 7, center.y);
            glVertex2i(center.x, center.y + 20);
            glVertex2i(center.x + 7, center.y);
        }
    }
    // End drawing
    glEnd();
}